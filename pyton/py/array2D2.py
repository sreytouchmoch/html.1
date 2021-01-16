array2D=[
    ["A","B","c"],
    ["D","F","c"],
    ["A","A","F"],
    ["v","B","c"],
]
number=int(input())
text=""
ifTrue=True
for i in range(len(array2D)):
    if len(array2D[i])> number:
        array2D[i][number]="*"
    else:
        text=("cloumn error")
        ifTrue=False
if ifTrue:
    print(array2D)
else:
    print(text)