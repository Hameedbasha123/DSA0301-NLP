from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = [
    "caresses",
    "ponies",
    "ties",
    "cats",
    "running",
    "playing",
    "happiness",
    "relational"
]

print("{:<15}{}".format("Original","Stem"))

for word in words:
    print("{:<15}{}".format(word, ps.stem(word)))
