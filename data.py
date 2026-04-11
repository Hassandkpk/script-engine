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
