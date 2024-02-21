from typing import Optional

from app.database_manager import DatabaseManger
from app.song import Song


class Library:

    def __init__(self):
        self.db = DatabaseManger()

    def add_song(self, name: Optional[str] = None, author:Optional[str] = None, song:Optional[Song] = None)->bool:
        if name is not None and author is not None:
            return self.db.add_song(name, author)
        if song is not None:
            return self.db.add_song(song.name, song.author)
        else:
            return False

    def remove_song(self, name:str, author:str) -> bool:
        return self.db.delete_song_by_name_and_author(name, author)

    def get_song_id(self, name:str, author:str) -> Optional[int]:
        return self.db.get_song_id(name, author)

    def find_song(self, name:str, author:str) -> Optional[Song]:
        if self.db.song_exists(name, author):
            return Song(name, author)
        return None

    