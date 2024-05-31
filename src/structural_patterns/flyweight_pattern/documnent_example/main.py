from document import Document


if __name__ == "__main__":
    # Usage example
    document = Document()
    document.add_character('H', 12)
    document.add_character('e', 12)
    document.add_character('l', 12)
    document.add_character('l', 12)
    document.add_character('o', 12)
    document.add_character(' ', 12)
    document.add_character('W', 14)
    document.add_character('o', 14)
    document.add_character('r', 14)
    document.add_character('l', 14)
    document.add_character('d', 14)

    document.render()
