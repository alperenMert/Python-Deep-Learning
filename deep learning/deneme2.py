
import nltk
#nltk.download('punkt')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
#nltk.download('stopwords')

#Cümleyi kelimelere ayır

tokens = word_tokenize("The quick brown fox jumps over the lazy dogs and hello guys cats")
print(tokens)

#anlamı olmayan kelimeleri at

stop_words = set(stopwords.words('english'))
tokens = [w for w in tokens if not w in stop_words]
print(tokens)

#kelime köklerini bul

porter = PorterStemmer()
stems = []
for t in tokens:
    stems.append(porter.stem(t))
print(stems)