from dataclasses import dataclass
class Sentence:
    def __init__(self, sentence=""):
        self.sentence = sentence

    def __iter__(self):
        return self

    def __next__(self, start, end):
        current = start
        try:
            return self.sentence[current]
        except StopIteration as e:
            print(e)
