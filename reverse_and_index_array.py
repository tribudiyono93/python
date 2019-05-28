import array

arr = array.array('i', [1,2,3,1,2,5])

print("The new created array is ")
for i in range(0,6):
    print(arr[i], end=" ")

print("\r")

print("The index of 1st of 2 is ")
print(arr.index(2))

arr.reverse()

print("The array after reversing is ")
for i in range(0,6):
    print(arr[i], end=" ")