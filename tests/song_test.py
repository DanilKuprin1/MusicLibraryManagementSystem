from app.song import Song


class TestSong:

    def test_print_song(self):
        song = Song("Hello", "Adele")
        assert str(song) == "Hello by Adele"

    