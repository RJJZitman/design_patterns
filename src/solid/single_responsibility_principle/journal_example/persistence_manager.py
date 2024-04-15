class PersistenceManager:
    @staticmethod
    def save_to_file(content: str, filename: str):
        with open(filename, "w") as f:
            f.write(content)
