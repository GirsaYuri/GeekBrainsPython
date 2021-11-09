def num_translate(number):
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
    return translate.get(number)
    # for key, val in translate.items():
    #     if number == key:
    #         return val


print(num_translate('one'))
