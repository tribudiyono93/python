Dict = {5: 'Welcome', 6: 'To', 7: 'Geeks',
        'A': {1: 'Geeks', 2: 'For', 3: 'Geeks'},
        'B': {1: 'Geeks', 2: 'Life'}}
print("Initial dictionary")
print(Dict)

del Dict[6]
print("\nDeleting a specific key")
print(Dict)

del Dict['A'][2]
print("\nDeleting a key from nested dictionary")
print(Dict)

Dict.pop(5)
print("\nPopping specific element")
print(Dict)

Dict.popitem()
print("\nPops first item")
print(Dict)

Dict.clear()
print("\nDeleting entire dictionary")
print(Dict)
