input_string = input()
input_counter = int(input())


def rep_str(string, n):
    output_string = ''
    for _ in range(n):
        output_string += string
    return output_string


print(rep_str(input_string, input_counter))
