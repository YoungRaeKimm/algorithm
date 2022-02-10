num = int(input())
arr = []
score = []
for i in range(num):
    a, b = input().split()
    arr.append([int(a),int(b)])
for i in range(num):
    s = 1
    for j in range(num):
        if i == j:
            continue
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            s += 1
    score.append(s)
    
    print(score[i], end=" ")