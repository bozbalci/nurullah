# Copyright (c) 2017, Berk Ozbalci, Fatih Akca, Yagmur Oymak
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
# 
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

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

# The frequency chart.
Frequency = {
    "R": 0.0,
}

# Fill the frequency chart by calculating the octave frequencies
for octave in range(0, 11):
    for pitch in base_frequencies.keys():
        notation = pitch + str(octave)
        octave_frequency = base_frequencies[pitch] * (2 ** octave)
        
        Frequency[notation] = octave_frequency
