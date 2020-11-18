class MyStringBuilder:
    """A dummy string builder handling just string appending."""
    
    def __init__(self):
        self.storedText = []

    def Append(self, textToAppend):
        self.storedText.append(textToAppend)

    def ToString(self):
        return "".join(self.storedText)
        



