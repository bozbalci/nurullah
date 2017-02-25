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

import re

from .frequency import Frequency


def _get_dot_multiplier(n):
    n = n + 1

    return (2 ** (1 - n)) * (-1 + (2 ** n))


def _get_seconds(duration, tempo):
    # The base duration is the first part of the string, before any
    # special notation appears.
    parts = re.split('\.|/', duration)
    result = 1.0 / int(parts[0])

    # Count the dots and multiply by duration
    dots = duration.count(".")
    if dots >= 1:
        result *= _get_dot_multiplier(dots)

    # Count the tuples. Default is two.
    try:
        ntuple = int(duration.split("/")[1])
    except IndexError:
        ntuple = 2.0
    result *= 3.0 / ntuple

    result *= 1.0 / tempo
    return result


class Note(object):

    def __init__(self, freq, duration, tempo=1):
        self.freq = freq
        self.duration = duration
        self.tempo = tempo

    def __str__(self):
        return "sine=frequency={}:duration={}".format(
            Frequency[self.freq], str(_get_seconds(self.duration, self.tempo)))
