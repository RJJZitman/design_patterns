from components import Section, Paragraph, TextElement


if __name__ == "__main__":
    # Create a document structure
    doc = Section("Main Document")

    intro = Section("Introduction")
    intro.add(Paragraph("Welcome to the document!"))
    intro.add(Paragraph("This is an example of composite pattern."))

    body = Section("Body")
    body.add(Paragraph("This is a paragraph in the body section."))
    body.add(TextElement("Some inline text here."))

    conclusion = Section("Conclusion")
    conclusion.add(Paragraph("Thank you for reading!"))

    doc.add(intro)
    doc.add(body)
    doc.add(conclusion)

    # Render the entire document
    doc.render()
