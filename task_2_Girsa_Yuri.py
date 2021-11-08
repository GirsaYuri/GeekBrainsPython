def num_translate(number):
    for key, val in translate.items():
        if number.istitle() and translate.get(number.lower()):
            return translate.get(number.lower()).title()
        else:
            return translate.get(number)


translate = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять',
}

print(num_translate(input('Введите число: ')))
