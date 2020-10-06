def create_phone_number(n: list):
    result = f"({str(numbers[0])}{str(numbers[1])}{str(numbers[2])}) " \
             f"{str(numbers[3])}{str(numbers[4])}{str(numbers[5])}-" \
             f"{str(numbers[6])}{str(numbers[7])}{str(numbers[8])}{str(numbers[9])}"
    return result


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(create_phone_number(numbers))
