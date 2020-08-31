class MovieWorld:

    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        dvd = [d for d in self.dvds if d.id == dvd_id]
        customer = [c for c in self.customers if c.id == customer_id]
        if len(dvd) == 1:
            dvd = dvd[0]
            if dvd.is_rented:
                if len(customer) == 1:
                    if dvd not in customer[0].rented_dvds:
                        return "DVD is already rented"
                    return f"{customer[0].name} has already rented {dvd.name}"
            if customer[0].age < dvd.age_restriction:
                return f"{customer[0].name} should be at least {dvd.age_restriction} to rent this movie"
            customer[0].rented_dvds.append(dvd)
            dvd.is_rented = True
            return f"{customer[0].name} has successfully rented {dvd.name}"
        cust_dvd = [x for x in customer[0].rented_dvds if customer[0].rented_dvds.id == dvd_id]
        if len(cust_dvd) == 1:
            cust_dvd = cust_dvd[0]
            if cust_dvd.is_rented:
                return f"{customer[0].name} has already rented {cust_dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = [c for c in self.customers if c.id == customer_id]
        if len(customer[0].rented_dvds)>=1:
            cust_dvd = [x for x in customer[0].rented_dvds if x.id == dvd_id]
            if len(cust_dvd) == 1:
                customer[0].rented_dvds.remove(cust_dvd[0])
                dvd = [d for d in self.dvds if d.id == dvd_id][0]
                dvd.is_rented = False
                return f"{customer[0].name} has successfully returned {dvd.name}"
        return f"{customer[0].name} does not have that DVD"

    def __repr__(self):
        result = "\n".join([x.__repr__() for x in self.customers]) + "\n" + "\n".join([x.__repr__() for x in self.dvds])
        return result
