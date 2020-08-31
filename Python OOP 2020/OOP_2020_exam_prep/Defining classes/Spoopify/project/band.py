from project.album import Album
from project.song import Song


class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        else:
            self.albums.append(album)
            return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        album = [x for x in self.albums if x.name == album_name]
        if not album:
            return f"Album {album_name} is not found."
        album = album[0]
        if album.published:
            return "Album has been published. It cannot be removed."
        else:
            self.albums.remove(album)
            return f"Album {album_name} has been removed."

    def details(self):
        result = f"Band {self.name}\n"
        for a in self.albums:
            result += f"{a.details()}\n"
        return result



