from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = [
    "university",
    "universe",
    "policy",
    "police",
    "analysis",
    "analyze"
]

print("{:<15}{:<15}".format("Word","Stem"))

for word in words:
    print("{:<15}{:<15}".format(word, ps.stem(word)))

print("\nExamples")
print("Overstemming : university -> univers")
print("Understemming: analysis -> analysi")
