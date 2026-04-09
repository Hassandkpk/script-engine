# ============================================================
# LOVECRAFT ANCHOR TAXONOMY
# Each entity has 5 real-world anchors — all visceral, all
# verifiable, all immediately dreadful with eyes closed.
# Organized so the system can track entity+anchor pairings
# and enforce genuine divergence across scripts.
# ============================================================

LOVECRAFT_ANCHORS = {

    "Cthulhu / R'lyeh / The Dreaming God": [
        {
            "anchor": "The Bloop (1997) — NOAA hydrophones recorded an ultra-low-frequency sound rising from the deep Pacific, consistent with a living organism far larger than any known species. The source was never located. The recording is available. The explanation is not.",
            "domain": "ocean_acoustics"
        },
        {
            "anchor": "REM intrusion disorder — documented neurological condition where dream content bleeds into waking consciousness. Sufferers report not waking from dreams but discovering they never left them. The EEG signature is identical to dreamless sleep.",
            "domain": "sleep_neurology"
        },
        {
            "anchor": "Thalassophobia neurological mapping — fMRI studies show the human brain has a dedicated fear response to open water depth that activates before conscious recognition. The brain identifies the threat before the mind does.",
            "domain": "depth_neurology"
        },
        {
            "anchor": "Pacific seamount sonar surveys — multiple uncharted underwater formations photographed at depth show symmetrical geometry inconsistent with volcanic or tectonic origin. No follow-up surveys have been funded.",
            "domain": "ocean_geology"
        },
        {
            "anchor": "Coastal mass stranding events — documented cases of whales and dolphins beaching simultaneously across unconnected coastlines, showing no pathogen, no toxin, no navigational explanation. The behavior precedes by hours any measurable change in ocean conditions.",
            "domain": "marine_behavior"
        },
    ],

    "Nyarlathotep / The Crawling Chaos": [
        {
            "anchor": "Mass psychogenic illness — documented outbreaks where groups of unconnected individuals develop identical symptoms, identical visions, identical behavioral changes, with no shared physical contact and no identified pathogen. Medicine classifies these. It does not explain them.",
            "domain": "psychogenic_illness"
        },
        {
            "anchor": "Extraordinary popular delusions — historical record documents entire populations simultaneously believing identical false things with no central coordination: the Dancing Plague of 1518, the Halifax Slasher, the Great Fear. The mechanism of transmission has never been identified.",
            "domain": "social_contagion"
        },
        {
            "anchor": "Infrasound at 18.98Hz — documented to cause anxiety, dread, and the sensation of a presence in the room in subjects with no knowledge of the source. The frequency is produced naturally by certain wind and weather patterns. Cathedrals were built at dimensions that resonate at this frequency.",
            "domain": "infrasound"
        },
        {
            "anchor": "Doppelganger phenomenon — documented in temporal lobe neurology as autoscopy: the clinical experience of seeing oneself from outside the body. In 8% of cases, the external self behaves differently than the subject. The neurological cause is identified. The behavioral divergence is not.",
            "domain": "autoscopy"
        },
        {
            "anchor": "Historical iconography convergence — independent civilizations with no documented contact produced functionally identical symbols, architectural ratios, and cosmological descriptions within centuries of each other. Diffusionism accounts for some. Not all.",
            "domain": "cultural_convergence"
        },
    ],

    "Azathoth / The Blind Idiot God": [
        {
            "anchor": "Cosmic microwave background radiation — the universe has a constant hum at 160.2 GHz, a relic of the first 380,000 years after the Big Bang. It is uniform. It is everywhere. It predates every structure in existence. It has never stopped.",
            "domain": "cosmic_radiation"
        },
        {
            "anchor": "Vacuum catastrophe — quantum field theory predicts the energy density of empty space should be 10^120 times larger than observed. This is the largest discrepancy between theory and measurement in physics. If the prediction were correct, reality as structured would be impossible. Nobody knows why it is not.",
            "domain": "quantum_cosmology"
        },
        {
            "anchor": "Heat death thermodynamics — the second law of thermodynamics guarantees the universe trends toward maximum entropy: a state of uniform temperature, no structure, no information, no distinction between anything and anything else. The timeline is 10^100 years. The endpoint is not in question.",
            "domain": "thermodynamics"
        },
        {
            "anchor": "Observable universe boundary — at 46 billion light years, the observable universe ends not because space ends but because light from beyond has not had time to reach us. What exists beyond this boundary is unknowable in principle, not in practice. The universe is larger than perception by an amount that cannot be calculated.",
            "domain": "cosmological_boundary"
        },
        {
            "anchor": "Nuclear chaos — radioactive decay is genuinely random at the quantum level. Not pseudorandom. Not determined by hidden variables. The moment a specific atom decays cannot be predicted, calculated, or caused. At the base of physical reality, events happen for no reason.",
            "domain": "quantum_randomness"
        },
    ],

    "Yog-Sothoth / The Key and the Gate": [
        {
            "anchor": "Quantum entanglement across time — particles in certain experimental configurations correlate with each other's future measurements before those measurements occur. The effect is real, documented, reproducible. The causal explanation requires causality to run backward.",
            "domain": "temporal_physics"
        },
        {
            "anchor": "Block universe theory — a mainstream interpretation of relativity in which past, present, and future exist simultaneously as fixed coordinates in four-dimensional spacetime. In this model, nothing happens. Everything simply is, at its location in time, permanently.",
            "domain": "temporal_ontology"
        },
        {
            "anchor": "Déjà vu neurological basis — occurs when the hippocampus files an experience as memory before the experience is complete. The brain timestamps it as past while it is still present. For a fraction of a second, you have already lived this moment.",
            "domain": "memory_neurology"
        },
        {
            "anchor": "Gravitational waves — distortions in spacetime caused by massive events propagate outward at the speed of light. The LIGO detection in 2015 recorded two black holes merging 1.3 billion years ago. The spacetime around Earth was physically compressed and stretched. Nobody felt it.",
            "domain": "gravitational_physics"
        },
        {
            "anchor": "Archaeological site dating paradoxes — multiple independent sites contain artifacts that predate the civilizations credited with producing them by thousands of years. In some cases, the material predates the existence of the required technology by an amount that rules out gradual development.",
            "domain": "archaeological_anomaly"
        },
    ],

    "The Deep Ones / Innsmouth": [
        {
            "anchor": "Coastal population genetic isolation — island and coastal communities separated for more than 800 years develop measurable physiological divergence from inland populations: altered stress hormone baselines, modified pain response thresholds, neurological differences in spatial processing. The mechanism is standard genetics. The speed is not.",
            "domain": "population_genetics"
        },
        {
            "anchor": "Human aquatic adaptations — Bajau sea nomads of Southeast Asia have spleens 50% larger than land populations, allowing longer dives. The adaptation is genetic, not developmental. It emerged in 15,000 years — evolutionarily instantaneous. The genome shows no other significant divergence.",
            "domain": "human_adaptation"
        },
        {
            "anchor": "Atavistic gene expression — dormant ancestral genes occasionally reactivate in modern humans, producing features absent for millions of years: functional tails, additional nipple rows, gill-arch remnants that do not fully close. These are documented in clinical literature. They are not classified as mutations. They are regressions.",
            "domain": "atavistic_biology"
        },
        {
            "anchor": "Ocean floor sediment memory — sediment cores from deep ocean contain complete biological records of every major extinction event in Earth's history. The organisms preserved in the deepest strata have never been matched to any surface fossil record. They existed only in the deep. They may still.",
            "domain": "deep_sediment"
        },
        {
            "anchor": "Bioluminescence signaling — deep sea organisms produce light in patterns that function as language — repeating sequences, call-and-response structures, encoded information — between species with no shared evolutionary ancestor. The communication exists. The content has not been decoded.",
            "domain": "bioluminescence"
        },
    ],

    "The Colour Out of Space": [
        {
            "anchor": "Non-visible spectrum biological response — documented cases where animals respond to UV and infrared wavelengths with behaviors identical to those produced by visible threat stimuli. The threat is undetectable to human senses. The response in co-present humans is measurable as elevated cortisol and accelerated heart rate with no identified cause.",
            "domain": "spectrum_biology"
        },
        {
            "anchor": "Radiation sickness historical documentation — the first documented cases of radiation exposure (early radium workers, 1920s) were initially classified as wasting diseases of unknown origin. The cause was invisible, odorless, tasteless. Patients described feeling watched by something inside their bodies.",
            "domain": "radiation_history"
        },
        {
            "anchor": "Soil contamination archaeology — excavated sites near certain industrial and naturally occurring chemical deposits show complete biological absence: no microbial life, no fungal growth, no decomposition. The soil looks normal. Nothing will grow in it. Nothing will die in it.",
            "domain": "soil_contamination"
        },
        {
            "anchor": "Cherenkov radiation — particles moving faster than light travels through a given medium produce blue radiation visible to the naked eye. It has no source in the conventional sense — it is the visible evidence of something moving too fast to see. It is beautiful. It is lethal at sufficient exposure.",
            "domain": "cherenkov"
        },
        {
            "anchor": "Photosensitization disorders — documented conditions where exposure to ordinary sunlight causes progressive cellular destruction. The mechanism is the light interacting with a substance already present in the body. The light did not change. The body became incompatible with it.",
            "domain": "photosensitization"
        },
    ],

    "At the Mountains of Madness / The Elder Things": [
        {
            "anchor": "Antarctic ice core biological material — cores drilled from ice sheets 800,000 years old contain viable bacterial spores that revive when thawed. The organisms are metabolically functional. Some are not matched to any known species. They have been frozen since before modern humans existed.",
            "domain": "ice_core_biology"
        },
        {
            "anchor": "Lake Vostok — a liquid freshwater lake the size of Lake Ontario, sealed beneath 4km of Antarctic ice for 15-25 million years, isolated from the surface biosphere. Drilling reached it in 2012. The water samples contained DNA sequences that matched no known organism in any database.",
            "domain": "subglacial_lake"
        },
        {
            "anchor": "Pre-Cambrian multicellular life — the Ediacaran biota (635-538 million years ago) were complex multicellular organisms with no evolutionary antecedents. They appeared fully formed in the fossil record, dominated for 100 million years, and vanished completely. No descendant has been identified.",
            "domain": "ediacaran"
        },
        {
            "anchor": "Deep rock microbial ecosystems — bacteria have been found living in solid rock 5km below the surface, in complete darkness, at temperatures above 60°C, with no connection to the surface biosphere. Their metabolism runs on geological timescales. Some individual cells are estimated to be millions of years old.",
            "domain": "deep_rock_biology"
        },
        {
            "anchor": "Antarctic mountain discovery — the Gamburtsev Mountains, a range the size of the Alps, were discovered in 1958 completely buried beneath the Antarctic ice sheet. They have never been above ice. No human has seen them. Their geological origin is contested. They should not be where they are.",
            "domain": "subglacial_geology"
        },
    ],

    "Hastur / The King in Yellow": [
        {
            "anchor": "Semantic satiation — a documented neurological phenomenon where repeating a word causes it to lose all meaning. The brain stops processing it as language. In extended cases, the subject reports the word beginning to sound like something that was never a word at all.",
            "domain": "semantic_neurology"
        },
        {
            "anchor": "Stendhal syndrome — documented acute psychological response to exposure to large concentrations of art: rapid heartbeat, dizziness, confusion, dissociation. First formally documented in 1817. The mechanism is not understood. The syndrome is not metaphorical. It is in the clinical literature.",
            "domain": "aesthetic_syndrome"
        },
        {
            "anchor": "Earworm neurology — involuntary musical imagery activates the auditory cortex identically to actually hearing the sound. The brain cannot fully distinguish between a memory of sound and its occurrence. In documented cases lasting weeks, subjects report the music changing — developing harmonics not present in the original.",
            "domain": "auditory_imagery"
        },
        {
            "anchor": "Glossolalia — documented in neurological literature as a dissociative state in which subjects produce complex vocalizations in no known language. The vocalizations have syntactic structure. They have never been decoded. Multiple independent subjects in separate countries produce statistically similar phoneme distributions.",
            "domain": "glossolalia"
        },
        {
            "anchor": "Collective obsessive ideation — documented episodes throughout history in which a specific idea spreads through a population causing identical compulsive behaviors. The Dancing Plague. The Laughing Epidemic. The suicide clusters following a single publicized death. The idea spreads like infection. The vector has never been identified.",
            "domain": "ideational_contagion"
        },
    ],

    "The Great Race of Yith / Deep Time": [
        {
            "anchor": "Genetic memory research — documented evidence that traumatic experiences alter gene expression in ways that are inherited by offspring who never experienced the trauma. Holocaust survivor descendants show measurable stress hormone dysregulation. The memory is in the body before the mind has any reason for it.",
            "domain": "epigenetic_memory"
        },
        {
            "anchor": "Chronobiology and deep time — the human circadian rhythm runs at 24.2 hours, not 24. Over evolutionary time, this drift would desynchronize the body from the day completely. Something corrects it. The correction mechanism is partially understood. The reason it drifts in the first place is not.",
            "domain": "chronobiology"
        },
        {
            "anchor": "Stratigraphic time — geologists read time in rock. A single cliff face may contain 500 million years of record. The scale is not metaphorical. The Cambrian explosion — when complex life appeared — occupies approximately 2cm of stone in a standard outcrop.",
            "domain": "deep_time_geology"
        },
        {
            "anchor": "Long-period comets — comets with orbital periods of thousands of years arrive from the Oort Cloud, a region of space so distant that most were last in the inner solar system before human civilization began. They carry material that has not been near a star in millions of years.",
            "domain": "comet_geology"
        },
        {
            "anchor": "Denisovan DNA — a separate human species identified entirely from a finger bone and two teeth found in a Siberian cave. Their full genome has been sequenced. They interbred with modern humans. Their descendants live today in Melanesia and Tibetan populations. No complete skeleton has ever been found.",
            "domain": "ancient_dna"
        },
    ],

    "Shub-Niggurath / The Black Goat": [
        {
            "anchor": "Mycelium network intelligence — fungal networks transfer nutrients, chemical signals, and electrical impulses between unconnected plants across hectares of forest. The network responds to stimuli, solves optimization problems, and remembers. It has no brain. The behavior is not metaphorical.",
            "domain": "mycelium_cognition"
        },
        {
            "anchor": "Cordyceps behavioral manipulation — parasitic fungi alter the behavior of infected insects with surgical precision, directing them to specific locations and heights before killing them to maximize spore dispersal. The manipulation targets the nervous system without destroying it. The insect continues to function until the function is no longer needed.",
            "domain": "parasitic_control"
        },
        {
            "anchor": "Reproductive drive neurology — documented neuroimaging showing that reproductive impulses activate brain regions associated with basic survival drives, bypassing prefrontal judgment systems. The mechanism is identical across mammalian species. In humans, it produces decisions inconsistent with stated values at a measurable rate.",
            "domain": "reproductive_neurology"
        },
        {
            "anchor": "Horizontal gene transfer — bacteria exchange genetic material directly, outside of reproduction. A bacterium can acquire resistance, capability, or behavior from an organism it has never reproduced with. The genome is not a fixed inheritance. It is a document that other organisms can edit.",
            "domain": "horizontal_genetics"
        },
        {
            "anchor": "Slime mold problem-solving — Physarum polycephalum, a single-celled organism with no neurons, independently recreates the Tokyo rail network, the Canadian highway system, and Roman road networks when presented with nutrient sources at city locations. It optimizes for efficiency. It has no mind with which to intend anything.",
            "domain": "slime_mold_cognition"
        },
    ],

}

