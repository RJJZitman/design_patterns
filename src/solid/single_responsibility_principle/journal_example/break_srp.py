class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def __str__(self):
        return "\n".join(self.entries)

    def add_entry(self, text: str):
        self.entries.append(f"{self.count}: {text}")
        self.count += 1

    def remove_entry(self, pos):
        del self.entries[pos]

    # break SRP by handling journal persistence in the Journal class
    def save_to_file(self, filename: str):
        with open(filename, "w") as f:
            f.write(str(self))
