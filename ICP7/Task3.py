import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.util import ngrams
from nltk.stem import SnowballStemmer
from nltk.stem import LancasterStemmer
from nltk import wordpunct_tokenize, pos_tag, ne_chunk
#Reads the input.txt file
file_content = open("input.txt").read()
# a) Tokenization
# Word tokenization
wtokens = nltk.word_tokenize(file_content)
print("Tokenization")
for t in wtokens:
    print(t)

# b) POS
print("POS sravs",nltk.pos_tag(wtokens))

# c) Stemming
print("PorterStemmer")
pStemmer = PorterStemmer()
for t in wtokens:
    print(t, pStemmer.stem(t.lower()))
print("LancasterStemmer")
lStemmer = LancasterStemmer()
for t in wtokens:
    print(t, lStemmer.stem(t.lower()))
print("SnowballStemmer")
snowball = SnowballStemmer('english')
for t in wtokens:
    print(t, snowball.stem(t.lower()))
# d) Lemmatization
lemmatizer = WordNetLemmatizer()
print("Lemmatization")
for t in wtokens:
    print(t, lemmatizer.lemmatize(t.lower()))
# e) Trigram
print("Trigrams")
trigrams = list(ngrams(wtokens, 3))
print(trigrams)
# f) Named entity recognition
print("Named entity recognition")
print(ne_chunk(pos_tag(wordpunct_tokenize(file_content))))