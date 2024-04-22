from interfaces import Printer, Scanner


class MyPrinter(Printer):
    """Printer implementation"""
    def print(self, document):
        print(document)


class Photocopier(Printer, Scanner):
    """Photocopier implementation"""
    def print(self, document):
        print(document)

    def scan(self, document):
        print("your document has been scanned!")