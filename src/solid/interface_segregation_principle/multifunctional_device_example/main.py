from devices import MyPrinter, Photocopier


if __name__ == "__main__":
    printer = MyPrinter()
    photocopier = Photocopier()

    my_document = "Test document"

    printer.print(my_document)
    photocopier.print(my_document)
    photocopier.scan(my_document)

