import array

arr = array.array('i', [1,2,3,1,5])

print("The new created array is : ", end="")
for i in range(0, 5):
    print(arr[i], end=" ")

print("\r")

print("The popped element is :")
print(arr.pop(2))

print("The array after popping is ")
for i in range(0, 4):
    print(arr[i], end=" ")

print("\r")

arr.remove(1)

print("Print the array after removing")
for i in range(0, 3):
    print(arr[i], end=" ")
