from audioop import add


my_list = [*range(1,11,1)]
print(my_list)

add_one = map(lambda x: x + 1, my_list)
print(list(add_one))