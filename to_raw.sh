channelCount=0
for channel in /tmp/nurullah/*
do
	for i in $channel/*.wav
	do
		ffmpeg -y -i $i -f s16le -acodec pcm_s16le $i.raw &
	done
	wait

	cat $channel/*.raw > $channel/out.pcm
	echo $channel
	ffmpeg -f s16le -ar 44.1k -ac 1 -i $channel/out.pcm /tmp/nurullah/out_${channel##*/}.wav
	rm -rf $channel
	channelCount=$((channelCount+1))
done

if [ "$channelCount" -ne 1 ]; then
	ffmpeg -y $(for out in `seq 0 $((channelCount-1))`; do echo "-i /tmp/nurullah/out_$out.wav ";done;)-filter_complex amix=inputs=$channelCount:duration=first:dropout_transition=3 output.wav
else
	mv /tmp/nurullah/out_*.wav output.wav
fi

rm -rf /tmp/nurullah

echo $channelCount
