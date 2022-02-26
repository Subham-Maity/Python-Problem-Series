# from random_word import RandomWords
from quote import quote
from RandomWrods import random_words


r = RandomWords()
w = r.get_random_word()
print("Keyword Generated: ", w)

res = quote(w, limit=1)
for i in range(len(res)):
    print("\nQuote Generated: ", res[i]['quote'])




