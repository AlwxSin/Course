from random import randint
x = randint(1, 100)
#print(x)
s = 1 #Number of attempts
y = int(input("Enter the number => "))
while y != x:
   if x > y: y = int(input("Your number is lower then need. Try harder => "))
   else: y = int(input("Your number is higher then need. Try harder => "))
   s += 1
print("Success after " + str(s) + " attempts")
