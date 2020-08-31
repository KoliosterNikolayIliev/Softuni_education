book_name = input()
book_count = int(input())

counter = 0
book_found = False

while counter < book_count:
    book = input()
    if book == book_name:
        book_found = True
        print(f'You checked {counter} books and found it.')
        break
    counter += 1
if book_found == False:
    print('The book you search is not here!')
    print(f'You checked {book_count} books.')
