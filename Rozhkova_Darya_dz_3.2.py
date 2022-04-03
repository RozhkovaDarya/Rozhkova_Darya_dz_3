def num_translate_adv(i):
  num = {
    'one': 'один',
    'One': 'Один',
    'two': 'два',
    'Two': 'Два',
    'three': 'три',
    'Three': 'Три',
    'four': 'четыре',
    'Four': 'Четыре',
    'five': 'пять',
    'Five': 'Пять',
    'six': 'шесть',
    'Six': 'Шесть',
    'seven': 'семь',
    'Seven': 'Семь',
    'eight': 'восемь',
    'Eight': 'Восемь',
    'nine': 'девять',
    'Nine': 'Девять',
    'ten': 'десять',
    'Ten': 'Десять'
  }  
  if i in num:
    return num[i]
  else:
    return None

print(num_translate_adv('eleven'))
