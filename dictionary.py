from tokenizer import tokenize, WORD


class Dictionary:
    def __init__(self, values):
        if not isinstance(values, list):
            raise "values must be list"

        clean = []
        for value in values:
            if not isinstance(value, str):
                raise "non string value in values"
            if value not in clean:
                clean.append(value.lower())

        self.values = clean

    def has(self, value):
        return value.lower() in self.values

    def sentence(self, s):
        tokens = [token[0] for token in tokenize(s) if token[1] == WORD]

        result = [(word, self.has(word)) for word in tokens]

        return result
