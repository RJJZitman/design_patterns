from abc import ABCMeta
from collections.abc import Iterable


class Connectable(Iterable):#, metaclass=ABCMeta):
    def connect_to(self, other):
        if self == other:
            return

        for s in self:
            for o in other:
                s.outputs.append(o)
                o.inputs.append(s)