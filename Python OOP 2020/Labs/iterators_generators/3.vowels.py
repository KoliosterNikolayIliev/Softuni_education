class vowels:
    def __init__(self, string):
        self.string = string
        self.i = 0
        self.vowels = "AaEeIiOoUuWwYy"

    def __iter__(self):
        return self

    def __next__(self):
        vowels = [x for x in self.string if x in self.vowels]
        if self.i <= len(vowels) - 1:
            letter = vowels[self.i]
            self.i += 1
            return letter

        else:
            raise StopIteration()


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
