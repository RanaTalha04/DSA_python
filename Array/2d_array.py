print("2D Array Example:\n")


arr1 = [
    ['apple', 'banana', 'cherry'],
    ['dog', 'cat', 'mouse'],
    ['red', 'green', 'blue']
]

for row in arr1:
    for item in row:
        print(item, end=' ')
    print()
      
print("\n")

num_pad = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    ['*', 0, '#']
]

for row in num_pad:
    for item in row:
        print(item, end=' ')
    print()  
