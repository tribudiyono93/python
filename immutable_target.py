import operator

x = 5
y = 6
a = 5
b = 6

z = operator.add(a,b)

p = operator.iadd(x,y)

print("Value after adding using normal operator")
print(z)

print("Value after adding using inplace operator")
print(p)

# printing value of first argument 
# value is unchanged 
print ("Value of first argument using normal operator : ",end="") 
print (a) 
  
# printing value of first argument 
# value is unchanged 
print ("Value of first argument using Inplace operator : ",end="") 
print (x)