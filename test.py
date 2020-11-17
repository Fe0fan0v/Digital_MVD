from nltk.tokenize import word_tokenize
import pymorphy2

text = 'В октябре законопроект был принят палатой представителей конгресса США. Для его вступления в силу в ' \
       'течение десяти дней он должен быть подписан президентом США. Закон носит имя экс-директора московской ' \
       'антидопинговой лаборатории Григория Родченкова, который выступает главным информатором WADA по делу о ' \
       'допинге в российском спорте.'

tokenized = word_tokenize(text)
morph = pymorphy2.MorphAnalyzer(lang='ru')
for i in range(len(tokenized)):
    if morph.parse(tokenized[i])[0].tag.person == '1per':
        print(morph.parse(tokenized[i])[0].inflect({'3per'}))
        tokenized[i] = morph.parse(tokenized[i])[0].inflect({'3per'})

print(' '.join(tokenized))