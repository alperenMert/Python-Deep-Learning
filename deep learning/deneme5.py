
import nltk
#nltk.download()

from collections import Counter
import nltk, string
from nltk.corpus import stopwords
from snowballstemmer import stemmer
from nltk.tokenize.treebank import TreebankWordDetokenizer


doc = 'The reason there is no simple answer is you actually need the span locations of the original ' \
      'tokens in the string. If you do not have that, and you are not reverse engineering your original tokenization,' \
      ' your reassembled string is based on guesses about the tokenization rules that were used. If your tokenizer did not ' \
      'give you spans, you can still do this if you have three things:'



#kelimeleri bul
tokens = nltk.word_tokenize(doc.lower())

#noktalamaları çıkar
tokens = [i for i in tokens if i not in string.punctuation]

#kök bul
stemmer = nltk.stem.porter.PorterStemmer()

def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]


tokens = stem_tokens(tokens)

#token String dönüşümü
deg=TreebankWordDetokenizer().detokenize(tokens)

#anlamı olmayan kelimeleri at
stop_words = set(stopwords.words('english'))
anlamli = [w for w in tokens if not w in stop_words]


#token String dönüşümü
deg2=TreebankWordDetokenizer().detokenize(anlamli)

#kelme sayısını bul
kelimeler = deg2.split()
print('Anlamlı kelime sayısı:', len(kelimeler))
enFazla=kelimeler[0:5]

# Kelime çantasını hazırlamak bir satır
kelime_sayi = Counter(kelimeler)
print(type(kelime_sayi), '\n')

dizi=[]
# En sık kullanılan 5 kelimeye
for kelime in kelime_sayi.most_common(5):
    dizi = dizi+ [kelime[0]]
    print(kelime)

print(dizi)


#anlamlı cümle kur(2 kelime)
bigrams = nltk.bigrams(dizi)
for x in bigrams:
    print(x)

