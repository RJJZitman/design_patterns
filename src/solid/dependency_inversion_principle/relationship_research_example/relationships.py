from enum import Enum
from abc import ABCMeta, abstractmethod


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class RelationshipBrowser(metaclass=ABCMeta):
    @abstractmethod
    def find_all_children_of(self, name):
        pass


class Relationships(RelationshipBrowser):  # Low-level
    relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.PARENT, parent))

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name
