def separate(lst):
    lst_neg = []
    lst_pos = []
    for i in lst:
        if i < 0:
            lst_neg.append(i)
        else:
            lst_pos.append(i)

    positive_sum = sum(lst_pos)
    negative_sum = sum(lst_neg)
    print(negative_sum)
    print(positive_sum)
    if abs(positive_sum) > abs(negative_sum):

        print("The positives are stronger than the negatives")
    else:

        print("The negatives are stronger than the positives")
    return


ll = [int(x) for x in input().split()]

separate(ll)
