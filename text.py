import pymorphy2
from nltk.tokenize import word_tokenize


class Text:
    def __init__(self, id, text):
        self.id = id
        self.text = text

    def change_person(self):
        tokenized = word_tokenize(self.text)
        morph = pymorphy2.MorphAnalyzer(lang='ru')
        result = ''

        for i in range(len(tokenized) - 1):
            if morph.parse(tokenized[i])[0].tag.person == '1per' and morph.parse(tokenized[i])[0].tag.POS != 'NPRO':
                tokenized[i] = morph.parse(tokenized[i])[0].inflect({'3per'}).word
                result += tokenized[i] if tokenized[i + 1] in ',.!?' else tokenized[i] + ' '
            elif morph.parse(tokenized[i])[0].tag.POS == 'NPRO' and morph.parse(tokenized[i])[0].tag.person == '1per':
                if tokenized[i] == 'я':
                    tokenized[i] = 'он'
                elif tokenized[i] == 'мы':
                    tokenized[i] = 'они'
                elif tokenized[i] == 'меня':
                    tokenized[i] = 'его'
                result += tokenized[i] if tokenized[i + 1] in ',.!?' else tokenized[i] + ' '
            else:
                result += tokenized[i] if tokenized[i + 1] in ',.!?' else tokenized[i] + ' '

        return result + tokenized[-1]
