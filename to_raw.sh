trackCount=0
for track in /tmp/nurullah/*
do
	for i in $track/*.wav
	do
		ffmpeg -y -i $i -f s16le -acodec pcm_s16le $i.raw &
	done
	wait

	cat $track/*.raw > $track/out.pcm
	echo $track
	ffmpeg -f s16le -ar 44.1k -ac 1 -i $track/out.pcm /tmp/nurullah/out_${track##*/}.wav
	rm -rf $track
	trackCount=$((trackCount+1))
done

if [ "$trackCount" -ne 1 ]; then
	ffmpeg -y $(for out in `seq 0 $((trackCount-1))`; do echo "-i /tmp/nurullah/out_$out.wav ";done;)-filter_complex amix=inputs=$trackCount:duration=first:dropout_transition=3 output.wav
else
	mv /tmp/nurullah/out_*.wav output.wav
fi

rm -rf /tmp/nurullah
