import re

text = input("Enter a paragraph: ")

sentences = re.split(r'[.!?]+', text)

print("\nSentences are:")
count = 1
for sentence in sentences:
    sentence = sentence.strip()
    if sentence:
        print(str(count) + ". " + sentence)
        count += 1
