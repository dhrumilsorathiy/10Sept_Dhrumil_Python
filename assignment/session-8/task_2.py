def extract_artist(song_title):
    dash_position = song_title.index("-")
    artist = song_title[dash_position + 1:].strip()
    return artist

song = "kesariya - arijit singh"
print("aritist name:", extract_artist(song))