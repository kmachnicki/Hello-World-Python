"""
This is the heart of the program.
This class is responsible for printing the string provided by the caller.
It is a proxy for the print function.
"""


class Printer:
    # __init__
    def __init__(self):
        pass

    # __call__ is used to print the string provided by the caller
    def __call__(self, string_to_print):
        print(string_to_print)

