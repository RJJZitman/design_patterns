from journal import Journal
from persistence_manager import PersistenceManager

if __name__ == "__main__":
    # make a journal
    j = Journal()
    j.add_entry("I cried today.")
    j.add_entry("I ate a bug.")
    print(f"Journal entries:\n{j}\n")

    # write the journal to a file
    file = './journal.txt'
    PersistenceManager.save_to_file(content=str(j), filename=file)

    # verify the entries by printing them to the console
    with open(file) as fh:
        print(fh.read())
