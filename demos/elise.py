# Für Elise

from nurullah.note import NoteSequence
from nurullah.units import Track, Song

# The beginning of the main melody
main1 = [
    ("E5", "16", 0.5),
    ("D#5", ),
    ("E5", ),
    ("D#5", ),
    ("E5", ),
    ("B4", ),
    ("D5", ),
    ("C5", ),
    ("A4", "8", ),
    ("R", ),
    ("C4", "16"),
    ("E4", ),
    ("A4", ),
    ("B4", "8"),
]

# Alternate ending one of the first melody
alt1 = [
    ("R", "16"),
    ("E4", ),
    ("G#4", ),
    ("B4", ),
    ("C5", "8"),
    ("R", "16"),
    ("E4", )
]

# Alternate ending two of the first melody
alt2 = [
    ("R", "16"),
    ("E4", ),
    ("C5", ),
    ("B4", ),
    ("A4", "4")
]

# The second melody
main2 = [
    ("R", "16", 0.5),
    ("E4", ),
    ("C5", ),
    ("B4", ),
    ("A4", "8"),
    ("R", "16"),
    ("B4", ),
    ("C5", ),
    ("D5", ),
    ("E5", "8."),
    ("G4", "16"),
    ("F5", ),
    ("E5", ),
    ("D5", "8."),
    ("F4", "16"),
    ("E5", ),
    ("D5", ),
    ("C5", "8."),
    ("E4", "16"),
    ("D5", ),
    ("C5", ),
    ("B4", "8"),
    ("R", "16"),
    ("E4", ),
    ("E5", ),
    ("R" , ),
    (),
    ("E5", ),
    ("E6", ),
    ("R" , ),
    (),
]

ns = NoteSequence()

rh_sequences = [
    main1, alt1,
    main1, alt2,
    main1, alt1,
    main1,
    main2,
    main1, alt1,
    main1, alt2,
]

rh_track = Track(sum([ns.create(seq) for seq in rh_sequences], []))
elise = Song(
    [
        rh_track,
    ]
)

print(elise)
