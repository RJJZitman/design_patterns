from person import Person
from research import Research
from relationships import Relationships


if __name__ == "__main__":
    parent = Person('John')
    child1 = Person('Chris')
    child2 = Person('Matt')

    # low-level module
    relationships = Relationships()
    relationships.add_parent_and_child(parent, child1)
    relationships.add_parent_and_child(parent, child2)

    research = Research(browser=relationships)
    research.find_children_of(parent=parent.name)
