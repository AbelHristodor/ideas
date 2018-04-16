import random

numbers = input("How many numbers do you want? ")
num_range1 = input("from ")
num_range2 = input("to ")


for i in range(int(numbers)):
    print(random.randrange(int(num_range1),int (num_range2)))
