all:
	python3 generate.py | sh
	sh to_raw.sh
	rm -f *.wav *.raw

play:
	aplay out.pcm -f cd -c 1

clean:
	rm -f *.wav *.raw *.pyc *.pcm
