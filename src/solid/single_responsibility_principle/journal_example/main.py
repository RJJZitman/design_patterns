from journal import Journal
from persistence_manager import PersistenceManager

if __name__ == "__main__":
    # make a journal
    j = Journal()
    j.add_entry("Dear diary...")
    j.add_entry("Today was the best day ever, I ...")
    print(f"Journal entries:\n{j}\n")

    # write the journal to a file
    file = './journal.txt'
    PersistenceManager.save_to_file(content=str(j), filename=file)

    # verify the entries by printing them to the console
    with open(file) as fh:
        print(fh.read())

"""Note on the design
This example provides a very simple example in which the Single Responsibility Principle (SRP) is shown. Given the 
simplicity of the example, it could be argued to actually use the implementation in break_srp.py and seemingly reduce
the complexity of the code. Surely, we do not want a lot of additional code and files just to keep track of our personal
journal! While this may seem like a good option, it is best no to. Even though the benefits of adhering to the SRP 
might not seem worthwhile for this particular example, it still provides a intuitively logical solution for the problem 
we're facing. And not only that, it also provides us with a base from which we can easily extend our journal-keeping 
program. This prepares us for currently unknown journal-keeping functionalities required in the future and managing the 
persistence of other files without having to duplicate code from a SRP-violating Journal class. Our other option would 
be to refactor our entire program to prevent this duplication, which is a waste of time if it could have been prevented 
by simply utilising a design compliant with the srp from the beginning.

To give an example, if we were to rather save our journal some place else, we could now add a method doing just that to 
the PersistenceManager class. Not only that, but we could use the exact same functionalities to properly make notebook 
by e.g. creating a new journal instance for our notebook. Notebooks require the same saving and retrieving 
functionalities as our journal does.
"""