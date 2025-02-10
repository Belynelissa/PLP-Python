# Create an empty list called my_list.
my_list = []


# Append the following elements to my_list: 10, 20, 30, 40.
my_list = []
>>> my_list.extend([10, 20, 30, 40])
>>> print(my_list)


# Insert the value 15 at the second position in the list.
my_list= [10, 20, 30, 40]
>>> my_list.insert(10,15)
>>> print(my_list)


# Extend my_list with another list: [50, 60, 70].
my_list = [10, 15, 20, 30, 40] 
>>> my_list = my_list + [50, 60, 70]
>>> print(my_list)

# Remove the last element from my_list.
my_list = [10, 15, 20, 30, 40, 50, 60, 70]
>>> my_list.pop(-1)
>>> print(my_list)

# Sort my_list in ascending order.
my_list = [10, 15, 20, 30, 40, 50, 60]
>>> my_list.sort(reverse = True)
>>> print(my_list)


#Find and print the index of the value 30 in my_list.
my_list = [10, 15, 20, 30, 40, 50, 60]
>>> print(my_list.index(30))
