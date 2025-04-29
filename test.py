#I am learing python Variable
name = "rafiul"

#Data types
print(type(name))
print(type(name) == str)
print(isinstance(name, str)) 

age = 2
print(isinstance(age,int))

age = 2.3
print(isinstance(age,float))

age = float(2)
print(isinstance(age,float ))

#casting or conversion
number = "20"
age = int (number)
print(isinstance(age, int))

#complex for complex numbers
#bool for booleans
#list for lists
#tuple for tuples
#range for ranges
#dict for dictionaries
#set for sets


#opeartors
5 // 2 #2 floor division

#comparison operator
a=1
b=2
a == b  #false
a != b  #true


#boolean operator
condition1 = True
condition2 = False


not condition1 #false
condition1 and condition2 #false
condition1 or condition2 #true


# OR operator
print (0 or 1) ##1
print (False or 'hey') ##'hey
print ('hi' or 'hey') ##'hi'
print ([] or False) ## False
print (False or []) ## []

#or operator returns the value of the first operand that is not a False value, otherwise it returns the second operand

# and operator
print (0 and 1) ##0
print (False and 'hey') ##False
print ('hi' and 'hey') ##'hi'
print ([] and False) ## []
print (False and []) ## False

#and operator returns the value of the first operand that is a False value, otherwise it returns the second operand

# bitwise opeartor
# &, | ^ (Binary XOR), ~ (Binary NOT), << (Shift left), >> (Shift right)

#is and in

#ternary opeartor
def is_adult(age):
    True if age > 18 else False
    