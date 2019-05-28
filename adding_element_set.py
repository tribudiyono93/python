set1 = set()
print("Initial blank set")
print(set1)

set1.add(8)
set1.add(9)
set1.add(12)
print("\nSet after addition of three elements")
print(set1)

for i in range(1,6):
    set1.add(i)
print("\nSet after addition of elements from 2-5")
print(set1)

set1.add((6,7))
print("\nSet after addition of a tuple")
print(set1)

set1.update([10,12])
print("\nSet after addition of elements using update")
print(set1)