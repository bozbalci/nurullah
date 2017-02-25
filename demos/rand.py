# Piano Concerto No. $(RAND)

from nurullah.note import NoteSequence
from nurullah.units import Track, Song
from nurullah.frequency import Frequency
import random

pitches = list(Frequency.keys())

rand1 = [
    pitches[i] for i in [
        random.randint(0, len(pitches) - 1) for j in range(1, 2500)
    ]
]

rand2 = [
    pitches[i] for i in [
        random.randint(0, len(pitches) - 1) for j in range(1, 2500)
    ]
]

rand3 = [
    pitches[i] for i in [
        random.randint(0, len(pitches) - 1) for j in range(1, 2500)
    ]
]

notes1 = [(pitch, "32", 0.85) for pitch in rand1]
notes2 = [(pitch, "32", 0.85) for pitch in rand2]
notes3 = [(pitch, "32", 0.85) for pitch in rand3]

ns = NoteSequence()
track1 = Track(ns.create(notes1))
track2 = Track(ns.create(notes2))
track3 = Track(ns.create(notes3))
rand = Song([track1, track2, track3])

print(rand)
