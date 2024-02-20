
class Song:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def __str__(self) -> str:
        return self.name+" by " + self.author

    def display_song(self) -> None:
        print(f"{self.name} by {self.author}")
