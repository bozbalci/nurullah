from demo import istiklal

song = istiklal

for i, n in enumerate(song):
    i = str(i).zfill(4)
    print("ffmpeg -y -f lavfi -i \"" + str(n) + "\" " + str(i) + ".wav")
