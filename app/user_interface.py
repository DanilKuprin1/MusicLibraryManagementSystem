from typing import Optional

from app.library import Library
from app.song import Song



class UserInterface():
    def __init__(self, library: Library):
        self.library = library

    def run_interface(self) -> None:
        interface_running:bool = True
        print("\n\nHello there! This is a super Music Library!")
        while(interface_running):
            print("\nWhat would you want to do?\n"+
                  "1: Find song in the library\n" + 
                  "2: Add song to the library \n"+
                  "3: Remove song from the library\n"+
                #   "4: Display all songs in the library\n"+
                  "If you want to exit just type: exit\n"+
                  "Your choice: ", end='')
            value_str: str = input()
            if value_str == "exit":
                print("\nThank you for using super Music Library!\n")
                break
            if value_str.isdigit():
                value_int: int = int(value_str)
                if value_int < 4 and value_int > 0:
                    if value_int == 1:
                        self.find_song_choice()
                    elif value_int == 2:
                        self.add_song_choice()
                    else:
                        self.remove_song_choice()
                    continue
            print("Incorrect input!\n\n")
                

    def find_song_choice(self) -> None:
        print("\nWhat is song name?: ", end='')
        song_name: str = input()
        print("Who is song's author?: ", end='')
        song_author: str = input()
        song: Optional[Song] = self.library.find_song(song_name, song_author)
        if song is not None:
            print(f"Here is: {song}\n\n")
        else:
            print("The song is not in out library. Go ahead and add it!\n\n")
        
            
    def add_song_choice(self) -> None:
        print("What is the name of the song you want to add?: ", end='')
        name: str = input()
        print("What is the author of the song?: ",end='')
        author:str = input()
        song = Song(name, author)
        if self.library.add_song(song=song):
            print(f"You sucessfully added {song}")
        else:
            print(f"Uups somehting went wrong when adding {song}")


    def remove_song_choice(self) -> None:
        pass
            