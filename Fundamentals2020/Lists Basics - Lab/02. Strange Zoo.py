tail = input()
body = input()
head = input()

meerkat = [tail, body, head]
# print(meerkat[0])
# print(meerkat[1])
# print(meerkat[2])
# print(meerkat)
meerkat[0], meerkat[2] = meerkat[2], meerkat[0]
# print(meerkat[0])
# print(meerkat[1])
# print(meerkat[2])
print(meerkat)
