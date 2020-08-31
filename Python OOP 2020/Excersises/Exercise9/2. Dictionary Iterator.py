class dictionary_iter:

    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        list = [(k, v) for k, v in self.dictionary.items()]
        if self.i <= len(list) - 1:
            result = list[self.i]
            self.i += 1
            return result
        else:
            raise StopIteration()


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
