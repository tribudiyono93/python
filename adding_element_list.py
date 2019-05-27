List = []
print("Initial blank list")
print(List)

List.append(1)
List.append(2)
List.append(4)
print("\nList after addition of three elements")
print(List)

for i in range(1,4):
    List.append(i)
print("\nList after addition of elements from 1-3 : ")
print(List)

List.append((5,6))
print("\nList after addition of a tuple : ")
print(List)

List2 = ['For', 'Geeks']
List.append(List2)
print("\nList after addition of a list : ")
print(List)

List.insert(3,12)
List2.insert(0, 'Geeks')
print("\nList after performing insert operation : ")
print(List)

List.extend([8, 'Geeks', 'Always'])
print("\nList after performing extends operation : ")
print(List)



