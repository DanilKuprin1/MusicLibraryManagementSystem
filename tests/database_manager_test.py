from app.database_manager import DatabaseManger

class TestDatabaseManager:

    def setup_method(self):
        self.db_manager = DatabaseManger()
        self.test_song = "test_song"
        self.test_author = "test_author"
    
    def test_add_song(self):
        assert self.db_manager.add_song(self.test_song, self.test_author)

    def test_delete_song(self):
        song_id = self.db_manager.get_song_id(self.test_song, self.test_author)
        print(song_id)
        if song_id is not None:
            assert self.db_manager.delete_song(song_id)
            return 
        raise RuntimeError("song_id is None after get_song_id()")