print("Karan Kumar")
print("2210997112")
my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)
my_list.append(6)
print("List after append:", my_list)
my_list.extend([7, 8, 9])
print("List after extend:", my_list)
my_list.insert(2, 10)
print("List after insertion:", my_list)
my_list.remove(3)
print("List after removal of element 3:", my_list)
popped_element = my_list.pop()
print("Popped element:", popped_element)
print("List after popping:", my_list)
popped_element = my_list.pop(2)
print("Popped element at index 2:", popped_element)
print("List after popping element at index 2:", my_list)
my_list.reverse()
print("Reversed list:", my_list)
my_list.sort()
print("Sorted list:", my_list)
count_of_2 = my_list.count(2)
print("Count of 2 in the list:", count_of_2)
my_list.clear()
print("List after clearing all elements:", my_list)
