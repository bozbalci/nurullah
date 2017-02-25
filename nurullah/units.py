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

class Track(object):
    def __init__(self, notes):
        self.notes = notes
        self.prefix = "/tmp/nurullah/0"

    def __str__(self):
        result = []

        for index, note in enumerate(self.notes):
            # Pad with zeroes
            fname = str(index).zfill(4)

            result.append('{program} {options} '
                '-i "{inp}" {prefix}/{fname}.wav'.format(
                    program="ffmpeg",
                    options="-y -f lavfi",
                    inp=note,
                    prefix=self.prefix,
                    fname=fname,
                )
            )

        return "\n".join(result)

class Song(object):
    def __init__(self, tracks):
        self.tracks = tracks

        # Enumerate the tracks
        for i, track in enumerate(self.tracks):
            track.prefix = "/tmp/nurullah/{trackno}".format(trackno=i)

    def __str__(self):
        result = []

        for i, track in enumerate(self.tracks):
            result.append("mkdir -p /tmp/nurullah/{trackno}".format(trackno=i))
            result.append(str(track))

        return "\n".join(result)
