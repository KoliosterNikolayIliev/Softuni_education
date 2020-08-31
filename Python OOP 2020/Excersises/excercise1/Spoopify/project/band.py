from project.song import Song
from project.album import Album


class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        albums_list = [a for a in self.albums if a.name == album_name]
        if albums_list:
            album = albums_list[0]
            if album.published:
                return "Album has been published. It cannot be removed."
            self.albums.remove(album)
            return f"Album {album.name} has been removed."
        return f"Album {album_name} is not found."

    def details(self):
        result = f"Band {self.name}\n"
        for album in self.albums:
            result += f"{album.details()}\n"
        return result


# import unittest
#
#
# class SongTest(unittest.TestCase):
#     def test_remove_song_working(self):
#         album = Album("The Sound of Perseverance")
#         song = Song("Scavenger of Human Sorrow", 6.56, False)
#         album.add_song(song)
#         message = album.remove_song("Scavenger of Human Sorrow")
#         expected = "Removed song Scavenger of Human Sorrow from album The Sound of Perseverance."
#         self.assertEqual(message, expected)
#
#     def test_init(self):
#         song = Song("A", 3.15, False)
#         message = song.get_info()
#         expected = "A - 3.15"
#         self.assertEqual(message, expected)
#
#
# if __name__ == '__main__':
#     unittest.main()
