stop_words = [
    "a","an","the","is","am","are","was","were","be","been","being",
    "i","me","my","we","our","you","your","he","his","she","her",
    "it","its","they","them","their","to","of","in","on","for",
    "with","at","by","from","as","and","or","but"
]

text = input("Enter a sentence: ")

words = text.split()

filtered = []

for word in words:
    w = word.lower().strip(".,!?")
    if w not in stop_words:
        filtered.append(word)

print("\nAfter Removing Stop Words:")
print(filtered)
