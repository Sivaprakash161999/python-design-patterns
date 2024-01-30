from abc import ABC, abstractmethod

class TextProcessor(ABC):

    def __init__(self, text):
        self.text = text

    @abstractmethod
    def process_text(self):
        pass

class UpperCase(TextProcessor):

    def process_text(self):
        return self.text.upper()
    
class LowerCase(TextProcessor):

    def process_text(self):
        return self.text.lower()
    
class Capitalize(TextProcessor):

    def process_text(self):
        return self.text.capitalize()



def process_text(text, operation):
    if operation == "uppercase":
        return text.upper()
    elif operation == "lowercase":
        return text.lower()
    elif operation == "capitalize":
        return text.capitalize()
    else:
        return text
    
text_processors = {
    'uppercase': UpperCase,
    'lowercase': LowerCase,
    'capitalize': Capitalize,
}

input_text = "This is an example text."
operation = "uppercase"

text_processor = text_processors[operation](input_text)

output_text = text_processor.process_text()
print(output_text)