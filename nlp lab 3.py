import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# Download tokenizer (run only the first time)
nltk.download('punkt')

ps = PorterStemmer()

# Open the text file
with open("sample.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Tokenize the text
words = word_tokenize(text)

print("Original Word\tStemmed Word")
print("-" * 35)

# Apply Porter Stemmer
for word in words:
    if word.isalpha():      # Ignore punctuation
        print(word, "\t\t", ps.stem(word))
