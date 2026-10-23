
def add_song(song_name, playlist):
    playlist.append(song_name)
    print(f"Successfully Added {song_name} in your playlist.")
    return playlist

def remove_song(song_name, playlist):
    playlist.remove(song_name)
    print(f"Successfully Removed {song_name} in your playlist.")
    return playlist 
def display_playlist(playlist):
    idx = 1
    for song in playlist:
        print(idx ," ",song)
        idx+=1