import re

text = input("Enter a sentence: ")

words = re.findall(r'\b\w+\b', text)

print("\nTotal Words =", len(words))
