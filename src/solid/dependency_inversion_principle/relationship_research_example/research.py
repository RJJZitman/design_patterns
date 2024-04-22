from relationships import RelationshipBrowser


class Research:
    """Enables heritage research"""
    def __init__(self, browser: RelationshipBrowser):
        self.browser = browser

    def find_children_of(self, parent: str):
        """Find children of a parent"""
        for p in self.browser.find_all_children_of(name=parent):
            print(f'{parent} has a child called {p}')
