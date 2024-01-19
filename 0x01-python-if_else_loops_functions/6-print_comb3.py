#!/usr/bin/python3
for numbers in range(0, 10):
    for nums in range(0, 10):
        if numbers == 8 and nums == 9:
            print("{}{}".format(numbers, nums))
        elif numbers != nums and numbers < nums:
            print("{}{}".format(numbers, nums), end=", ")
        else:
            print(end="")
