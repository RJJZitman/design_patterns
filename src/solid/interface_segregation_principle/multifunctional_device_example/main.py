from interfaces import Scanner, Printer


class MyPrinter(Printer):
    def print(self, document):
        print(document)


class Photocopier(Printer, Scanner):
    def print(self, document):
        print(document)

    def scan(self, document):
        print("your document has been scanned!")


if __name__ == "__main__":
    printer = MyPrinter()
    photocopier = Photocopier()

    my_document = "Test document"

    printer.print(my_document)
    photocopier.print(my_document)
    photocopier.scan(my_document)

