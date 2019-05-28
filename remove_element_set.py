set1 = set([1,2,3,4,5,6,7,8,9,10,11,12])
print("Initial set")
print(set1)

set1.remove(5)
set1.remove(6)
print("\nSet after removal of two elements")
print(set1)

set1.discard(8)
set1.discard(9)
print("\nSet after discarding two elements")
print(set1)

for i in range(1,5):
    set1.remove(i)
print("\nSet after removing a range of elements ")
print(set1)

set1.pop()
print("\nSet after popping element")
print(set1)

set1.clear()
print("\nSet after clearing all elements")
print(set1)

