input_string = "//this is my string!//"

startIndex = 0
count = 10
result = input_string[len(input_string[startIndex:count:1])::]
print(result)

pattern1 = r"(@|\*)([A-Z]{1}[a-z]+)\1"