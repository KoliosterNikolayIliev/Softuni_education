from collections import defaultdict



class Library:

    def __init__(self):
        self.user_records = []
        self.books_available = []
        self.rented_books = defaultdict({})

    def add_user(self, user):
        if user in self.user_records:
            return f"User with id = {user.user_id} already registered in the library!"
        self.user_records.append(user)

    def remove_user(self, user):
        if user in self.user_records:
            self.user_records.remove(user)
        return "We could not find such user to remove!"

    def change_username(self, user_id: int, new_username: str):
        user_list = [x for x in self.user_records if x == user_id]
        if user_list:
            if user_list[0].username == new_username:
                return "Please check again the provided username - \
                it should be different than the username used so far!"
            user_list[0].username = new_username
            return f"Username successfully changed to: {new_username} for userid: {user_id}"
        return f"There is no user with id = {user_id}!"


