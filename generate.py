from demo import istiklal

song = istiklal

for track in range(len(istiklal)):
	print("mkdir -p /tmp/nurullah/" + str(track))
	for i, n in enumerate(song[track]):
		i = str(i).zfill(4)
		print("ffmpeg -y -f lavfi -i \"" + str(n) + "\" /tmp/nurullah/"+str(track)+"/" + str(i) + ".wav")
