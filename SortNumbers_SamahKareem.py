num1, num2 , num3 = input("Enter Three Numbers")
n1, n2, n3 = num1, num2, num3
if n1 > n2 :
         n1, n2 = n2 , n1
if n2 > n3:
    n2, n3 = n3, n2

if n1 > n2 :
    n1, n2 = n2 , n1

print ("The sorted Numbers are :", n1, n2, n3)

