import csv
from sys import exec_prefix
# from datetime import date, datetime

# test_list = ["Hej", "något", "boll", "puck"]

# test_list.insert(0,datetime.now().strftime("%Y/%m/%d/ %H:%M:%S"))

# with open("orders.csv", "w+", newline='') as file:
#     csv_writer = csv.writer(file, delimiter=",")

#     for item in test_list:
#         csv_writer.writerow(test_list)

# #print(order_time)
# print(test_list)
lst = []
try:
    with open ("orders.csv", "r", newline="") as f:
        reader = csv.reader(f)
        # next(f)
        for row in f:
            lst.append(row)
except FileNotFoundError:
    print("File for saving orders does not exist. Contact systam admin.")
except Exception as e:
    print(e)
print(lst[-1])
lst2= str(lst[-1])
cur_orderId = (lst2[21])
print(cur_orderId)



