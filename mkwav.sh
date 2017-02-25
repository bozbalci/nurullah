# Copyright (c) 2017, Berk Ozbalci, Fatih Akca, Yagmur Oymak
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
# 
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

count=0

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
	count=$((count+1))
done

if [ "$count" -ne 1 ]
then
    ffmpeg -y $(
        for out in `seq 0 $((count -1))`
        do
            echo "-i /tmp/nurullah/out_$out.wav"
        done
    ) -filter_complex amix=inputs=$count:duration=first:dropout_transition=3 output.wav
else
    mv /tmp/nurullah/out_*.wav output.wav
fi

rm -rf /tmp/nurullah
