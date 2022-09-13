from collections import deque
from queue import Empty
import random
names = ["lisa", "olle", "pelle"]

#1
list_of_names = random.choices(names, k = 50)
# print ("*** LIST OF NAMES ***")
# print(list_of_names)

#2
queue_of_names = deque([], maxlen = 10)
print(queue_of_names)
exit()
for i in range(10):
    queue_of_names.append(list_of_names[i])

#print(queue_of_names)

#3
while len(queue_of_names) > 0:
    n = random.randint(1,10)
    print(n)
    for i in range(n):
        if queue_of_names == 0:
            break
        else: 
            queue_of_names.popleft()
            print(queue_of_names)
