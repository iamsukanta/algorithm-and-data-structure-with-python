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

#----------------------------***-------------------------

#First Non repeating character
def first_non_repeating_char(word):
    my_dict = {}
    for i in word:
        if i in my_dict:
            del my_dict[i]
        else:
            my_dict[i] = True
    
    first_key = next(iter(my_dict), None)
    return first_key

print('First non repeating char: ', first_non_repeating_char('leetcode'))

# -------------------------------****-------------------------------
# Find Anagram groups
def group_anagrams(strings):
    my_dict = {}
    for word in strings:
        key = ''.join(sorted(word))
        if key not in my_dict:
            my_dict[key] = []
        my_dict[key].append(word)

    return list(my_dict.values())

print ('Anagrams groups: ', group_anagrams(['eat', 'tan', 'bat', 'tea']))

# -----------------------------****-----------------------------------
# Two sum function Bad approach, Time complexity: O(n*2)
def two_sum1(list, target):
    for i in range(len(list)):
        for j in range(len(list)):
            if i == j:
                continue
            else:
                if list[i] + list[j] == target:
                    return [i, j]
    return []

# Two sum good approach, 
def two_sum2(list, target):
    for i in range(len(list)):
        for j in range(len(list)):
            if i == j:
                continue
            else:
                if list[i] + list[j] == target:
                    return [i, j]
    return []

print('Two Sum: ', two_sum1([10, 15, 5, 2, 8, 1, 7], 12))
print('Two Sum: ', two_sum2([10, 15, 5, 2, 8, 1, 7], 12))

