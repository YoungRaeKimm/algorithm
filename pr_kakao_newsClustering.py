import re
def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    
    r = re.compile('[a-z]{2}')
    d1, d2 = {}, {}
    for i in range(len(str1)-1):
        if len(r.findall(str1[i:i+2])) == 0:
            continue
        if d1.get(str1[i:i+2]) != None:
            d1[str1[i:i+2]] += 1
        else:
            d1[str1[i:i+2]] = 1
    for i in range(len(str2)-1):
        if len(r.findall(str2[i:i+2])) == 0:
            continue
        if d2.get(str2[i:i+2]) != None:
            d2[str2[i:i+2]] += 1
        else:
            d2[str2[i:i+2]] = 1
    print(d2)
    answer = 0    
    for i in d1:
        if d2.get(i) == None:
            continue
        else:
            answer += min(d1[i], d2[i])
    div = 0
    for i in d1:
        if d2.get(i) == None:
            div += d1[i]
        else:
            div += max(d1[i], d2[i])
    for i in d2:
        if d1.get(i) == None:
            div += d2[i]
            
    if div > 0:
        answer = int(answer/div * 65536)
    else:
        answer = 65536
    
    return answer
print(solution('aa1+aa2', 'AAAA12'))