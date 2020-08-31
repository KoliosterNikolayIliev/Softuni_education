class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.i > len(self.sequence) - 1:
            self.number = self.number - self.i
            self.i = 0

        if self.i < self.number:
            letter = self.sequence[self.i]
            self.i += 1
            return letter

        else:
            raise StopIteration()


result = sequence_repeat('abc', 6)
for item in result:
    print(item, end='')
