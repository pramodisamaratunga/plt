class PigLatin:

    def __init__(self, phrase: str):
        self._phrase = phrase

    def _init_(self, phrase: str):
        self.phrase = phrase

    def get_phrase(self) -> str:
        return self.phrase

    def translate(self) -> str:
        pass