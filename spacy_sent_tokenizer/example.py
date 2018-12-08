import spacy

print()

nlp = spacy.load('en_core_web_sm')
doc = nlp(u"This is a sentence. This is another sentence.")
for sent in doc.sents:
    print(sent.text)