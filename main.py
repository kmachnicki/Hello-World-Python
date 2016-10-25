#!/usr/bin/env python3
# This is the Hello-World-Python program ported to Python3 and improved
# by using the proper enterprise project patterns.
# Originally written by kmachnicki
# Disclaimer: Yes, it is a joke :)


# This is the heart of the program.
# This class is responsible for printing the string provided by the caller.
# It is a proxy for the print function.
class Printer:
    # __init__ is responsible for initializing the _printer member, so we can use it later.
    def __init__(self):
        self._printer = print

    # __call__ is used to print the string provided by the caller
    def __call__(self, string_to_print):
        self._printer(string_to_print)

# Since Printer is a pretty complicated class, we need a factory so we can create it easier.
class PrinterFactory:
    # create_printer is a static method of the PrinterFactory class
    # it creates a printer and returns it to the caller
    @staticmethod
    def create_printer():
        return Printer()

# main function
def main():
    # creation of the printer
    printer = PrinterFactory.create_printer()
    # string to pass to the printer
    greeting = "Hello, World!"
    # the printing happens on the next line
    printer(greeting)

if __name__ == "__main__":
    main()
