base_frequencies = {
    "C": 16.35,
    "C#": 17.32,
    "Db": 17.32,
    "D": 18.35,
    "D#": 19.45,
    "Eb": 19.45,
    "E": 20.60,
    "F": 21.83,
    "F#": 23.12,
    "Gb": 23.12,
    "G": 24.50,
    "G#": 25.96,
    "Ab": 25.96,
    "A": 27.50,
    "A#": 29.14,
    "Bb": 29.14,
    "B": 30.87,
}

Freq = {}

for octave in range(0, 11):
    for pitch in base_frequencies.keys():
        notation = pitch + str(octave)
        octave_frequency = base_frequencies[pitch] * (2 ** octave)
        
        Freq[notation] = octave_frequency

Freq["R"] = 0.0
