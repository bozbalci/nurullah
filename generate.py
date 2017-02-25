from demo import istiklal

song = istiklal

for channel in range(len(istiklal)):
	print("mkdir -p /tmp/nurullah/" + str(channel))
	for i, n in enumerate(song[channel]):
		i = str(i).zfill(4)
		print("ffmpeg -y -f lavfi -i \"" + str(n) + "\" /tmp/nurullah/"+str(channel)+"/" + str(i) + ".wav")
