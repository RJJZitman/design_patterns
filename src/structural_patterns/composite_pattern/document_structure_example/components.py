from abc import ABCMeta, abstractmethod


class DocumentComponent(metaclass=ABCMeta):
    @abstractmethod
    def render(self):
        pass


class Section(DocumentComponent):
    def __init__(self, title):
        self.title = title
        self.children = []

    def add(self, component):
        self.children.append(component)

    def render(self):
        print(f"Section: {self.title}")
        for child in self.children:
            child.render()


class Paragraph(DocumentComponent):
    def __init__(self, content):
        self.content = content

    def render(self):
        print(f"Paragraph: {self.content}")


class TextElement(DocumentComponent):
    def __init__(self, text):
        self.text = text

    def render(self):
        print(f"Text: {self.text}")