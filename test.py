from unittest import TestCase
from unittest.mock import patch
import Printer
import PrinterFactory


class TestPrinter(TestCase):
    def setUp(self):
        self.printer = Printer.Printer()

    @patch('Printer.print', create=True)
    def test_hello(self, print_):
        phrase_to_print = "Hello"
        self.printer(phrase_to_print)
        print_.assert_called_with(phrase_to_print)

    @patch('Printer.print', create=True)
    def test_hello(self, print_):
        phrase_to_print = "World"
        self.printer(phrase_to_print)
        print_.assert_called_with(phrase_to_print)

    @patch('Printer.print', create=True)
    def test_hello(self, print_):
        phrase_to_print = "Hello World!"
        self.printer(phrase_to_print)
        print_.assert_called_with(phrase_to_print)


class TestPrinterFactory(TestCase):
    def test_create_printer(self):
        printer = PrinterFactory.PrinterFactory.create_printer()
        self.assertIsNotNone(printer)
        self.assertIsInstance(printer, Printer.Printer)

if __name__ == '__main__':
    unittest.main()
