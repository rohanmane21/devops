def unique_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    if(set1.intersection(set2)):
        print("Common elements: " + str(set1.intersection(set2)))
    else:
        print ("No common elements")

list1 = [3, 6, 9, 12, 15]
list2 = [2, 4, 6, 8, 10, 12, 14]
unique_elements(list1, list2)

