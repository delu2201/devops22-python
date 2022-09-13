# #1
# def printing(start=1, stop=11):
#     for i in range(start,stop):
#         print(i)

# printing()

#2
def reverse(arg=None):
    string = "abcdefgh"
    if arg == "reverse=True":
        backwards = sorted(string, reverse=True)
        for n in range(len(backwards)):
            print(backwards[n], end="")
    else: 
        for i in range(len(string)):
            print(string[i], end="")

reverse("reverse=True")