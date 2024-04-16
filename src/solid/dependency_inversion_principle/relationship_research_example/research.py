from relationships import RelationshipBrowser


class Research:
    def __init__(self, browser: RelationshipBrowser, parent: str):
        for p in browser.find_all_children_of(name=parent):
            print(f'{parent} has a child called {p}')
