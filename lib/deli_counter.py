katz_deli = []


def line():
    if len(katz_deli) == 0:
        print("The line is currently empty.")


def take_a_number(katz_deli, customer):
    """
    accepts two arguments: list(katz_deli) and str of person joining the end of line
    prints out the person's name and position in line
    """
    katz_deli.append(-1, customer)
    return f"Welcome, {customer}. You are number {katz_deli.index(customer)} in line"
