Tuple1 = ()
print("Initial empty tuple")
print(Tuple1)

Tuple1 = ('Geeks', 'For')
print("\nTuple with the use of string")
print(Tuple1)

list1 = [1,2,4,5,6]
print("\nTuple using list : ")
print(tuple(list1))

Tuple1 = ('Geeks')
n = 5
print("\nTuple with a loop")
for i in range(int(n)):
    Tuple1 = (Tuple1,)
    print(Tuple1)

Tuple1 = (0,1,2,3)
Tuple2 = ('python','geek')
Tuple3 = (Tuple1, Tuple2)
print("\nTuple with nested tuples")
print(Tuple3)

Tuple1 = ('Geeks', ) * 3
print("\nTuple with repetition ")
print(Tuple1)