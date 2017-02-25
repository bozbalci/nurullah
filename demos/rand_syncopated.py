# Piano Concerto No. $(RAND)

from nurullah.note import NoteSequence
from nurullah.units import Track, Song
from nurullah.frequency import Frequency
import random

pitches = list(Frequency.keys())
lengths = ["4", "8", "16"]
dots = [".", ""]

rand = [
    pitches[i] for i in [
        random.randint(0, len(pitches) - 1) for j in range(1, 2500)
    ]
]

notes = []
for pitch in rand:
    lr = random.randint(0, len(lengths) - 1)
    dr = random.randint(0, len(dots) - 1)

    notes.append(tuple([pitch, lengths[lr] + dots[dr], 0.85]))

ns = NoteSequence()
track = Track(ns.create(notes))
rand = Song([track])
print(rand)
