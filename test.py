from nltk.tokenize import word_tokenize
import pymorphy2

text = 'Я шла по шоссе'

tokenized = word_tokenize(text)
morph = pymorphy2.MorphAnalyzer(lang='ru')
for i in range(len(tokenized)):
    if morph.parse(tokenized[i])[0].tag.person == '1per':
        print(morph.parse(tokenized[i])[0].inflect({'3per'}))
        tokenized[i] = morph.parse(tokenized[i])[0].inflect({'3per'})

print(' '.join(tokenized))