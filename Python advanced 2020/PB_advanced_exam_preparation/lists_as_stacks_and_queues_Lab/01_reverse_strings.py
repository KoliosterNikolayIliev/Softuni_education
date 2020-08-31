def reverse_string(string):
    reversed_string = ''
    input_str = [x for x in string]
    while input_str:
        item = input_str.pop()
        reversed_string += item
    print(reversed_string)


reverse_string(input())
