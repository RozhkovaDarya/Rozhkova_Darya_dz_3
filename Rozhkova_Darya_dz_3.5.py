# import random


# nouns = ['автомобиль', 'лес', 'огонь', 'город', 'дом']
# adverbs = ['сегодня', 'вчера', 'завтра', 'позавчера', 'ночью']
# adjectoves = ['веселый', 'яркий', 'зеленый', 'утопичный', 'мягкий']


# random.shuffle
# for i in range(5): 
#     print(f"{nouns[i]} {adverbs[i]} {adjectoves[i]}")

# Закомментированный код - это мои собственные мысли, написанные честно мной. 
# Нижний код с функцией - подгляденное в интернете, обмозгованное. 
# Самостоятельно до такого додуматься я бы не смогла. 
# Теперь по подобию, конечно, будет легче делать :)

from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
list_1 = []


def get_jokes(n, flag=False):
  for i in range(n):
    random_index = choice(nouns)
    random_index_1 = choice(adverbs)
    random_index_2 = choice(adjectives)
    joke = f'{random_index} {random_index_1} {random_index_2}'
    list_2 = []
    print(joke)
    if flag == True:
      list_2 = joke.split()
      for noun in nouns:
        for fun in list_2:
          if noun == fun:
            nouns.remove(noun)
            for adverb in adverbs:
              for fun in list_2:
                if adverb == fun:
                  adverbs.remove(adverb)
            for adjective in adjectives:
              for fun in list_2:
                if adjective == fun:
                  adjectives.remove(adjective)

get_jokes(n=5, flag=False)
