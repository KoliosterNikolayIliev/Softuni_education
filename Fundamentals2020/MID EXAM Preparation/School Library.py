books = input().split("&")
Done = False

while not Done:
    command = input().split(" | ")
    cmd = command[0]
    if cmd == "Add Book":
        book = command[1]
        if book not in books:
            books.insert(0, book)

    elif cmd == "Take Book":
        book = command[1]
        if book in books:
            books.remove(book)

    elif cmd == "Swap Books":
        book1 = command[1]
        book2 = command[2]
        if book1 in books and book2 in books:
            book1, book2 = books.index(book1), books.index(book2)
            books[book1], books[book2] = books[book2], books[book1]

    elif cmd == "Insert Book":
        book = command[1]
        books.append(book)
    elif cmd == "Check Book":
        index = int(command[1])
        if 0 <= index < len(books):
            print(books[index])
    elif cmd == "Done":
        Done = True
print(', '.join(books))
