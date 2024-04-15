class Journal:
    """
    A simple class to save and retrieve journal entries.
    """
    def __init__(self):
        self.entries = []
        self.count = 0

    def __str__(self) -> str:
        """
        An EOL separated string representation of the journal.
        """
        return "\n".join(self.entries)

    def add_entry(self, text: str) -> None:
        """
        Adds an entry to the journal and updates the entry id.

        :param text: the journal entry
        """
        self.entries.append(f"{self.count}: {text}")
        self.count += 1

    def remove_entry(self, pos: int) -> None:
        """
        Permanently removes an entry from the journal based on its position.

        :param pos: id of the journal entry
        """
        del self.entries[pos]
