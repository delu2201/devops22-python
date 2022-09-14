from asyncio import events
import collections
from collections import Counter
from operator import itemgetter
from posixpath import split
import random


#1 1-100 med "list comprehension"
hundred = [x for x in range(1,101)]
#print(hundred)

#2 Jämna tal med for-loop fr. 2-60.
even_numbers = []
for i in range(2,61,2):
    even_numbers.append(i)

#print(even_numbers)

#3 ojämna tal med list comprehension fr. 1-77.
odd_numbers = [n for n in range(1,78,2)]
print(odd_numbers)

#4.generera lista med 100 tal mellan 100-300. Unika tal, random.
random_list = random.sample(range(300), k = 60)
print(random_list)

#5.1
colors = ["blue", "green", "pink", "yellow", "purple"]
red_list = ["red"]

red_list.extend(random.sample(colors, k = 2))
print(red_list)

#5.2
random_colors = random.choices(colors, k = 50)
print(random_colors)

#5.3
print (f'Colors: {len(colors)}, Red list: {len(red_list)}, Random Colors:{len(random_colors)}')
count_colors = Counter(colors)
count_red = Counter(red_list)
count_random = Counter(random_colors)
print(count_colors)
print(count_red)
print(count_random)
