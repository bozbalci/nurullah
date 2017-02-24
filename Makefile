all:
	python3 generate.py | xargs -L 1 xargs
	sh to_raw.sh

play:
	aplay out.pcm -f cd -c 1

clean:
	rm -f *.wav *.raw *.pyc *.pcm