# Flat list for backward compatibility with any code using ANCHORS
ANCHORS = [
    entry["anchor"]
    for entity_anchors in LOVECRAFT_ANCHORS.values()
    for entry in entity_anchors
]

# Entity names for the concept check and anchor pairing tracker
LOVECRAFT_ENTITIES = list(LOVECRAFT_ANCHORS.keys())

ANGLES = [
    "The data was collected normally. The anomaly was only noticed during archiving, years later.",
    "The measurement is accurate. What it implies cannot be true under current physics.",
    "Multiple independent sources confirmed the same reading. None of them communicated.",
    "The pattern repeats at a frequency that has no natural driver.",
    "The anomaly was documented once. All subsequent attempts to reproduce it find nothing.",
    "The researchers noted it. Then stopped noting it. The records do not explain why.",
    "It is the absence that is wrong — something that should be there and simply is not.",
    "The oldest records show it more clearly. The more modern the data, the weaker the signal.",
    "It only appears in aggregate. At the individual level, everything is normal.",
    "Three people have independently described the same response to the data: they felt watched.",
    "The anomaly resolves if you accept one assumption that no living scientist accepts.",
    "The equipment that recorded it was later decommissioned. The data was never replicated.",
    "Every dataset that contains this anomaly was collected within the same 11-year window.",
    "The anomaly grows at a rate that would be catastrophic — in approximately 900 years.",
    "There is no funding to investigate it further. No one has applied for any.",
]

