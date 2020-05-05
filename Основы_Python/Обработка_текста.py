"""
Дан список текстов, слова в которых разделены пробелами (можно считать, что знаков препинания нет). Часть слов является "мусорными": в них присутствуют цифры и спецсимволы. Отфильтруйте такие слова из каждого текста.

Используйте функции str.split, str.isalpha, str.join, а также list comprehensions.

Пример ввода:

['1 thousand devils', 'My name is 9Pasha', 'Room #125 costs $100']

Пример вывода:

['thousand devils', 'My name is', 'Room costs']

"""

def process(sentences):
    for i in range(len(sentences)):
        sentences[i] = " ".join(list(filter(lambda x: x.isalpha(), sentences[i].split(" "))))

    result = sentences
    return result