a = int(input())
b = int(input())
c = int(input())
d = int(input())

for top_left in range(a, b + 1):
    for top_right in range(a, b + 1):
        for bottom_left in range(c, d + 1):
            for bottom_right in range(c, d + 1):
                first_diagonal = top_left + bottom_right
                second_diagonal = top_right + bottom_left

                diagoal_equal = first_diagonal == second_diagonal

                top_numbers_different = top_right != top_left
                bottom_numbers_different = bottom_left != bottom_right

                if diagoal_equal and top_numbers_different and bottom_numbers_different:
                    print(f'{top_left}{top_right}\n{bottom_left}{bottom_right}')
                    print()