POVS = [
    "Second person — the reader is inside the event as it happens",
    "First person plural — 'we' — no individual is ever identified",
    "Third person omniscient with deliberate restraint — knows everything, describes almost nothing",
    "False documentary — written as field notes or a log that stops mid-entry",
    "Nested narration — someone recounting what someone else told them, with small discrepancies",
    "No identifiable narrator — pure description of phenomena with no human anchor",
    "First person singular — a scientist writing a report that slowly stops being a report",
    "Second person plural — 'you all' — a collective addressed as a unit",
]

DISTANCES = [
    "Maximum intimacy — the reader is inside a single consciousness",
    "Forensic distance — clinical, observational, no affect",
    "Historical distance — this happened long ago and the narrator survived",
    "Dissolving distance — starts distant, collapses into immediate by the end",
    "Unreliable proximity — narrator is present but their perception is compromised",
    "Absolute removal — no narrator exists; only data and what it implies",
]

PARAS = [
    "Paragraphs compress as the script progresses — longest at top, shortest at end",
    "Alternating rhythm — long paragraph, short paragraph, throughout",
    "Single unbroken block — no paragraph breaks at all",
    "Each paragraph shorter than the previous, without exception",
    "Fragments only — no complete sentences anywhere in the script",
    "Normal prose that suddenly fragments in the final third, with no explanation",
    "Paragraphs expand — shortest at top, longest at end — pressure builds with density",
    "Two sentences per paragraph maximum, throughout — compression without fragments",
]

