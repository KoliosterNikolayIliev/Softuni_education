import calendar


class DVD:

    def __init__(self, name, id, creation_year, creation_month, age_restriction):
        self.name = name
        self.id = id
        self.creation_month = creation_month
        self.creation_year = creation_year
        self.age_restriction = age_restriction
        self.is_rented = False

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction " \
               f"{self.age_restriction}. Status: {'rented' if self.is_rented else 'not rented'}"

    @classmethod
    def from_date(cls, id, name, date, age_restriction):
        date = date.split('.')
        creation_month = calendar.month_name[int(date[1])]
        creation_year = int(date[2])
        return cls(name, id, creation_year, creation_month, age_restriction)
