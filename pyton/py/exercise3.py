
a=[4,9,8,12]
max=a[0]
for number in a:
    if number>max:
        max=number
print(max)

#2

def maximum(number):
    max=number[0]
    for i in number:
        if i>max:
            max=i 
    return max

input=[
    {"name": "Bunthoeun", "score": 90},
    {"name": "Kunthy", "score": 75},
    {"name": "Sreymom", "score": 95}
]
beststudent=""
maxscore=[]
for key in input:
    maxscore.append(key["score"])

print("max score is:",maximum(maxscore))
