from audioop import reverse
import random
import collections
from typing import Counter
#2.1
names = ["Johan", "Jalle", "Dennis", "Oskar", "Gustaf", "Lisa", "Anna", "Daniel", "Alicia"]
hundred_names = random.choices(names, k = 100)
print(hundred_names)
#2.2
count_names = Counter(hundred_names)
print(count_names)
#2.3
sorted_names = sorted(hundred_names)
print(count_names.most_common(3))
#2.4
print(count_names.most_common()[-1])
#2.5.1
print(*Counter(hundred_names))
#2.5.2
hundred_names.sort()
print(*Counter(hundred_names))
#2.5.3
set_names = set(hundred_names)
list_names = list(set_names)
random.shuffle(list_names)
print(list_names)

list_names.sort()
print(list_names)

