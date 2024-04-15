class PersistenceManager:
    """
    Manages the persistence of any given content by saving it to a file.
    """
    @staticmethod
    def save_to_file(content: str, filename: str):
        """ A static method to save text to a provided file path."""
        with open(filename, "w") as f:
            f.write(content)
