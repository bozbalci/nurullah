for i in *.wav
do
	ffmpeg -y -i $i -f s16le -acodec pcm_s16le $i.raw
done

cat *.raw > out.pcm
