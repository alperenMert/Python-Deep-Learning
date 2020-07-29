from snowballstemmer import TurkishStemmer

tr_stemmer = TurkishStemmer()

text = "Merhaba selam alperen"

stemmed_words = tr_stemmer.stemWords(text)

my_data = [" ".join(a) for a in stemmed_words]

print(my_data)



