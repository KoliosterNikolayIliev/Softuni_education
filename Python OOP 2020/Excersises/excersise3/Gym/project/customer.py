class Customer:
    auto_incr_id = 1

    def __init__(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email
        self.id = Customer.auto_incr_id
        Customer.auto_incr_id += 1

    @staticmethod
    def get_next_id():
        return Customer.auto_incr_id

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; " \
               f"Address: {self.address}; Email: {self.email}"
