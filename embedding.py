class Embedding:

    def encode(self, text):

        vector = []

        for char in text:
            vector.append(ord(char))

        return vector