CONSTRAINTS = [
    "No metaphors — every image must be literal",
    "No questions — nothing in the script is posed as a question",
    "No adjectives in the final 300 words",
    "No character is ever named",
    "No time markers — no 'then', 'after', 'when', 'before'",
    "No dialogue — even quoted speech is paraphrased",
    "Every paragraph must begin with a number or a measurement",
    "The word 'dark' and all synonyms are banned",
    "No verbs of perception — seeing, hearing, feeling, sensing — banned entirely",
    "The script must end on a factual statement, not a dramatic one",
    "No sentence may exceed 15 words",
    "The word 'horror', 'fear', 'terror', 'dread' — none of these may appear",
    "Every claim must be attributable to a real source, cited inline",
    "No paragraph may repeat a noun used in the previous paragraph",
    "The opening word must be a number",
]

DEFAULT_BANS = [
    {"move": "Opening with a rhetorical question to the audience", "type": "opening"},
    {"move": "Starting with a definition or dictionary framing", "type": "opening"},
    {"move": "Second-person address in the opening line", "type": "opening"},
    {"move": "Three-part list structure anywhere in the script", "type": "structure"},
    {"move": "Ending on a question that mirrors the opening", "type": "ending"},
    {"move": "Zooming out to cosmic scale in the final paragraph", "type": "ending"},
    {"move": "Unnamed protagonist who 'notices something is wrong'", "type": "pov"},
    {"move": "Fake academic citation as an authority device", "type": "device"},
    {"move": "The phrase 'what if I told you'", "type": "device"},
    {"move": "Countdown or enumerated revelation structure", "type": "structure"},
    {"move": "Scientist discovers anomaly, ignores it, later regrets it", "type": "structure"},
    {"move": "Ending with 'we may never know the truth'", "type": "ending"},
    {"move": "Opening with atmospheric weather or environmental description", "type": "opening"},
    {"move": "A character reading a document that contains the horror", "type": "device"},
    {"move": "Flashback structure — present tense interrupted by past", "type": "structure"},
]
