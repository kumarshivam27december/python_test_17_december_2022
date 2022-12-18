list1 = [54, 44, 27, 79, 91, 41]
t=list1[4]
list1.remove(list1[4])
print(list1)
# list1.remove(list1[2])
# print(list1)
# list1.pop()
# print(list1)



# in question expected output is wrong
list1.insert(2,t)
print(list1)
list1.remove(list1[2])
list1.append(t)
print(list1)
