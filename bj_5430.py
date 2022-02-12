from collections import deque
t = int(input())

for i in range(t):
    p = input()
    n = int(input())
    x = input().strip('[]').split(',')
    if n > 0:
        x = deque(map(int, x))
        
    rev = False
    if p.count('D') > n:
        print('error')
        continue
    
    for i in range(len(p)):
        if p[i] == 'R':
            if rev:
                rev = False
            else:
                rev = True
        else:
            if rev == True:
                x.pop()
            else:
                x.popleft()
                
    print('[', end='')
    for i in range(len(x)):
        if rev:
            print(x[len(x)-1-i], end='')
            if i != len(x)-1:
                print(end=',')
        else:
            print(x[i], end='')
            if i != len(x)-1:
                print(end=',')
    print(']')