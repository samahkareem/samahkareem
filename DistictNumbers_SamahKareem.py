mylist = input("enter ten numbers separated by a space in one line")
list1 = mylist.split()
list2 = []
for i in range(len(list1)):
   if not list1[i] in list2:
    list2.append(list1[i])
print("The distinct numbers are: ")
for i in range(len(list2)):
 print(list2[i], end=' ')
print()