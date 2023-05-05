#!/usr/bin/python3

def linear_search(list, length, key):
    for i in range(0, length):
        if (list[i] == key):
            return i
    return -1

list = [12, 23, 52, 72, 33, 918, 88, 58, 73, 12, 11, 52]
print("The list is:", list)
length = len(list)
print("The length of the list is", length)

# Call the function
key = int(input("Please input the item to be searched:"))
print("Number to be found", key)
index = linear_search(list, length, key)

if (index == -1):
    print("Item not in the list.")
else:
    print("Item is in the list at position of: ", index)


