
class Song:
    def __init__(self, name, author, lyrics):
        self.name = name
        self.author = author
        self.lyrics = lyrics

    def __str__(self) -> str:
        return self.name+" by " + self.author

    def display_song(self) -> None:
        print(f"{self.name} by {self.author} :\n{self.lyrics}")
