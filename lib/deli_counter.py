# katz_deli = []


# def take_a_number(katz_deli, customer):
#     """
#     accepts two arguments: list(katz_deli) and str of person joining the end of line
#     prints out the person's name and position in line
#     """
#     katz_deli.append(customer)
#     customer_position = katz_deli.index(customer) + 1
#     print(f"Welcome, {customer}. You are number {customer_position} in line.")
#     return katz_deli


# customer_queue = take_a_number(katz_deli, "Ada")


# def now_serving(customer_queue):
#     """
#     Calls out the next person in line & removes them from the front.

#     Args:
#         customer_queue (list): LIst of customers in line.
#     Returns:
#         str: Message indicating the customer being served.
#     """
#     if len(customer_queue) == 0:
#         return "There is nobody waiting to be served!"
#     served_customer = customer_queue.pop(0)  # Remove the first customer in line after being served
#     return f"Currently serving {served_customer}.\n"


# def line(katz_deli):
#     """
#     Displays the current line of customers.
#     Args:
#         katz_deli (list): List of customers in line.
#     Returns:
#         str: Formatted message of customers in line.
#     """

#     if len(katz_deli) == 0:
#         return "The line is currently empty."

#     formatted_line = ", ".join([f"{index + 1}.{customer}" for index, customer in enumerate(katz_deli)])
#     return f"The line is currently: {formatted_line}."


def take_a_number(katz_deli, customer):
    """
    Adds a customer to the end of the line and returns the updated queue.

    Args:
        katz_deli (list): List of customers in line.
        customer (str): Name of the customer to be added.

    Returns:
        list: Updated list of customers in line.
    """
    katz_deli.append(customer)
    customer_position = len(katz_deli)
    print(f"Welcome, {customer}. You are number {customer_position} in line.")
    return katz_deli


def now_serving(customer_queue):
    """
    Serves the first customer in line, removes them from the queue, and returns a message.

    Args:
        customer_queue (list): List of customers in line.

    Returns:
        str: Message indicating the customer being served.
    """
    if not customer_queue:
        return "There is nobody waiting to be served!"
    served_customer = customer_queue.pop(0)
    return f"Currently serving {served_customer}."


def line(katz_deli):
    """
    Displays the current line of customers.

    Args:
        katz_deli (list): List of customers in line.

    Returns:
        str: Formatted message of customers in line.
    """
    if not katz_deli:
        return "The line is currently empty."
    formatted_line = ", ".join([f"{index + 1}. {customer}" for index, customer in enumerate(katz_deli)])
    return f"The line is currently: {formatted_line}"
