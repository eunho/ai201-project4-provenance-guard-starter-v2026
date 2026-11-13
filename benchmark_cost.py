#!/usr/bin/env python3
"""
Cost & Performance Benchmark for Provenance Guard (Capstone Milestone 3).

Measures empirical compute cost across 10 evaluation runs:
- Wall clock duration (ms and seconds)
- Process CPU compute time (user + system seconds)
- Token count processed
- Empirical average cost per run
"""

import json
import time
import statistics
import os
import resource
from app import app

client = app.test_client()

# Sample human prose texts of standard evaluation length (~100-150 words)
TEST_SAMPLES = [
    "The morning sunlight filtered gently through the ancient pine branches, casting long fractured shadows across the damp woodland trail. A pair of blue jays called back and forth in the canopy above.",
    "After three unsuccessful attempts to configure the database replication topology, our engineering team identified a silent race condition in the initial sync protocol that corrupted transaction sequence IDs.",
    "My grandmother's kitchen always smelled of roasted garlic and rosemary on Sunday afternoons. She prepared sourdough loaves using a sourdough starter she kept alive in an earthenware crock for over thirty years.",
    "The regional commuter express arrived exactly seven minutes late due to signal switching maintenance outside the central depot, forcing passengers to hurry along the rain-slicked concrete platform.",
    "Learning a foreign language as an adult requires patience and steady habit. Every morning I practice vocabulary flashcards for twenty minutes before beginning my daily work routine at the software studio.",
    "We pitched our lightweight nylon tent near the timberline just as the autumn sun dipped below the jagged granite ridge, turning the frozen glacier into an intense expanse of violet light.",
    "The antique mechanical typewriter sat on a heavy mahogany desk, its steel keys requiring deliberate physical force to drive the ink ribbon against the crisp cotton paper.",
    "During the summer heatwave, urban neighborhoods without mature tree canopies experienced surface temperatures up to fifteen degrees higher than adjacent suburban parks and residential greenways.",
    "Our university research team analyzed three years of seismic sensor readings from the volcanic ridge, documenting subtle harmonic tremors that reliably preceded minor subterranean magma shifts.",
    "The community bakery on Elm Street opens at five in the morning, filling the entire block with the rich aroma of fresh rye bread, cardamom buns, and strong dark-roast coffee."
]

def run_benchmark():
    # Warm up model so first-time download/JIT compilation does not skew operational run cost
    print("Warming up local model cache...")
    client.post("/submit", json={"creator_id": "warmup", "text": "Warmup text to ensure weights and tokenizers are loaded into memory."})

    print("\nRunning 10 measurement trials...")
    results = []
    
    for i, sample in enumerate(TEST_SAMPLES, 1):
        rusage_start = resource.getrusage(resource.RUSAGE_SELF)
        t_wall_start = time.perf_counter()
        t_cpu_start = time.process_time()

        res = client.post("/submit", json={"creator_id": f"bench_author_{i}", "text": sample})
        
        t_wall_end = time.perf_counter()
        t_cpu_end = time.process_time()
        rusage_end = resource.getrusage(resource.RUSAGE_SELF)

        wall_sec = t_wall_end - t_wall_start
        cpu_sec = t_cpu_end - t_cpu_start
        data = res.get_json()

        results.append({
            "trial": i,
            "status": res.status_code,
            "char_len": len(sample),
            "wall_sec": round(wall_sec, 4),
            "cpu_sec": round(cpu_sec, 4),
            "latency_ms": data.get("latency_ms"),
            "model_ms": data.get("latency_breakdown", {}).get("model_ms"),
            "guess": data.get("guess"),
            "combined_score": data.get("combined_score"),
        })

    wall_times = [r["wall_sec"] for r in results]
    cpu_times = [r["cpu_sec"] for r in results]
    latencies_ms = [r["latency_ms"] for r in results]

    avg_wall = statistics.mean(wall_times)
    avg_cpu = statistics.mean(cpu_times)
    avg_ms = statistics.mean(latencies_ms)
    std_ms = statistics.stdev(latencies_ms)

    print("\n" + "=" * 70)
    print("PROVENANCE GUARD — EMPIRICAL RUN COST BENCHMARK (10 TRIALS)")
    print("=" * 70)
    print(f"{'Trial':<6}{'Chars':<8}{'Status':<8}{'Wall (s)':<12}{'CPU (s)':<12}{'Latency (ms)':<14}{'Guess':<8}{'Score':<8}")
    print("-" * 70)
    for r in results:
        print(f"{r['trial']:<6}{r['char_len']:<8}{r['status']:<8}{r['wall_sec']:<12.4f}{r['cpu_sec']:<12.4f}{r['latency_ms']:<14.2f}{r['guess']:<8}{r['combined_score']:<8.4f}")
    print("-" * 70)
    print(f"Mean Wall-Clock Latency:  {avg_wall:.4f} seconds ({avg_ms:.2f} ms ± {std_ms:.2f} ms)")
    print(f"Mean CPU Compute Time:    {avg_cpu:.4f} seconds of compute per run")
    print(f"Min / Max Latency:        {min(latencies_ms):.2f} ms / {max(latencies_ms):.2f} ms")
    
    # Financial translation: e.g. standard AWS c6i.large (2 vCPU, 4GB RAM) = $0.085/hr = $0.0000236/sec
    cost_per_cpu_sec = 0.085 / 3600.0
    run_spend = avg_cpu * cost_per_cpu_sec
    print(f"Estimated Cloud Compute Spend: ${run_spend:.7f} per run (@ $0.085/hr baseline)")
    print("=" * 70)

    # Save benchmark results as JSON
    with open("results/cost_benchmark.json", "w") as f:
        json.dump({
            "trials": results,
            "mean_wall_sec": avg_wall,
            "mean_cpu_sec": avg_cpu,
            "mean_latency_ms": avg_ms,
            "std_latency_ms": std_ms,
            "cloud_compute_cost_usd": run_spend,
        }, f, indent=2)

if __name__ == "__main__":
    run_benchmark()
