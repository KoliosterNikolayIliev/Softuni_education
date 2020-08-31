def age_assignment(*args, **kwargs):
    dictionary = {}
    for i in args:
        if i[0] in kwargs.keys():
            dictionary[i] = kwargs[i[0]]
    return dictionary


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
