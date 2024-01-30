class TextEditor:
    def __init__(self):
        self.text = None
        self.state = None
        self.undo_stack = []
        self.redo_stack = []

    def enter_text(self, text):
        self.text = text
        self.state = DefaultState(self.text)

    def apply_bold(self):
        self.undo_stack.append(self.state)
        self.state = BoldState(self.text)

    def apply_italic(self):
        self.undo_stack.append(self.state)
        self.state = ItalicState(self.text)

    def apply_underline(self):
        self.undo_stack.append(self.state)
        self.state = UnderlineState(self.text)

    def undo(self):
        self.redo_stack.append(self.state)
        self.state = self.undo_stack.pop()
        print(f"restored to previous state {self.state}")

    def redo(self):
        self.undo_stack.append(self.state)
        self.state = self.redo_stack.pop()
        print(f"redid the changes to state {self.state}")

class DefaultState:
    def __init__(self, text):
        print(f"{text} is in default state")

class BoldState:
    def __init__(self, text):
        print(f"{text} is in bold state")

    def __str__(self):
        return 'Bold'

class ItalicState:
    def __init__(self, text):
        print(f"{text} is in italics state")

    def __str__(self):
        return 'Italic'

class UnderlineState:
    def __init__(self, text):
        print(f"{text} is in underline state")

    def __str__(self):
        return 'Underline'


te = TextEditor()
te.enter_text('hello')
te.apply_bold()
te.apply_italic()
te.apply_underline()
te.undo()
te.redo()