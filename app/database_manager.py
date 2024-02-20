import sqlite3
from typing import Optional

class DatabaseManger:
    def __init__(self):
        try:
            self.connection = sqlite3.connect("music_library.db")
            self.cursor = self.connection.cursor()
        except Exception as e:
            print(e)
            raise RuntimeError("Couldn't connect to database") from e
        
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.cursor.close()
            self.connection.close()
        if exc_type is not None:
            print(f"{exc_type}: {exc_val}; in the DatabaseContextManager")


    def close(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()

    def add_song(self, name: str, author: str) -> bool:
        try:
            self.cursor.execute(
            "INSERT INTO songs (name, author) VALUES (?, ?)",
            (name, author)
            )
            self.connection.commit()
        except sqlite3.OperationalError as e:
            print(e)
            return False
        except sqlite3.Error as e:
            print(e)
            return False
        return True

    def get_song_id(self, name: str, author: str) -> Optional[int]:
        try:
            self.cursor.execute("SELECT songs.id FROM songs WHERE name = ? AND author = ?", (name, author))
        except sqlite3.OperationalError as e:
            print(e)
            return None
        except sqlite3.Error as e:
            print(e)
            return None
        str_id = self.cursor.fetchone()
        print(str_id)
        return 1

    
    def delete_song(self, song_id: int):
        try:
            number_of_rows_before_deletion = self.cursor.rowcount
            self.cursor.execute("DELETE FROM songs WHERE id = ?", (song_id,))
            self.connection.commit()
        except sqlite3.OperationalError as e:
            print(e)
            return False
        except sqlite3.Error as e:
            print(e)
            return False
        if self.cursor.rowcount == number_of_rows_before_deletion:
            return False
        return True

        
