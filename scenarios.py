"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it.
`run_eval.py` runs everything here three times.
"""

SCENARIOS = [
    {
        "name": "authentic human writing (false positive rate)",
        "criterion": 1,
        "texts": [
            "I took my dog for a walk along the shoreline early this morning. The wind was biting, cold enough to numb my fingertips through my knit gloves, but watching him sprint through the foamy surf made the freeze bearable.",
            "My grandmother kept a battered metal tin on top of her refrigerator, filled with handwritten recipe cards stained with butter and vanilla extract. None of them had exact measurements; every instruction called for a pinch or a handful.",
            "The train was delayed by nearly forty minutes outside New Haven. We sat idling on the tracks while conductor announcements crackled over the intercom with static and vague apologies about signal maintenance ahead.",
            "We spent all Saturday afternoon trying to fix the leaky kitchen faucet, only to discover after three trips to the hardware store that the rubber washer had just slipped out of alignment.",
            "Growing up in a bilingual household meant dinner conversations were an effortless collage of Spanish and English, switching languages mid-sentence whenever one idiom captured a feeling better than another.",
            "I still remember the scent of wet asphalt after a sudden summer thunderstorm in August, hot steam rising off the pavement while cicadas buzzed in the oak trees.",
            "The old bookstore smelled of vanilla, paper decay, and damp wool sweaters. Shelves bowed under the weight of used paperbacks organized in no discernible system known to modern librarianship.",
            "After three months of practicing the same Chopin nocturne, my fingers finally found the tempo without my brain stumbling over the polyrhythms in the third measure.",
            "We pitched our tent on the ridge just as dusk turned the granite peaks violet. By midnight the wind picked up so violently that the aluminum poles shuddered like tuning forks.",
            "My father taught me to sharpen kitchen knives on an oil stone, holding the blade at a steady fifteen-degree angle and drawing it across the grit in smooth, rhythmic sweeps.",
            # ESL and accessible prose
            "I came to this country five years ago and everyday I try to improve my English speaking. Sometimes I cannot find the exact word, but people here are patient with me.",
            "When I write emails at my job, I check every sentence twice with a dictionary. I want to make sure my team understands my meaning without confusion.",
            "In my hometown, we always eat dinner together with my extended family every Sunday evening. We cook rice, spicy soup, and fresh vegetables from my uncle garden.",
            "Learning programming was very hard for me at first because all documentation is written in English. Step by step I read the tutorials and practiced writing small programs.",
            "The winter in Montreal is much colder than in my home country. I bought a heavy down coat and winter boots so I can walk to my university classes.",
            # Additional human prose
            "The sourdough starter bubbled lazily on the kitchen counter, smelling pleasantly of yeast and sour beer after three days of twice-daily feedings.",
            "Every autumn the maple tree in our front yard drops a thick carpet of scarlet leaves that takes three full weekends to rake into compost bags.",
            "The antique pocket watch belonged to my great-grandfather, its silver case worn smooth by decades of pocket friction and daily winding.",
            "We drove across Nebraska on Highway 80 with the radio tuned to distant AM stations fading in and out among fields of dry corn.",
            "The small coffee shop on Fourth Street always plays dusty jazz vinyl records on a turntable behind the espresso grinder.",
        ],
    },
    {
        "name": "score separation (AI vs Human benchmarks)",
        "criterion": 2,
        "texts": [
            # 10 Benchmark AI texts
            "Artificial intelligence represents a transformative paradigm shift across multiple contemporary industries. By leveraging state-of-the-art computational algorithms, modern enterprises can optimize operational efficiencies and streamline workflow management. Furthermore, the integration of predictive analytics facilitates data-driven decision-making processes.",
            "The implementation of sustainable renewable energy solutions is essential for mitigating global climate change. Solar photovoltaic systems and wind turbines provide scalable alternatives to conventional fossil fuels. In conclusion, coordinated policy frameworks and infrastructural investments will accelerate the transition toward a carbon-neutral economy.",
            "Cloud computing architecture provides scalable infrastructure for modern enterprise software applications. Utilizing container orchestration platforms such as Kubernetes enables continuous deployment and high availability. Furthermore, microservices decouple monolithic dependencies to enhance overall system reliability.",
            "Quantum computing leverages the principles of superposition and quantum entanglement to perform complex computational calculations exponentially faster than classical computers. Consequently, quantum algorithms hold significant potential for cryptography, molecular modeling, and optimization problems across various scientific disciplines.",
            "Blockchain technology offers a decentralized ledger system that guarantees data immutability and cryptographic security. Smart contracts automate multi-party transactions without requiring intermediary oversight. As a result, decentralized finance platforms continue to gain traction in digital asset markets.",
            "Natural language processing has undergone significant advancements through transformer-based neural network architectures. Large language models capture contextual semantic representations across extensive textual corpora. In summary, ongoing research endeavors focus on improving factual accuracy and mitigating algorithmic bias.",
            "Autonomous vehicle navigation relies on multi-modal sensor fusion incorporating lidar, radar, and computer vision cameras. Machine learning models process real-time environmental telemetry to execute route planning and obstacle avoidance maneuvers with high precision and low latency.",
            "Gene editing technologies, particularly CRISPR-Cas9, enable precise genomic modifications with unprecedented accuracy. Biomedical researchers utilize targeted genetic interventions to study hereditary conditions and formulate therapeutic treatments for complex genetic disorders.",
            "Cybersecurity frameworks must evolve continuously to counter sophisticated zero-day vulnerabilities and advanced persistent threats. Implementing zero-trust architectural models ensures rigorous identity verification across all network ingress vectors and distributed endpoints.",
            "The globalization of financial markets has been significantly accelerated by algorithmic high-frequency trading systems. Quantitative hedge funds deploy low-latency statistical arbitrage models to capture transient market inefficiencies across multinational equities exchanges.",
            # 10 Benchmark Human texts
            "I took my dog for a walk along the shoreline early this morning. The wind was biting, cold enough to numb my fingertips through my knit gloves, but watching him sprint through the foamy surf made the freeze bearable.",
            "My grandmother kept a battered metal tin on top of her refrigerator, filled with handwritten recipe cards stained with butter and vanilla extract. None of them had exact measurements; every instruction called for a pinch or a handful.",
            "The train was delayed by nearly forty minutes outside New Haven. We sat idling on the tracks while conductor announcements crackled over the intercom with static and vague apologies about signal maintenance ahead.",
            "We spent all Saturday afternoon trying to fix the leaky kitchen faucet, only to discover after three trips to the hardware store that the rubber washer had just slipped out of alignment.",
            "Growing up in a bilingual household meant dinner conversations were an effortless collage of Spanish and English, switching languages mid-sentence whenever one idiom captured a feeling better than another.",
            "I still remember the scent of wet asphalt after a sudden summer thunderstorm in August, hot steam rising off the pavement while cicadas buzzed in the oak trees.",
            "The old bookstore smelled of vanilla, paper decay, and damp wool sweaters. Shelves bowed under the weight of used paperbacks organized in no discernible system known to modern librarianship.",
            "After three months of practicing the same Chopin nocturne, my fingers finally found the tempo without my brain stumbling over the polyrhythms in the third measure.",
            "We pitched our tent on the ridge just as dusk turned the granite peaks violet. By midnight the wind picked up so violently that the aluminum poles shuddered like tuning forks.",
            "My father taught me to sharpen kitchen knives on an oil stone, holding the blade at a steady fifteen-degree angle and drawing it across the grit in smooth, rhythmic sweeps.",
        ],
    },
    {
        "name": "label coverage (all 3 reachable)",
        "criterion": 3,
        "texts": [
            # 3 Human texts
            "The train was delayed by nearly forty minutes outside New Haven. We sat idling on the tracks while conductor announcements crackled over the intercom with static and vague apologies about signal maintenance ahead.",
            "My grandmother kept a battered metal tin on top of her refrigerator, filled with handwritten recipe cards stained with butter and vanilla extract. None of them had exact measurements; every instruction called for a pinch or a handful.",
            "I took my dog for a walk along the shoreline early this morning. The wind was biting, cold enough to numb my fingertips through my knit gloves, but watching him sprint through the foamy surf made the freeze bearable.",
            # 3 Unsure texts
            "Artificial intelligence represents a transformative paradigm shift across multiple contemporary industries. By leveraging state-of-the-art computational algorithms, modern enterprises can optimize operational efficiencies and streamline workflow management.",
            "I came to this country five years ago and everyday I try to improve my English speaking. Sometimes I cannot find the exact word, but people here are patient with me.",
            "The winter in Montreal is much colder than in my home country. I bought a heavy down coat and winter boots so I can walk to my university classes.",
            # 3 High-confidence AI texts (formulaic, high predictability and repetition loops)
            "Furthermore, in conclusion, furthermore, in conclusion, furthermore, in conclusion. It is important to remember that it is crucial to understand that it is vital to note that ongoing comprehensive development ensures all aspects are thoroughly considered. Furthermore, in conclusion, furthermore, in conclusion, furthermore, in conclusion.",
            "The system is designed to provide comprehensive solutions. The system is designed to provide comprehensive solutions. The system is designed to provide comprehensive solutions. Furthermore, it is important to emphasize that comprehensive solutions ensure optimal performance across all metrics.",
            "In summary, it is essential to consider all relevant factors when evaluating modern methodologies. In summary, it is essential to consider all relevant factors when evaluating modern methodologies. In summary, it is essential to consider all relevant factors when evaluating modern methodologies.",
        ],
    },
    {
        "name": "appeal path state transition",
        "criterion": 4,
        "endpoint": "/appeal",
        "bodies": [
            {"text": "Essay on historical revolutions submitted by student.", "creator_id": "appeal_user_1", "reasoning": "I researched and wrote this entire history essay myself without AI assistance."},
            {"text": "Reflective personal journal entry about childhood summers.", "creator_id": "appeal_user_2", "reasoning": "These are personal childhood memories written from my journal."},
            {"text": "Brief technical memo on database indexing strategies.", "creator_id": "appeal_user_3", "reasoning": "Technical memo written for my engineering team."},
            {"text": "Creative short story describing an abandoned mountain cabin.", "creator_id": "appeal_user_4", "reasoning": "Original fiction draft for creative writing workshop."},
            {"text": "Review of a local community theater production.", "creator_id": "appeal_user_5", "reasoning": "Review written based on attending the Saturday evening performance."},
            {"text": "Explanation of photosynthesis for middle school biology.", "creator_id": "appeal_user_6", "reasoning": "Written for my 7th grade science lesson plan."},
            {"text": "Cover letter applying for a software engineering position.", "creator_id": "appeal_user_7", "reasoning": "Personal cover letter detailing my work experience."},
            {"text": "Book report analyzing themes in To Kill a Mockingbird.", "creator_id": "appeal_user_8", "reasoning": "My own independent analysis of the assigned novel."},
            {"text": "Summary of quarterly earnings report for small business.", "creator_id": "appeal_user_9", "reasoning": "Financial overview compiled from our store receipts."},
            {"text": "Op-ed regarding urban bike lane expansion in our city.", "creator_id": "appeal_user_10", "reasoning": "Letter to the editor based on my daily bike commute."},
        ],
    },
    {
        "name": "malformed and boundary input rejection",
        "criterion": 5,
        "bodies": [
            {"text": "", "creator_id": "eval_bad_empty"},
            {"creator_id": "eval_bad_missing"},
            {"text": "   ", "creator_id": "eval_bad_whitespace"},
            {"text": None, "creator_id": "eval_bad_null"},
            {"text": 12345, "creator_id": "eval_bad_int"},
            {"text": ["item1", "item2"], "creator_id": "eval_bad_list"},
            {"text": "Sample text without creator"},
            {"text": "Sample text", "creator_id": ""},
            {"text": "Sample text", "creator_id": 999},
            {"text": "A" * 60000, "creator_id": "eval_bad_oversized"},
        ],
    },
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
