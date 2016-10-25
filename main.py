#!/usr/bin/env python3

"""
This is the Hello-World-Python program ported to Python3 and improved
by using the proper enterprise project patterns.
Originally written by kmachnicki
Disclaimer: Yes, it is a joke :)
"""

from PrinterFactory import PrinterFactory


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
