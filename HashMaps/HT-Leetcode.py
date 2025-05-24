# Item in common
# First Approach BigO (n*2) --- Bad approach

def item_in_common1(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False

# Second approach BigO (n) --- Good approach
def item_in_common2(list1, list2):
    my_dict = {}
    for i in list1:
        my_dict[i] = True
    for j in list2:
        if j in my_dict:
            return True
    return False

list1 = [1, 3, 5]
list2 = [2, 4, 9]
list3 = [5, 6, 10]

print(item_in_common1(list1, list2))
print(item_in_common2(list1, list3))

#----------------------***----------------------------

# Find duplicates

def find_duplicates(list):
    my_dict = {}
    duplicate_list = []
    for i in list:
        if i in my_dict:
            duplicate_list.append(i)
        else:
            my_dict[i] = True
    return duplicate_list
duplicate_list = [1, 2, 3, 4, 5, 5]
print('Duplicate List: ', find_duplicates(duplicate_list))