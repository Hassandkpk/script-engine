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


# ============================================================
# ENTITY KNOWLEDGE BASE
# What each entity actually IS — its specific nature, horror,
# and how it contaminates real-world data.
# Injected into outline and script generators so they know
# WHO they are writing about, not just WHAT anchor to use.
# ============================================================

ENTITY_KNOWLEDGE = {

    "Cthulhu / R'lyeh / The Dreaming God": {
        "nature": (
            "Cthulhu is not a monster. It is a mind so vast that its sleep generates reality as a byproduct. "
            "It does not dream stories — it dreams geometry. R'lyeh is not a city but a thought, "
            "built in angles that do not exist in Euclidean space. "
            "The horror of Cthulhu is not that it will wake and destroy — "
            "it is that it has been asleep for longer than complex life has existed, "
            "and something that size does not notice us either way."
        ),
        "specific_horror": (
            "The listener is not in danger from Cthulhu. "
            "They are inside it. The ocean is its dreaming. "
            "Every deep water instinct, every thalassophobic response, "
            "every sound that rises from depth without explanation — "
            "these are not warnings. They are symptoms of proximity to something that does not know we exist."
        ),
        "contamination_logic": (
            "Real data connects to Cthulhu not by proving it exists "
            "but by proving that the deep ocean behaves as if something dreaming there "
            "would explain the anomaly better than anything else does. "
            "The Bloop is not Cthulhu. It is what Cthulhu's sleep sounds like from the outside."
        ),
        "narrative_arc": (
            "Start with the real data as pure anomaly. "
            "Show how the scientific explanation keeps failing. "
            "Show what the data implies if you follow it honestly. "
            "Arrive at the point where the only coherent explanation requires accepting "
            "something that cannot be named without losing the ability to name things."
        ),
    },

    "Azathoth / The Blind Idiot God": {
        "nature": (
            "Azathoth is not evil. It is not anything. "
            "It sits at the center of ultimate chaos, "
            "playing no music, dreaming no dream, making no decision. "
            "It is the ground state of existence — "
            "what reality looks like before consciousness imposes order on it. "
            "The other gods dance around it not in worship but because "
            "they cannot stop. The music that keeps them dancing "
            "is the only thing between Azathoth and full awareness of its own nature. "
            "If it ever became aware, existence would end — "
            "not destroyed, simply no longer necessary."
        ),
        "specific_horror": (
            "The horror of Azathoth is that it is already here. "
            "Quantum randomness — genuine, irreducible, causeless randomness — "
            "is Azathoth's fingerprint on physics. "
            "Every radioactive decay, every quantum event, "
            "every moment where the universe makes a choice with no reason — "
            "that is the blind idiot god, not sleeping but simply being, "
            "without awareness, without intent, without the capacity to stop. "
            "We are the dream Azathoth doesn't know it's having."
        ),
        "contamination_logic": (
            "Real data connects to Azathoth through the measurement problem, "
            "vacuum catastrophe, and irreducible quantum randomness. "
            "These are not metaphors for Azathoth — they are its actual mechanism. "
            "When physicists say 'the universe genuinely has no reason for this,' "
            "they are describing Azathoth without knowing its name."
        ),
        "narrative_arc": (
            "Begin with the specific real data — a radioactive atom, a quantum event, "
            "a moment of genuine causeless randomness. "
            "Show that science has confirmed this randomness is ontological, not epistemological. "
            "Follow that confirmation to its logical end: "
            "if the foundation of reality is causeless, then existence has no author. "
            "Then show that Lovecraft named this before physics confirmed it. "
            "End not with Azathoth as metaphor but as the most accurate description "
            "of what the universe actually is."
        ),
    },

    "Nyarlathotep / The Crawling Chaos": {
        "nature": (
            "Nyarlathotep is the only Lovecraftian entity that speaks. "
            "It is the messenger of the Outer Gods — "
            "not because they sent it, but because it goes anyway. "
            "It takes forms. It appears in history. It moves through crowds. "
            "Unlike Cthulhu or Azathoth, Nyarlathotep notices humans — "
            "and finds them interesting in the way a child finds an insect interesting, "
            "briefly, before moving on."
        ),
        "specific_horror": (
            "Nyarlathotep's horror is that it spreads. "
            "Not like a disease but like an idea. "
            "Mass psychogenic illness, collective delusion, "
            "the Dancing Plague, the Great Fear — "
            "these are what Nyarlathotep looks like from the outside. "
            "The horror is not possession but transmission: "
            "something moves through a population and leaves everyone changed "
            "in the same way, with no identified vector."
        ),
        "contamination_logic": (
            "Real data connects to Nyarlathotep through documented cases "
            "where something spread through human minds with no physical mechanism. "
            "The vector is never identified because the vector is not physical. "
            "Nyarlathotep does not need a body to move — it moves through attention."
        ),
        "narrative_arc": (
            "Begin with a specific documented case of mass psychogenic transmission. "
            "Show that science cannot explain the vector. "
            "Show that the same pattern repeats across history with no connection. "
            "Arrive at the implication that something uses human consciousness "
            "as a medium — not to destroy it but to pass through it, "
            "leaving marks, moving on."
        ),
    },

    "Yog-Sothoth / The Key and the Gate": {
        "nature": (
            "Yog-Sothoth is time made conscious. "
            "It exists at all points simultaneously — "
            "it is the gate and the key and the guardian. "
            "It does not move through time; it is coextensive with it. "
            "To Yog-Sothoth, past and future are the same thing, "
            "and causality is a local phenomenon it finds quaint."
        ),
        "specific_horror": (
            "The horror of Yog-Sothoth is that time is already fixed. "
            "Block universe theory — the mainstream physics interpretation "
            "that past, present, and future exist simultaneously as coordinates — "
            "is Yog-Sothoth's actual structure. "
            "You have already done everything you will do. "
            "The moment of your death exists right now, at its coordinate. "
            "Yog-Sothoth can see it. You are moving toward it "
            "and calling the movement choice."
        ),
        "contamination_logic": (
            "Real data connects to Yog-Sothoth through quantum retrocausality, "
            "block universe theory, and the documented cases where "
            "particles appear to respond to measurements not yet made. "
            "These are not metaphors — they are physics confirming "
            "that time does not work the way consciousness experiences it."
        ),
        "narrative_arc": (
            "Begin with a specific physics experiment where the timeline seems wrong. "
            "Show what block universe theory actually implies — "
            "not as metaphor but as the dominant interpretation of relativity. "
            "Follow it to the personal: your future is already fixed, "
            "at its coordinate in spacetime. "
            "End at the implication that something could, in principle, "
            "see all of it — and that Lovecraft called it by name."
        ),
    },

    "The Deep Ones / Innsmouth": {
        "nature": (
            "The Deep Ones are not invaders. They were here first. "
            "They represent the part of human biology that remembers the ocean — "
            "atavistic genes, ancestral memory encoded in the body, "
            "the evolutionary history that does not fully erase. "
            "Innsmouth is not a curse. It is a reversion. "
            "The horror is that the Deep One is already inside human genetics, "
            "waiting for conditions that allow expression."
        ),
        "specific_horror": (
            "The horror is biological and intimate. "
            "It is already in you. Not metaphorically — "
            "the genes that could produce gill arches exist in human embryos, "
            "briefly, before being suppressed. "
            "The Innsmouth look is not infection. It is memory. "
            "The ocean is not calling — it is reclaiming."
        ),
        "contamination_logic": (
            "Real data connects through atavistic biology, "
            "coastal genetic isolation studies, and the documented cases "
            "where ancestral genes reactivate in modern humans. "
            "The Deep Ones are not supernatural — "
            "they are what human biology looks like "
            "when the suppression mechanisms fail."
        ),
        "narrative_arc": (
            "Begin with a documented case of atavistic gene expression. "
            "Show that the suppression mechanisms are recent and fragile. "
            "Show what coastal isolation does to genetics over generations. "
            "Arrive at the implication that Innsmouth is not fiction "
            "but a description of what happens when isolation "
            "removes the evolutionary pressure to stay human."
        ),
    },

    "Hastur / The King in Yellow": {
        "nature": (
            "Hastur is an idea that destroys by being understood. "
            "The King in Yellow is not a play — it is a transmission. "
            "Reading it does not expose you to Hastur; "
            "it makes you Hastur's, because understanding the idea "
            "is the same as being changed by it. "
            "Hastur operates through aesthetics — "
            "through beauty that cannot be unseen, "
            "through meaning that restructures the mind that holds it."
        ),
        "specific_horror": (
            "The horror is cognitive and irreversible. "
            "Stendhal syndrome, semantic satiation, "
            "the earworm that develops new harmonics — "
            "these are Hastur operating at low intensity. "
            "The full contact is understanding the Yellow Sign, "
            "which cannot be described because describing it "
            "would be transmitting it."
        ),
        "contamination_logic": (
            "Real data connects through documented cases of "
            "aesthetic experience producing neurological changes, "
            "ideas spreading with no physical vector, "
            "and the specific cases where exposure to certain content "
            "produces identical responses across unconnected individuals."
        ),
        "narrative_arc": (
            "Begin with a documented case of idea-as-pathogen — "
            "a real historical instance where something spread through minds "
            "with no physical mechanism. "
            "Show the neurological evidence for aesthetic experience changing brain structure. "
            "Follow it to the implication that some ideas, "
            "if complex enough, rewrite the mind that contains them. "
            "End at the threshold: the script itself is approaching "
            "the boundary of what can be said without becoming the thing it describes."
        ),
    },

    "At the Mountains of Madness / The Elder Things": {
        "nature": (
            "The Elder Things are not villains. They are scientists. "
            "They came to Earth before complex life existed, "
            "terraformed it, created life as an experiment, "
            "and were themselves destroyed by what they made. "
            "The horror of At the Mountains of Madness is not the monsters — "
            "it is the discovery that Earth's entire history of life "
            "is someone else's failed experiment, "
            "and the experimenters are still down there, dead but preserved."
        ),
        "specific_horror": (
            "The horror is archaeological and temporal. "
            "Everything we are came from something that doesn't know we exist "
            "because it has been dead for sixty-five million years. "
            "The Antarctic ice contains biological material "
            "older than the conditions that should allow biology. "
            "The implication is not that we were created — "
            "it is that creation was incidental."
        ),
        "contamination_logic": (
            "Real data connects through Antarctic ice core biology, "
            "Lake Vostok's isolated ecosystem, "
            "the Ediacaran biota that appeared with no antecedents, "
            "and the deep rock microbes that metabolize on geological timescales. "
            "The Elder Things are not proven by this data — "
            "they are what the data implies if you follow the timeline honestly."
        ),
        "narrative_arc": (
            "Begin with the specific anomaly — biological material "
            "that should not survive, in conditions that should not support it. "
            "Show the timeline: when did complex life appear, "
            "and what does the fossil record look like just before that. "
            "Follow the implication that the Cambrian explosion "
            "looks less like evolution and more like deployment. "
            "End at the question the data keeps raising: "
            "if something made this, where did it go."
        ),
    },

    "Shub-Niggurath / The Black Goat": {
        "nature": (
            "Shub-Niggurath is fertility without consciousness. "
            "It is the drive to reproduce, to spread, to proliferate — "
            "divorced from any organism and existing as a force. "
            "Its thousand young are not children but instances: "
            "every organism that reproduces without understanding why "
            "is momentarily Shub-Niggurath expressing itself. "
            "The horror is biological and impersonal — "
            "the reproductive drive that runs through every living thing "
            "belongs to something that has never been alive."
        ),
        "specific_horror": (
            "The horror is that the drive is not yours. "
            "Mycelium networks that solve optimization problems without neurons, "
            "Cordyceps fungi that rewrite insect behavior with surgical precision, "
            "the reproductive drive that bypasses prefrontal judgment — "
            "these are Shub-Niggurath operating through biology. "
            "The organism thinks it is acting. "
            "It is being acted through."
        ),
        "contamination_logic": (
            "Real data connects through parasitic behavior modification, "
            "mycelium cognition, horizontal gene transfer, "
            "and the documented cases where reproductive imperatives "
            "override conscious decision-making in measurable ways. "
            "Shub-Niggurath is not a metaphor for nature — "
            "it is what nature looks like from the outside, "
            "as a single process running through all of it."
        ),
        "narrative_arc": (
            "Begin with a specific case of behavior modification by a non-conscious organism. "
            "Show the mechanism: how something without a brain "
            "produces behavior more sophisticated than many brains. "
            "Follow the implication across species: "
            "the same process running through fungi, insects, mammals. "
            "Arrive at the question of whether consciousness is the driver "
            "or the passenger — and what Lovecraft called the driver."
        ),
    },

    "The Great Race of Yith / Deep Time": {
        "nature": (
            "The Great Race of Yith do not travel through space — they travel through time, "
            "displacing the minds of other beings into their own bodies "
            "while they occupy the host. "
            "They are archivists of all possible futures, "
            "moving through time to document what will happen "
            "and then returning to a past that cannot be changed. "
            "The horror is that they have already been here. "
            "In every era. Documenting."
        ),
        "specific_horror": (
            "The horror is memory and deep time. "
            "Epigenetic memory — trauma encoded in genes and inherited — "
            "is the Yithian displacement leaving marks. "
            "The déjà vu that cannot be explained, "
            "the ancestral fear that has no source in personal experience, "
            "the knowledge that arrives without learning — "
            "these are the residue of minds that occupied this body's ancestors "
            "and left something behind."
        ),
        "contamination_logic": (
            "Real data connects through epigenetic inheritance, "
            "chronobiology anomalies, deep time geology, "
            "and the documented cases where organisms carry information "
            "they could not have acquired in their own lifetime. "
            "The Yithian archive is not a building — "
            "it is the genome, and we are all already in it."
        ),
        "narrative_arc": (
            "Begin with a specific case of epigenetic inheritance — "
            "a fear or response encoded in a child "
            "whose parents never experienced its source. "
            "Show the mechanism: how experience writes itself into DNA. "
            "Follow the implication through deep time: "
            "how far back does this encoding go, "
            "and whose experiences are we still carrying. "
            "End at the Yithian implication: "
            "if minds can leave marks in genetics, "
            "something with enough time could leave marks deliberately."
        ),
    },

    "The Colour Out of Space": {
        "nature": (
            "The Colour is not an entity in the conventional sense. "
            "It is a property — something that exists outside the spectrum "
            "of what matter can express or consciousness can process. "
            "It arrived in a meteorite, not because it was sent "
            "but because it was simply there, in space, "
            "and space is full of things that have no relationship to life. "
            "It did not intend to destroy the Gardner farm. "
            "It simply was, in a place where life could not survive its presence."
        ),
        "specific_horror": (
            "The horror is incompatibility. "
            "The Colour is not hostile — it is simply from somewhere "
            "where the rules are different, "
            "and matter organized into life cannot exist near it "
            "without being reorganized into something else. "
            "The well, the crops, the family — "
            "they were not attacked. They were adjacent."
        ),
        "contamination_logic": (
            "Real data connects through radiation sickness "
            "before radiation was understood, "
            "soil contamination that produces biological absence, "
            "Cherenkov radiation as visible evidence of something "
            "moving faster than light in a medium, "
            "and the documented cases of non-visible spectrum "
            "producing measurable biological responses. "
            "The Colour is what happens when physics from elsewhere "
            "encounters matter organized for here."
        ),
        "narrative_arc": (
            "Begin with a specific case of biological impossibility near a physical anomaly. "
            "Show the history of radiation sickness — "
            "what it looked like before the mechanism was known. "
            "Follow the implication: how many historical 'curses' "
            "were incompatibility events with physics not yet named. "
            "End at the question of what is still in space, "
            "simply being, with no relationship to anything that lives."
        ),
    },
}


