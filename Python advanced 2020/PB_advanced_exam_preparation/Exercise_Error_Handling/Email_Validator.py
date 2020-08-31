class NameTooShortError(Exception):
    """ Raised when username is 4 symbols or less"""
    pass


class MustContainAtSymbolError(Exception):
    """ Raised when @ is missing"""
    pass


class InvalidDomainError(Exception):
    """ Raised - Invalid domain"""
    pass


def validate_name(email):
    mail_split = email.split('@')
    username = mail_split[0]
    if len(username) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")


def validate_at_symbol(email):
    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")


def validate_domain(email, input_valid_domains):
    mail_split = email.split('.')
    domain = '.' + mail_split[-1]
    if domain not in input_valid_domains:
        raise InvalidDomainError(f"Domain must be one of the following: {', '.join(valid_domains)}")
    else:
        print("Email is valid")


line = input()

while line != "End":
    valid_domains = ('.com', '.net', '.bg', '.org', '.skf')

    validate_name(line)
    validate_at_symbol(line)
    validate_domain(line, valid_domains)

    line = input()
