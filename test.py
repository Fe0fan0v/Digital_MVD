import pymorphy2
morph = pymorphy2.MorphAnalyzer()


from PyDictionary import PyDictionary
dictionary = PyDictionary()
print(dictionary.synonym("хорошо"))
