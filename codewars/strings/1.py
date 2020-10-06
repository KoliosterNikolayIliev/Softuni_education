def song_decoder(song):
    split = song.split("WUB")
    return " ".join([x for x in split if x != ""])


song = "AWUBWUBWUBBWUBWUBWUBC"
song2 = "AWUBBWUBC"
song3 = "WUBAWUBBWUBCWUB"

print(song_decoder(song))
print(song_decoder(song2))
print(song_decoder(song3))
