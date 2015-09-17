#Learn input function and default type of input being string

age1 = input ("Enter your age: ")
age2 = input ("Enter your age: ")

summa = age1 + age2

print (type (age1))
print (type (summa))
print (summa)
#########################################

#Default type for input is string
#hence we need to typecast to int
age1 = int (input ("Enter your age: "))
age2 = int(input ("Enter your age: "))

summa = age1 + age2

print (type (age1))
print (type (summa))
print (summa)

#similarly we can  typecast to float in case of need
