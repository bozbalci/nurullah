demo:
	/usr/bin/env python3 demos/istiklal.py | xargs --max-procs 16 -L 1 xargs
	wait
	sh mkwav.sh
	aplay output.wav

clean:
	rm -rf /tmp/nurullah *.wav *.pyc *.pcm __pycache__
