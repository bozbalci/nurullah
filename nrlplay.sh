#!/bin/sh

/usr/bin/env python3 $1 | xargs --max-procs 16 -L 1 xargs
wait
sh mkwav.sh
aplay output.wav
