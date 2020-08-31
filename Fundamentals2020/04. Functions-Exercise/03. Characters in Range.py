chr1 = input()
chr2 = input()


def ascii_char(chr1, chr2):
    for i in range(ord(chr1)+1, ord(chr2)):
        print(chr(i), end=' ')


ascii_char(chr1, chr2)
