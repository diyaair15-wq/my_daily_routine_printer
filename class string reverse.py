class StringReverser:
    def __init__(self, text: str):
        self.text = text

    def reverse_words(self) -> str:
        words = self.text.split()
        words.reverse()
        return " ".join(words)
