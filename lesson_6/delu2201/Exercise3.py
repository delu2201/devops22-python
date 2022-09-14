import string

alphabet = list(string.ascii_lowercase)
stack = []
for n in alphabet:
    stack.append(n)

print(stack)

for i in range(len(stack)):
    print(stack.pop(), end= " ")

