class Email:
    pass


# lazy initialized singleton, will import email instead
email = None


def initialize_email():
    """
    module level variable. without global, Python is going to create a new local variable
    and discarded when the method exists
    """
    global email
    email = Email()
