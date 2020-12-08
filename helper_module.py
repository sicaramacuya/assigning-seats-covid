from random import randint

def generate_id():
    """Helper function that return a eight digit random number which is going to be of type string."""
    id_number = ""
    for _ in range(10):
        id_number += str(randint(0,9))

    return id_number

def print_newline():
    """Helper function that just add a new empty line."""

    print("")