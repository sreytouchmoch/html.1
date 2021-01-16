array2D=[
    ["A","B","c"],
    ["D","F","c"],
    ["A","A","F"],
    ["v","B","c"],
]
row=int(input())
for k in range(len(array2D[row])):
    array2D[row][k]="*"
print(array2D)
