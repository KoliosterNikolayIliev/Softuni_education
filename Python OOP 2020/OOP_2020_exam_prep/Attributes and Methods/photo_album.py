class PhotoAlbum:

    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for x in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(photos_count // 4)

    def add_photo(self, label):
        for page in self.photos:
            if len(page) < 4:
                page.append(label)
                return f"{label} photo added successfully" \
                       f" on page {self.photos.index(page) + 1}" \
                       f" slot {self.photos[self.photos.index(page)].index(label) + 1}"
        return "No more free spots"

    def display(self):
        result = f'-----------\n'
        for page in self.photos:
            if page:
                result += ''.join('[] ' for _ in range(len(page))).strip()
            result += '\n'
            result += f'-----------\n'
        return result


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())