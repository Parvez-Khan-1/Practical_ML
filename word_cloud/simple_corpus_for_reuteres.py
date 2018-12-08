import matplotlib.pyplot as plt
from nltk.corpus import reuters
from wordcloud import WordCloud


Custom_Word_List = ["Parvez", "is", "machine", "learning", "expert", "He", "Work", "at", "Synerzip",
                    "He", "has", "expertise", "in", "natural", "language", "processing", "Machine",
                    "Learning", "Is", "Very", "Popular", "Technology"]
print(reuters.words())
words = ' '.join(Custom_Word_List)
wc = WordCloud().generate(words)
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()