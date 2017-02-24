all:
	/usr/bin/env python3 generate.py | xargs -L 1 xargs
	sh to_raw.sh

play:
	aplay out.wav

clean:
	rm -f *.wav *.raw *.pyc *.pcm
