import re

text = input("Enter a sentence: ")

words = re.findall(r'\b\w+\b', text.lower())

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("\nWord Frequency:")

for word in frequency:
    print(word, ":", frequency[word])
