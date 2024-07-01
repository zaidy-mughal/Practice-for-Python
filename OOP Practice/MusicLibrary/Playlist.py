from Song import Song
import random

class Playlist:
    """This class is used to make Playlists of Songs it means Song class is composed into it"""

    def __init__(self,playlistName,owner) -> None:
        self.playlistName = playlistName 
        self.id = random.randint(10,99)
        self.owner = owner
        self.songs = []

    def addSong(self,song):
        if song is not None:
            self.songs.append(song)
            print("Song Added Successfully\n")
        else:
            print("Song Error")


    def removeSong(self,songName):
        for song in self.songs:
            if song.title == song:
                self.songs.remove(song)
                print("Song Successfully Removed!")
        else:
            print("Song not Found!")


    def playSong(self):
        print("Playing song: 'Twinkle, Twinkle, Little Star'",
        "🎵 Twinkle, twinkle, little star 🎵",
        "Loading chorus... please wait...",
        "🎵 How I wonder what you are 🎵")

    
    def viewAllSongs(self):
        for song in self.songs:
            print(song)


    def __str__(self) -> str:
        return (f"Playlist:     {self.playlistName}\n"
                f"Owner Name:   {self.owner}\n")

