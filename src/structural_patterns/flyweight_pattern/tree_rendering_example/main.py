from forest import Forest


if __name__ == "__main__":
    forest = Forest()
    forest.plant_tree(1, 1, 'Oak', 'Green', 'Rough')
    forest.plant_tree(2, 3, 'Pine', 'Dark Green', 'Smooth')
    forest.plant_tree(3, 5, 'Oak', 'Green', 'Rough')
    forest.plant_tree(4, 7, 'Birch', 'White', 'Smooth')
    forest.plant_tree(5, 9, 'Pine', 'Dark Green', 'Smooth')

    forest.draw()
