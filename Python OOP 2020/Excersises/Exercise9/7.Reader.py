def read_next(*args):
    for i in args:
        # if args.index(i) % 2 == 0:
            if isinstance(i, dict):
                x = ""
                for j in i.keys():
                    x += j
                i = x
            for z in i:
                yield str(z)
        # else:
        #     if isinstance(i, dict):
        #         x = ""
        #         for j in i.keys():
        #             x += j
        #         i = x
        #     yield str(i[0])


for item in read_next('string', 'kur', {'d': 1, 'i': 2, 'c': 3, 't': 4}):
    print(item, end='')


# # test zero
# import unittest
#
# class Tests(unittest.TestCase):
#     def test_zero(self):
#         res = ''
#         for item in read_next('string', (2,), {'d': 1, 'i': 2, 'c': 3, 't': 4}):
#             res += item
#         self.assertEqual(res, 'string2dict')
#
# if __name__ == '__main__':
#     unittest.main()
