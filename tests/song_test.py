from app.song import Song


class TestSong:

    def test_print_song(self):
        song = Song("Hello", "Adele", "Hello....")
        assert str(song) == "Hello by Adele"
