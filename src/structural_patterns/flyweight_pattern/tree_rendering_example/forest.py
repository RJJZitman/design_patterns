from typing import Dict, List
from trees import Tree, TreeType


class Forest:
    def __init__(self):
        self.trees: List[Tree] = []
        self.tree_types: Dict[str, TreeType] = {}

    def _get_or_create_tree_type(self, name: str, color: str, texture: str) -> TreeType:
        key = f'{name}_{color}_{texture}'
        if key not in self.tree_types:
            self.tree_types[key] = TreeType(name, color, texture)
        return self.tree_types[key]

    def plant_tree(self, x: int, y: int, name: str, color: str, texture: str):
        tree_type = self._get_or_create_tree_type(name, color, texture)
        tree = Tree(x, y, tree_type)
        self.trees.append(tree)

    def draw(self):
        for tree in self.trees:
            tree.draw()