# ============================================================
# ANCIENT STORIES ANCHOR TAXONOMY
# Each civilisation/era has 5 real verifiable anchors —
# specific archaeological facts, anomalies, or mysteries
# that are immediately graspable in the dark.
# Same structure as LOVECRAFT_ANCHORS.
# ============================================================

ANCIENT_ANCHORS = {

    "Göbekli Tepe / Pre-Agricultural Builders": [
        {
            "anchor": "Göbekli Tepe (9600 BCE) — built 6,000 years before Stonehenge, 7,000 years before the wheel. The builders had no pottery, no writing, no agriculture, no city. They quarried and erected limestone pillars weighing up to 20 tonnes using only flint tools. The site was then deliberately buried — intentionally backfilled — around 8000 BCE. No one knows why.",
            "domain": "megalithic_construction"
        },
        {
            "anchor": "Animal carvings at Göbekli Tepe include species from three separate biogeographic regions: Anatolian plateau predators, Mesopotamian valley fauna, and African savanna animals. No single hunter-gatherer group had access to all three regions. Someone assembled imagery from a much wider world than any single band could have known.",
            "domain": "iconographic_geography"
        },
        {
            "anchor": "The T-pillars at Göbekli Tepe have no confirmed functional purpose. They are too tall to support a roof. They are not aligned to solstices. The largest are 5.5 metres tall and weigh 15-20 tonnes. They were carved, erected, used for an unknown purpose, then buried with fill stone. 95% of the site remains unexcavated.",
            "domain": "megalithic_function"
        },
        {
            "anchor": "Radiocarbon dating at Göbekli Tepe shows the oldest structures are the most sophisticated — larger pillars, more refined carvings, more complex enclosures. Over time, construction became smaller and simpler. This inverts every other archaeological sequence of civilizational development. Something was being remembered, not invented.",
            "domain": "architectural_regression"
        },
        {
            "anchor": "Göbekli Tepe sits at the precise centre of a 12,000-year-old ecological boundary — the exact line separating wild einkorn wheat from other grasses. Genetic studies of domestic wheat trace its origin to this specific hillside. The sanctuary was built where agriculture would begin. Whether this was intentional, symbolic, or coincidence has not been determined.",
            "domain": "agricultural_origin"
        },
        {
            "anchor": "The T-pillars at Göbekli Tepe are carved with human arms, hands, and belts — they are anthropomorphic. They depict beings, not columns. The enclosures were built around these figures, not the other way around. Whoever gathered tens of thousands of hunter-gatherers to build this site did so in service of worshipping specific entities — entities that required 20-tonne stone bodies to properly represent.",
            "domain": "deity_representation"
        },
        {
            "anchor": "Göbekli Tepe shows the earliest known evidence of organised religion preceding organised society. Every other model of civilisational development assumes agriculture and settlement came first, then religion. Göbekli Tepe inverts this completely — the temple came first, and the settlement grew around it. Religion did not emerge from society. At Göbekli Tepe, society emerged from religion.",
            "domain": "religion_before_civilisation"
        },
        {
            "anchor": "The deliberate burial of Göbekli Tepe around 8000 BCE coincides precisely with the earliest evidence of large-scale agricultural settlement in the same region. The site was not abandoned — it was sealed. Someone with the authority to organise thousands of people decided the sanctuary should be hidden. The knowledge of what was buried, and why, did not survive in any written record.",
            "domain": "deliberate_concealment"
        },
    ],

    "The Great Pyramid / Old Kingdom Egypt": [
        {
            "anchor": "The Great Pyramid's base is level to within 2.1 centimetres across 230 metres — a precision not matched by any modern surveyed flat surface of comparable scale without laser equipment. The four cardinal alignments are accurate to within 0.067 degrees of true north, which was measurable in 2560 BCE only by tracking stellar circumpolar rotation over months or years.",
            "domain": "construction_precision"
        },
        {
            "anchor": "The Great Pyramid's King's Chamber contains a granite coffer cut from a single block of hard Aswan granite. The interior angles are accurate to 0.05mm. The granite contains traces of tool marks inconsistent with any known ancient Egyptian tool. The coffer is 1cm too wide to have been inserted after the chamber walls were built — it had to be placed during construction.",
            "domain": "granite_precision"
        },
        {
            "anchor": "The Pyramid Texts (2400 BCE) — the oldest religious writings in the world — describe a star-based afterlife navigation system with specific stellar coordinates, rising angles, and passage times for Orion's Belt and Thuban. The astronomical data is accurate. The passages in the pyramid align with these stars at the dates described. Who compiled the original star charts is not documented.",
            "domain": "astronomical_alignment"
        },
        {
            "anchor": "The Great Pyramid contains two narrow shafts rising at precise angles from the King's and Queen's Chambers. In 1993, a small robot reached a sealed door in the Queen's Chamber shaft after 63 metres. In 2011, a second robot drilled through the door and found another sealed door behind it. Neither chamber beyond has been entered. Nobody knows what is in them.",
            "domain": "unexplored_chambers"
        },
        {
            "anchor": "The internal temperature of the King's Chamber has been measured consistently at 20°C regardless of external temperature, season, or time of day. The granite walls are 2.6 metres thick. The chamber's acoustic resonance frequency is approximately 111Hz — documented to suppress activity in the prefrontal cortex and produce altered states in human subjects at sustained exposure.",
            "domain": "acoustic_chamber"
        },
        {
            "anchor": "The pharaoh in Old Kingdom Egypt was not a ruler who claimed divine favour — he was legally a god. The entire administrative, agricultural, and military apparatus of Egypt existed to serve the god-king's eternal life. Every tax, every harvest, every conscripted labourer was theologically justified as an offering. The state and the religion were not separate institutions. They were the same institution.",
            "domain": "divine_kingship"
        },
        {
            "anchor": "The Pyramid Texts reserve specific astronomical knowledge — star names, rising times, passage coordinates — exclusively for the dead pharaoh. This knowledge was not public. It was not priestly. It existed in a single copy, inside a sealed tomb, accessible to one person who was no longer alive. The deliberate restriction of astronomical knowledge to the dead king is documented but its purpose has not been explained.",
            "domain": "restricted_knowledge"
        },
        {
            "anchor": "The priesthood of Amun at Karnak accumulated land, income, and political authority over approximately 500 years until, by 1070 BCE, the High Priest of Amun controlled more agricultural land than the pharaoh. The transfer of power happened entirely through religious office — no coup, no military takeover. The god's administrators became the state's rulers while the pharaoh remained nominally divine.",
            "domain": "priestly_power_accumulation"
        },
    ],

    "Sumerian Civilisation / Mesopotamia": [
        {
            "anchor": "The Sumerian King List (2100 BCE) records kings ruling for tens of thousands of years before the Flood — one king ruled for 43,200 years. After the Flood, reigns suddenly drop to human lengths. Archaeologists classify the pre-Flood section as mythological. The post-Flood names match independently confirmed archaeological records of real rulers. The document does not change register between them.",
            "domain": "king_list_chronology"
        },
        {
            "anchor": "Cuneiform tablets from Nippur (circa 1700 BCE) describe a world map with Babylon at the centre, surrounded by ocean, with seven triangular regions beyond the ocean labelled 'distant regions' accessible only by a specific route. Two of the seven regions are described in detail. The tablet is the oldest world map. The two described regions have no confirmed correspondence to any geography.",
            "domain": "ancient_cartography"
        },
        {
            "anchor": "The Sumerians described a planet called Nibiru in astronomical tablets that do not correspond to any known planet in the inner solar system. The orbital period given is approximately 3,600 years. Modern orbital mechanics allows for undiscovered large bodies in the outer solar system — the gravitational anomalies in the Kuiper Belt remain unexplained. No Nibiru has been found. The search is ongoing.",
            "domain": "planetary_anomaly"
        },
        {
            "anchor": "The Epic of Gilgamesh (circa 2100 BCE) contains a flood narrative with specific parallels to the Genesis account: a single chosen man, a boat with specific dimensions, animals brought aboard, a bird sent out to test receding waters. The Sumerian version predates the Biblical account by at least 1,000 years. Both appear to derive from an earlier source that has not been found.",
            "domain": "flood_narrative"
        },
        {
            "anchor": "The Antikythera Mechanism (150-100 BCE) is a bronze calculating device that modelled the solar system with 37 interlocking gears accurate enough to predict solar and lunar eclipses 19 years in advance. Nothing of comparable mechanical complexity appears in the archaeological record for the next 1,400 years. The metallurgical and engineering knowledge required to produce it had no documented precedent and left no documented legacy.",
            "domain": "lost_technology"
        },
        {
            "anchor": "The Atrahasis Epic (circa 1700 BCE) states explicitly that the Anunnaki created humans — lulu amelu, 'primitive workers' — specifically to perform agricultural labour so the lesser gods would not have to. The text describes a labour strike by the Igigi gods, followed by the decision to create a substitute workforce from clay and divine blood. The justification for human existence in the oldest creation narrative on Earth is: to work so gods do not have to.",
            "domain": "creation_as_labour_control"
        },
        {
            "anchor": "In Sumerian theology, each city was owned by a specific deity — Ur belonged to Nanna, Nippur to Enlil, Eridu to Enki. The temple was not a place of worship — it was the god's household, and the city's population were the god's servants. The en-priest or entu-priestess was the god's earthly spouse. Taxes were temple offerings. Labour was divine service. The entire economic system was framed as religious obligation.",
            "domain": "temple_economy_as_control"
        },
        {
            "anchor": "The ME — divine decrees in Sumerian theology — were physical objects kept in Enki's temple at Eridu. They included kingship, priesthood, descent into the underworld, the scribal arts, truth, falsehood, fear, and weeping. Whoever held the ME held legitimate authority over those aspects of human life. The Sumerian myth of Inanna stealing the ME from Enki describes the transfer of civilisational authority as literally stealing sacred objects from a god.",
            "domain": "divine_authority_objects"
        },
        {
            "anchor": "The Anunnaki in Sumerian texts are described as a council — the Assembly of the Great Gods — who met to issue binding decrees affecting humanity: flood, famine, kingship, law. Enlil alone could convene the assembly. Decisions made in the divine assembly were then announced to humans through the king, who received them in dreams or through oracles. Human law was divine decree. The king did not make laws — he received them.",
            "domain": "divine_council_law"
        },
    ],

    "Indus Valley Civilisation / Harappa": [
        {
            "anchor": "The Indus Valley Civilisation (3300-1300 BCE) built cities with standardised brick sizes used consistently across 1.5 million square kilometres — from Afghanistan to the Arabian Sea. No palace, no temple, no structure identifiably more important than any other has been found in any major city. No royal burials. No obvious hierarchy in skeletal remains. Nobody knows who governed it.",
            "domain": "egalitarian_urbanism"
        },
        {
            "anchor": "The Indus script appears on approximately 4,000 seals and tablets, uses 400-600 distinct signs, and has been studied since 1875. It has not been deciphered. It shares no confirmed connection to any known writing system. The longest known inscription is 26 signs. Without a bilingual key, it may never be read. The language of the Indus Valley is unknown.",
            "domain": "undeciphered_script"
        },
        {
            "anchor": "Mohenjo-daro's Great Bath (2600 BCE) is a waterproofed tank of fired brick and bitumen, 12 metres long, 7 metres wide, 2.4 metres deep, fed by a well and drained by an opening in the corner. It was built to hold water for an unknown purpose — ritual bathing, water storage, cooling system. It was sophisticated enough to require municipal water engineering. Nobody knows what it was for.",
            "domain": "hydraulic_engineering"
        },
        {
            "anchor": "Skeletal remains at Mohenjo-daro show a sudden, catastrophic event — unburied bodies found in streets and houses, some with signs of violent death. The collapse of the Indus Valley Civilisation around 1900 BCE happened within approximately a century and affected every major city simultaneously. Climate change, invasion, disease, and earthquake have all been proposed. None fully accounts for the simultaneity.",
            "domain": "civilisation_collapse"
        },
        {
            "anchor": "Indus Valley seals depict a figure in a cross-legged seated posture surrounded by animals — identified by some scholars as a proto-Shiva figure, by others as a shaman or ruler. The posture is anatomically identical to later yogic and meditative positions codified in Hindu texts 1,500 years later. Whether this represents continuous cultural transmission or independent reinvention has not been resolved.",
            "domain": "iconographic_continuity"
        },
        {
            "anchor": "The Indus Valley Civilisation had no detectable warrior class, no weapons caches, no fortifications designed for military defence, and no iconography depicting conquest or rulers dominating subjects. Every other Bronze Age civilisation of comparable scale left extensive evidence of elite violence and military hierarchy. The Indus Valley left none. Either it was governed by a form of authority that did not require visible force, or the evidence of that force has not been found.",
            "domain": "non_military_authority"
        },
        {
            "anchor": "The proto-Shiva seal from Mohenjo-daro — a horned figure seated in yogic posture, surrounded by a tiger, elephant, rhinoceros, and buffalo — appears on seals distributed across the entire civilisation. The same image, unchanged, appears thousands of kilometres apart. In a civilisation with no confirmed central authority, a single religious image achieved total geographic uniformity. Something enforced that consistency.",
            "domain": "uniform_religious_iconography"
        },
    ],

    "Mycenae / Bronze Age Collapse": [
        {
            "anchor": "Around 1200 BCE, every major Bronze Age civilisation in the Eastern Mediterranean collapsed within approximately 50 years: the Mycenaean Greeks, Hittite Empire, Ugarit, Egyptian New Kingdom, Kassite Babylon. Each collapse left incomplete construction projects, unburied dead, abandoned palaces. A clay tablet from Ugarit, the last written record of that city, reads: 'There is death in the land. Our grain has been taken. The enemy ships are here.' The tablet was never sent.",
            "domain": "bronze_age_collapse"
        },
        {
            "anchor": "The Linear B tablets of Mycenae are palace administrative records — inventories of oil, grain, bronze, cloth, livestock. They record the palace economy in meticulous detail. The last tablets show increasingly frantic emergency requisitioning of military materials and food. The writing stops. Mycenae was abandoned around 1100 BCE and not reoccupied. The final tablets were preserved because the palace burned down, baking the clay.",
            "domain": "administrative_collapse"
        },
        {
            "anchor": "The Lion Gate at Mycenae (1250 BCE) uses a single lintel stone weighing approximately 20 tonnes, positioned 3 metres above ground. The corbelled ceiling stones of the Treasury of Atreus span a 14.5-metre diameter dome — the largest in the world for 1,300 years, until the Pantheon in Rome. Both were built without mortar. The Treasury of Atreus was rifled in antiquity. The bodies it contained have never been identified.",
            "domain": "megalithic_engineering"
        },
        {
            "anchor": "Homer's Iliad describes Troy as a real city with a real harbour. Until 1868, it was classified as myth. Heinrich Schliemann excavated Hisarlik in Turkey and found nine successive cities, one above the other. Troy VIIa (1300-1180 BCE) shows evidence of fire, collapsed walls, and scattered human remains consistent with violent destruction. The layer below it shows earthquake damage. Both explanations for the fall of Troy exist in the archaeological record, in adjacent strata.",
            "domain": "legendary_city"
        },
        {
            "anchor": "The Phaistos Disc (1700 BCE) is a clay disc from Crete bearing 241 symbols arranged in a spiral, stamped with 45 distinct seal types. It is unique — no other object uses the same symbols. It was found sealed in a ground-floor deposit. It is the only known example of its script. It has not been deciphered. It was manufactured with a stamp-and-repeat technique that implies the symbols were used elsewhere — on objects that have not been found.",
            "domain": "undeciphered_artefact"
        },
        {
            "anchor": "Mycenaean kings derived authority from two sources simultaneously: military conquest and divine lineage. Every major Mycenaean dynasty traced its bloodline to a god — Perseus to Zeus, Agamemnon to Tantalus, Achilles to the sea-nymph Thetis. The divine bloodline was not metaphor — it was legal title. A king without divine ancestry had no legitimate claim to rule. The gods did not bless the kings. The kings were the gods' descendants.",
            "domain": "divine_bloodline_kingship"
        },
        {
            "anchor": "The Eleusinian Mysteries — the most important religious rites in ancient Greece — were conducted in secret for approximately 2,000 years, from circa 1500 BCE to 392 CE. Initiates were forbidden on pain of death to reveal what happened inside. Participants included Plato, Cicero, Marcus Aurelius, and multiple Athenian leaders. The content of the Mysteries has never been fully reconstructed. What the most powerful men in the ancient world were shown, and sworn to silence about, is not known.",
            "domain": "secret_mystery_religion"
        },
        {
            "anchor": "The Oracle at Delphi (circa 800-390 BCE) was consulted before every major Greek military campaign, colonial expedition, and political decision for 600 years. The oracle's pronouncements were delivered in ambiguous verse by a single woman — the Pythia — seated over a geological fissure emitting ethylene gas. Modern analysis confirms the gas induces dissociative states. The geopolitical decisions of the ancient Mediterranean world were shaped by the pronouncements of a woman in an altered state of consciousness.",
            "domain": "oracle_political_control"
        },
    ],

    "Ancient Egypt / Dynastic Period": [
        {
            "anchor": "The Dendera Zodiac (50 BCE) is a bas-relief star map on the ceiling of Hathor's temple. Modern astronomical back-calculation shows it records the sky as it appeared in approximately 90,000 BCE — a date 87,000 years before the temple was built. Mainstream Egyptology classifies this as a mythological date. The astronomical data is precise enough to be accidental only at a probability of less than one in ten thousand.",
            "domain": "astronomical_dating"
        },
        {
            "anchor": "The Turin King List (1279 BCE) records Egyptian pharaohs back to 3100 BCE, then lists 'gods who ruled on earth' for 13,420 years before historical kings, followed by 'Spirits of the Dead' ruling for 11,025 years before the gods. The document was complete when found. It has since been fragmented. Historians classify the pre-dynastic section as legend. The dynastic section is accurate to the year.",
            "domain": "predynastic_record"
        },
        {
            "anchor": "The mummification process (circa 2600 BCE) required knowledge of: specific natron concentrations, the 70-day timing of Sirius's heliacal rising, the removal and separate preservation of four specific organs, and the precise wrapping sequence of linen. The earliest mummies are the best preserved. The technique was not gradually refined — it appeared in near-perfect form and then slowly degraded over centuries.",
            "domain": "embalming_knowledge"
        },
        {
            "anchor": "The Saqqara bird (circa 200 BCE) is a carved wooden object found in a tomb, classified since discovery as a votive model. In 1969, aeronautical engineer Khalil Messiha re-examined it and argued it was an aerodynamically functional scale model of a glider. The Egyptian Museum reclassified it as a toy bird. It has never been tested in a wind tunnel. No other ancient culture produced a carved bird with a horizontal tail fin.",
            "domain": "ancient_aerodynamics"
        },
        {
            "anchor": "The tomb of Seti I (1294 BCE) contains relief carvings in the Abydos temple that, at a certain angle of oblique lighting, appear to show outlines that some observers identify as a helicopter, submarine, and aircraft. Mainstream Egyptology explains these as pareidolia from palimpsest carvings — two sets of hieroglyphs superimposed. High-resolution photogrammetric analysis has not definitively resolved which explanation is correct.",
            "domain": "hieroglyphic_anomaly"
        },
        {
            "anchor": "The pharaoh in Old Kingdom Egypt was not a ruler who claimed divine favour — he was legally a god. The entire administrative, agricultural, and military apparatus of Egypt existed to serve the god-king's eternal life. Every tax, every harvest, every conscripted labourer was theologically justified as an offering. The state and the religion were not separate institutions. They were the same institution.",
            "domain": "divine_kingship"
        },
        {
            "anchor": "The Book of the Dead (circa 1550 BCE) was a commercial product — spells were manufactured by scribes and sold to families who could afford them. Wealthier families purchased more spells, more elaborate illustrations, and higher-quality papyrus. The afterlife in ancient Egypt was not equal: those who could not afford the correct spells faced a worse fate. Access to divine protection was sold by a priestly class that controlled the means of eternal life.",
            "domain": "afterlife_as_commerce"
        },
        {
            "anchor": "Akhenaten (1353-1336 BCE) abolished the entire Egyptian pantheon, closed every temple in Egypt, disbanded the priesthood of Amun, and declared a single god — the Aten — whose sole intermediary on Earth was himself. Within two decades of his death, every image of Akhenaten was destroyed, his name removed from monuments, and the old priesthood restored. The world's first recorded monotheism lasted one generation and was then systematically erased.",
            "domain": "suppressed_monotheism"
        },
        {
            "anchor": "The Hermetic texts — attributed to Hermes Trismegistus — claim to preserve the secret theology of ancient Egypt: that the cosmos is mental, that humanity contains a spark of the divine, and that this knowledge was deliberately hidden from the general population and transmitted only through initiates. Whether these texts encode genuine Egyptian temple doctrine or were composed in Alexandria around 100-300 CE remains debated. The claim that hidden theological knowledge was actively suppressed is the texts' central argument.",
            "domain": "hermetic_hidden_knowledge"
        },
    ],

    "The Maya / Mesoamerica": [
        {
            "anchor": "The Maya Long Count calendar, initiated in 3114 BCE, tracks time in units of 144,000 days. The calendar was not invented for administrative convenience — no agricultural or political cycle requires a unit of 144,000 days. The system can date events 90 million years in the past and project 90 million years forward. No civilisation has a documented need for a calendar of this precision. The Maya explanation for why they needed it has not been fully decoded.",
            "domain": "calendar_precision"
        },
        {
            "anchor": "The Dresden Codex (1200-1450 CE) contains tables calculating Venus's synodic cycle to an accuracy of one day per 6,000 years — more precise than the Gregorian calendar's solar year calculation. The tables also contain eclipse prediction intervals accurate to less than a day across centuries. The Maya had no telescopes. The mathematical system required to produce these tables was independently invented on a different continent from every other advanced mathematical system.",
            "domain": "astronomical_mathematics"
        },
        {
            "anchor": "Chichen Itza's El Castillo pyramid is oriented so that on the spring and autumn equinoxes, shadows cast by the nine terraces create the illusion of a feathered serpent descending the northern staircase. The effect lasts precisely 34 minutes. It required the builders to calculate the exact solar angle at the equinox centuries before construction began, and to align nine separate terraces to within fractions of a degree.",
            "domain": "equinox_alignment"
        },
        {
            "anchor": "The Olmec civilisation (1500-400 BCE) produced colossal basalt heads up to 3.4 metres tall and weighing 40 tonnes, transported from quarries at least 150 kilometres away without the wheel, with no documented system of river transport for the specific routes involved. The faces depicted are not Mesoamerican in feature — they show characteristics associated with West African populations. The connection has not been explained.",
            "domain": "olmec_origins"
        },
        {
            "anchor": "Palenque's sarcophagus lid (683 CE) shows the Mayan ruler Pakal at the moment of death — falling into Xibalba, the underworld. In 1952, Erich von Däniken argued the lid showed a man piloting a spacecraft. Mainstream archaeologists identify the imagery as standard Mayan cosmological iconography. The same image, reanalysed by contemporary glyph specialists, shows 11 separate identifiable mythological symbols. The two interpretations have never been reconciled in a single definitive paper.",
            "domain": "iconographic_debate"
        },
        {
            "anchor": "Maya kings were not political leaders who used religion — they were the religion. The k'uhul ajaw, 'holy lord,' was the physical embodiment of the World Tree connecting underworld to sky. His blood was divine fuel: royal bloodletting ceremonies, in which the king pierced his own tongue or genitals over sacred paper, were required to sustain cosmic order. The king did not rule by force. He ruled because without his blood, the sun would not rise.",
            "domain": "blood_as_divine_currency"
        },
        {
            "anchor": "The Popol Vuh — the Maya creation text — describes humanity being created three times and destroyed twice. The first humans were made of mud and dissolved. The second were made of wood and were destroyed because they had no memory or reverence for their creators. The third were made of maize and survived — but the gods deliberately limited their vision so they could not see as far as the gods themselves. Human consciousness was intentionally diminished at the moment of creation.",
            "domain": "intentional_human_limitation"
        },
        {
            "anchor": "Quetzalcoatl — the feathered serpent deity worshipped across Mesoamerica for over 2,000 years — was described in multiple independent traditions as a pale, bearded figure who arrived from the sea, taught astronomy, agriculture, and law, and promised to return. When Hernán Cortés arrived in 1519, the Aztec emperor Moctezuma initially received him as the returning Quetzalcoatl. A pre-existing religious prophecy facilitated the conquest of an empire of millions by 600 men.",
            "domain": "prophecy_enabling_conquest"
        },
    ],

    "Stonehenge / Megalithic Britain": [
        {
            "anchor": "Stonehenge's bluestones (circa 3000 BCE) were transported from the Preseli Hills in Wales — 250 kilometres away. Each stone weighs 2-5 tonnes. The terrain between includes the Bristol Channel. No Bronze Age transport technology has been demonstrated to be capable of moving stones this size this distance. A 2019 experiment using Bronze Age methods failed to move a single 1-tonne stone more than 100 metres without the stone cracking.",
            "domain": "megalithic_transport"
        },
        {
            "anchor": "The Avenue at Stonehenge — a 2.8-kilometre processional route aligned to the midsummer sunrise and midwinter sunset — follows an ancient glacial channel that naturally aligned to the same solar directions before the monument was built. The builders oriented the monument to a natural feature that was already there, already aligned. Whether the builders discovered the natural alignment or the alignment drew them to the site has not been determined.",
            "domain": "natural_alignment"
        },
        {
            "anchor": "Stonehenge was rebuilt three separate times over 1,500 years (3000 BCE, 2500 BCE, 1500 BCE). Each rebuilding changed the orientation slightly. The first structure was a circular earthwork. The second introduced the bluestones. The third added the sarsen trilithons. Each phase used different construction techniques by populations separated by hundreds of years. The consistent goal across all three phases — a solar calendar — was never abandoned.",
            "domain": "multi_phase_construction"
        },
        {
            "anchor": "The Aubrey Holes at Stonehenge — 56 circular pits dug around 3000 BCE — contain cremated human remains of at least 63 individuals spanning 500 years. Isotopic analysis shows individuals buried here came from as far as Scotland and continental Europe. Stonehenge was a destination — a place people travelled hundreds of kilometres to be buried. Nobody knows what made it worth that journey.",
            "domain": "cremation_archaeology"
        },
        {
            "anchor": "The acoustic properties of Stonehenge's original complete configuration (sarsen ring + inner horseshoe + bluestones) would have created a specific reverberation time of approximately 0.6 seconds and directed sound inward rather than outward. This is the acoustic signature of a space designed for enclosed group ritual, not outdoor spectacle. The acoustic properties were intentional — they required placing stones of specific heights at specific spacings.",
            "domain": "acoustic_design"
        },
        {
            "anchor": "Isotopic analysis of the Amesbury Archer — a wealthy Bronze Age man buried near Stonehenge around 2300 BCE with the richest grave goods found in Bronze Age Britain — shows he was not British. He was from the Alpine region of central Europe. He carried gold, copper knives, and flint tools of extraordinary quality. He was buried with clear ceremonial honour less than 5 kilometres from Stonehenge. Whoever controlled the monument's construction attracted powerful individuals from across the known world.",
            "domain": "monument_as_power_centre"
        },
        {
            "anchor": "The Druids — the priestly caste of pre-Roman Britain and Gaul — preserved all religious and legal knowledge exclusively through oral transmission. Writing was forbidden for sacred content. Caesar documented that Druidic training lasted up to 20 years. The Druids controlled justice, religious practice, calendar knowledge, and exemption from military service and taxation. They were the only class in Celtic society that crossed tribal boundaries freely. Information was their power — and they ensured no one else had it.",
            "domain": "oral_knowledge_monopoly"
        },
        {
            "anchor": "The Rollright Stones, Avebury, Callanish, and dozens of other megalithic sites across Britain share the same astronomical alignment principles as Stonehenge and predate the Roman conquest by over 2,000 years. They were all maintained by the same priestly tradition across generations of populations who had no writing, no centralised government, and no formal communication system. A religious knowledge system survived intact for over 2,000 years across a fragmented tribal landscape. No one recorded how.",
            "domain": "knowledge_transmission"
        },
    ],

    "Ancient Mesopotamia / Babylon": [
        {
            "anchor": "The Hanging Gardens of Babylon are the only one of the Seven Wonders of the Ancient World with no confirmed archaeological evidence. They appear in Greek and Roman accounts but not in Babylonian records — despite Babylon's meticulous administrative documentation. In 2013, Oxford scholar Stephanie Dalley proposed the Hanging Gardens were actually in Nineveh, misattributed to Babylon. No definitive site has been identified.",
            "domain": "lost_wonder"
        },
        {
            "anchor": "Babylonian astronomical tablets (circa 700 BCE) record the positions of Jupiter using a mathematical technique — plotting velocity against time on a graph to calculate distance — that was believed to have been invented in 14th-century Europe. The tablets were found in 1881. The mathematical method was not identified until 2016. The tablets were in plain sight in the British Museum for 135 years before anyone understood what they showed.",
            "domain": "mathematical_technique"
        },
        {
            "anchor": "The Etemenanki ziggurat of Babylon (600 BCE) — the probable inspiration for the Tower of Babel — was 91 metres tall with a base of 91 metres square. Herodotus reported a solid gold statue of Marduk at the top weighing 800 Babylonian talents (approximately 24 tonnes). No trace of the statue has been found. Alexander the Great ordered the ziggurat demolished for rebuilding — it was never rebuilt. The foundation plan survives. The site is now in Iraq.",
            "domain": "lost_monument"
        },
        {
            "anchor": "The Baghdad Battery (circa 250 BCE-250 CE) is a terracotta jar found near Baghdad containing a copper cylinder, an iron rod, and traces of acetic acid — the components of a simple galvanic cell capable of producing approximately 1.5 volts. Replicas produce measurable current. No contemporary text describes electrical use. The object may be a scroll storage container. The debate has not been resolved by any method that does not involve assumptions about what ancient people were capable of.",
            "domain": "ancient_technology"
        },
        {
            "anchor": "Enuma Elish (circa 1100 BCE), the Babylonian creation epic, describes the cosmos being formed from the body of the defeated chaos dragon Tiamat — her upper half becoming the sky, her lower half the earth, her eyes the sources of the Tigris and Euphrates. Modern reading of the text in light of Mesopotamian geography shows the rivers do emerge from elevations that could be metaphorically described as the locations given. The myth encodes accurate hydrology.",
            "domain": "mythological_geography"
        },
        {
            "anchor": "The Code of Hammurabi (1754 BCE) opens with a carved image of Hammurabi receiving the laws directly from the sun god Shamash. The prologue states explicitly that the gods appointed Hammurabi to make justice prevail in the land. The 282 laws that follow — regulating wages, property, marriage, debt, and punishment — are framed not as royal decree but as divine mandate. Human law in Babylon was not created by men. It was received from gods and administered by their chosen king.",
            "domain": "law_as_divine_mandate"
        },
        {
            "anchor": "The Babylonian New Year festival — the Akitu — lasted 12 days and included a ritual in which the king was stripped of his regalia, struck by the High Priest, and made to kneel before Marduk's statue to confess his sins. If he wept, his reign was confirmed. If he did not, it was taken as a sign of divine disfavour. The most powerful king in the ancient world was annually humiliated before his entire court as proof that his authority came from the god, not from himself.",
            "domain": "ritual_submission_to_deity"
        },
        {
            "anchor": "Nebuchadnezzar II (605-562 BCE) destroyed the Temple of Solomon in Jerusalem in 587 BCE, deported its priestly class to Babylon, and absorbed Judean religious scholarship into the Babylonian intellectual world. During the Babylonian captivity, Jewish scribes produced or finalised the texts that became the Torah. Multiple scholars have identified direct structural parallels between the Genesis flood account, the Exodus narrative, and earlier Babylonian religious texts. The foundational texts of three world religions were shaped during one empire's forced relocation of one people.",
            "domain": "religious_transmission_through_conquest"
        },
    ],

    "The Nazca Lines / Ancient Peru": [
        {
            "anchor": "The Nazca Lines (100 BCE-800 CE) cover 450 square kilometres of Peruvian desert. The largest figures are 370 metres long. They are only fully visible from the air — from the ground, they appear as shallow cleared paths. The figures include a spider that exactly replicates the genus Ricinulei, found only in the Amazon basin 500 kilometres away. How the Nazca obtained accurate enough imagery of this spider to replicate it at 370-metre scale on the desert floor has not been explained.",
            "domain": "geoglyph_scale"
        },
        {
            "anchor": "The Nazca lines were made by removing red iron-oxide surface stones to reveal yellow-grey ground beneath. The cleared lines have been preserved for 2,000 years by the specific microclimate of the Nazca plateau — almost zero wind, almost zero rainfall, a thermal wind layer close to the ground that deposits dust back in position. The geoglyphs were made in the only desert on Earth with these specific preservation conditions.",
            "domain": "preservation_conditions"
        },
        {
            "anchor": "Groundwater mapping beneath the Nazca plateau shows that many of the lines and spirals trace the underground path of aquifers. The spiral figures in particular follow the exact routes of sub-surface water flows. This suggests the geoglyphs may be a map of water resources — a hypothesis supported by their placement near ancient irrigation systems. The largest biomorphic figures (the hummingbird, condor, spider) do not fit this pattern.",
            "domain": "hydrological_mapping"
        },
        {
            "anchor": "Trophy heads — decapitated skulls with a hole drilled through the forehead for carrying on a cord — have been found throughout the Nazca plateau. Isotopic analysis shows the individuals were not local — they came from diverse regions across Peru. Some are male, some female, some adolescent. They span 600 years of production. The ritual purpose has been inferred but not confirmed from any contemporary written record.",
            "domain": "ritual_decapitation"
        },
        {
            "anchor": "The Nazca plateau contains geoglyphs depicting 70 plant and animal figures, 300 geometric figures, and 800 straight lines. Several of the straight lines extend for 50 kilometres without deviation, crossing hills, ravines, and irregular terrain as if the terrain did not exist. Modern survey confirms the longest lines maintain accuracy to within 0.1 degrees over their full length. The survey method used to achieve this precision has not been identified.",
            "domain": "survey_precision"
        },
        {
            "anchor": "The Inca empire — which absorbed the Nazca region — was governed through a system called mit'a: mandatory labour tribute owed to the state as a religious obligation. Every subject owed the Sapa Inca a portion of their productive time, framed not as taxation but as service to the divine. The Inca ruler was literally the Son of the Sun — Inti Coya. Refusing mit'a was not tax evasion. It was sacrilege.",
            "domain": "labour_as_religious_obligation"
        },
        {
            "anchor": "The Tiwanaku civilisation (500-1000 CE), which preceded the Inca in the Andean highlands, built the Gateway of the Sun — a single carved andesite block depicting a central figure flanked by 48 winged attendants. The figure is identified by some researchers as Viracocha, the creator god described in multiple Andean traditions as a pale bearded figure who taught civilisation, then departed across the sea promising to return. The same figure, with identical attributes, appears in Aztec, Maya, and coastal Peruvian traditions independently.",
            "domain": "cross_cultural_deity"
        },
    ],
}

ANCIENT_CIVILISATIONS = list(ANCIENT_ANCHORS.keys())


def get_entity_context(entity_name: str) -> dict:
    """
    Looks up entity knowledge by name — handles partial matches
    since protocol entity names may not exactly match keys.
    Returns entity knowledge dict or empty dict if not found.
    """
    if not entity_name:
        return {}

    # Exact match first
    if entity_name in ENTITY_KNOWLEDGE:
        return ENTITY_KNOWLEDGE[entity_name]

    # Partial match — check if entity_name appears in any key
    entity_lower = entity_name.lower()
    for key, value in ENTITY_KNOWLEDGE.items():
        if any(part.lower() in entity_lower or entity_lower in part.lower()
               for part in key.split("/")):
            return value

    return {}
