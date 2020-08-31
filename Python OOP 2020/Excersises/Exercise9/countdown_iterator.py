class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.i = 0
        self.number = self.count

    def __iter__(self):
        return self

    def __next__(self):
        if self.i <= self.count:
            self.number -= 1
            self.i += 1
            return self.number+1

        else:
            raise StopIteration()


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
