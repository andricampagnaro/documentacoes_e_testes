### Sorting a list form low to high
list_1 = [7, 26, 34, 2, 12, 98, 56]
list_2 = sorted(list_1)
### Getting the max, min, and sum of a list
list_sum = sum(list_1) 
max_val = max(list_1)
min_val = min(list_1)
### Convert a string to a list where each element is a character
>>> list("bob")
["b", "o", "b"]
### You can quickly reverse a list
>>> list_1.reverse()
[56, 98, 12, 2, 34, 26, 7]
### Are any or all of the items in our list True?
>>> bool_list = [True, False, True, True]
>>> any(bool_list)
True
>>> all(bool_list)
False
### You can loop through a list's values AND indices simultaneously
for index, value in enumerate(list_1):
    "do stuff"