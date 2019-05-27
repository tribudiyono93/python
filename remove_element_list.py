List = [1,2,3,4,5,6,7,8,9,10,11,12]
print("Initial list : ")
print(List)

List.remove(5)
List.remove(6)
print("\nList after removal of two elements")
print(List)

for i in range(1,5):
    List.remove(i)
print("\nList after removing a range of elements")
print(List)

List.pop()
print("\nList after removing a range of elements ")
print(List)

List.pop(2)
print("\nList after popping a specific element :")
print(List)