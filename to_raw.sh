for i in *.wav
do
	ffmpeg -y -i $i -f s16le -acodec pcm_s16le $i.raw
done

cat *.raw > out.pcm
rm -f *.wav *.raw
ffmpeg -f s16le -ar 44.1k -ac 1 -i out.pcm out.wav
rm out.pcm
