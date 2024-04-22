from enum import Enum
from abc import ABCMeta, abstractmethod


class Relationship(Enum):
    """Enum to define the possible relationships"""
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class RelationshipBrowser(metaclass=ABCMeta):
    """Interface for relationship browsers"""
    @abstractmethod
    def find_all_children_of(self, name: str):
        pass


class Relationships(RelationshipBrowser):
    """Enables finding of relationships"""
    relations = []

    def add_parent_and_child(self, parent: str, child: str):
        """Enables construction of the family tree"""
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.PARENT, parent))

    def find_all_children_of(self, name: str):
        """Finds all children of parent by name"""
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name
