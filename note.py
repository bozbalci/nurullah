from freq import Freq
import re


def get_dot_multiplier(n):
    n = n + 1

    return (2 ** (1 - n)) * (-1 + (2 ** n))


def get_seconds(duration, tempo):
    # The base duration is the first part of the string, before any
    # special notation appears.
    parts = re.split('\.|/', duration)
    result = 1.0 / int(parts[0])

    # Count the dots and multiply by duration
    dots = duration.count(".")
    if dots >= 1:
        result *= get_dot_multiplier(dots)

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
            Freq[self.freq], str(get_seconds(self.duration, self.tempo)))
