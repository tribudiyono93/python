import operator

s1 = "geeksfor"

s2 = "geeks"

print("The concatenated string is : ", end="")
print(operator.concat(s1, s2))

if(operator.contains(s1,s2)):
	print("geeksfor contains geeks")
else :
	print("geeksfor doest not contain geeks")