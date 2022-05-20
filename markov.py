from corpus.text import holmes
from re import split, sub
from random import choice

# {
#     "word": ["next", "next", "next"]
# }

class Markov:
    def __init__(self, corpus):
        self.words = self.generate_words(self.preprocessing(corpus))

    def preprocessing(self, corpus):
        # 1. lower case everything
        # 2. remove all special chars
        # 3. split into words

        corpus = split(" |\n", sub("[^a-zA-Z ]", " ", corpus.lower()))
        return [word.strip() for word in corpus if len(word.strip()) > 0]

    def generate_words(self, corpus):
        words = {}

        for i in range(len(corpus) - 1):
            word = corpus[i]
            words[word] = words.get(word, []) + [corpus[i + 1]]

        return words

    def generate_sentence(self, length, genesis=None):
        genesis = genesis or choice(list(self.words.keys()))
        sentence = [genesis]

        for i in range(length):
            sentence.append(self.generate_word(sentence[-1]))

        return " ".join([word for word in sentence if word is not None])

    def generate_word(self, word):
        return choice(self.words.get(word, [None]))

markov = Markov(corpus=holmes)