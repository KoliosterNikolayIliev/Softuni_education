a = int(input())
b = int(input())

for num in range(a, b + 1):
    num = str(num)

    first_num = int(num[0])
    second_num = int(num[1])
    third_num = int(num[2])
    fourth_num = int(num[3])
    fifth_num = int(num[4])
    # sixt_num = int(num[5])
    #
    # odd_pos_sum = fifth_num + first_num + third_num
    # even_pos_sum = second_num + fourth_num + sixt_num
    # equal = odd_pos_sum == even_pos_sum
    #
    # if equal:
    #     print(num,end=' ')

    left_position_sum=first_num+second_num
    right_position_sum=fourth_num+fifth_num
    middle_num=third_num

    if left_position_sum==right_position_sum:
        print(num,end=' ')

    else:
        if left_position_sum>right_position_sum:
            right_position_sum+=middle_num

            if left_position_sum==right_position_sum:
                print(num, end=' ')

        else:
            left_position_sum+=middle_num

            if left_position_sum == right_position_sum:
                print(num, end=' ')