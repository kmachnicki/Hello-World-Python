from Printer import Printer


# Since Printer is a pretty complicated class, we need a factory so we can create it easier.
class PrinterFactory:
    # create_printer is a static method of the PrinterFactory class
    # it creates a printer and returns it to the caller
    @staticmethod
    def create_printer():
        return Printer()