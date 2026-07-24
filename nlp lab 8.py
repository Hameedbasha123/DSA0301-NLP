import re

text = input("Enter a sentence: ")

words = re.findall(r'\b\w+\b', text)

print("\nWords are:")
for word in words:
    print(word)
