#!/usr/bin/env python3

"""Given a list in Python and provided the positions of the elements
, write a program to swap the two elements in the list. 

Examples:  

    Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
    Output : [19, 65, 23, 90]

    Input : List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
    Output : [1, 5, 3, 4, 2]"""

list1 = [23, 65, 19, 90]
pos1 = 1
pos2 = 3

def swap_list(the_list, pos1, pos2):

    index_1 = pos1 - 1
    index_2 = pos2 - 1
    list_item_1 = the_list[index_1]
    list_item_2 = the_list[index_2]
    
    the_list[index_1] = list_item_2
    the_list[index_2] = list_item_1

    return (the_list)

print(swap_list(list1, pos1, pos2))


