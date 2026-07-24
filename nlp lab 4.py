from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import SnowballStemmer

porter = PorterStemmer()
lancaster = LancasterStemmer()
snowball = SnowballStemmer("english")

words = ["running","playing","studies","happiness","government"]

print("{:<15}{:<15}{:<15}{:<15}".format("Word","Porter","Lancaster","Snowball"))

for word in words:
    print("{:<15}{:<15}{:<15}{:<15}".format(
        word,
        porter.stem(word),
        lancaster.stem(word),
        snowball.stem(word)
    ))
