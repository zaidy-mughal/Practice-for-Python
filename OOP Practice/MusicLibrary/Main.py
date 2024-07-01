from Playlist import Playlist
from Song import Song


playlist = Playlist("Happy Music","Zaid")
print("\n====== Music Library ======\n")
while True:
    print("\n1. Add Song to Playlist")
    print("2. Remove Song from Playlist")
    print("3. Play Song")
    print("4. View All Songs")
    print("5. Playlist Details")
    print("6. Press Other than 1-5 to Close.")

    choice = int(input("\nEnter your choice: "))
        
    if choice == 1:
        title = input("Enter Song Title: ")
        artist = input("Enter Artist Name: ")
        duration = float(input("Enter Duration in float: "))
        song = Song(title,artist,duration)
        playlist.addSong(song)

    elif choice == 2:
        playlist.removeSong(input("Enter Song Name to Remove: "))

    elif choice == 3:
        playlist.playSong()

    elif choice == 4:
        playlist.viewAllSongs()

    elif choice == 5:
        print(playlist)

    else:
        print("Thanks for using!")
        break