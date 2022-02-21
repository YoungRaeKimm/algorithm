import re
import itertools

def solution(user_id, banned_id):
    dic = {}
    for i in range(len(banned_id)):
        if dic.get(banned_id[i]) == None:
            dic[banned_id[i]] = 1
        else:
            dic[banned_id[i]] += 1
        
    able_list = []
    for i in range(len(banned_id)):
        r = re.compile(banned_id[i].replace("*", "[0-9a-z]"))
        tmp_list = []
        for j in range(len(user_id)):
            if r.fullmatch(user_id[j]) != None:
                tmp_list.append(j)
        able_list.append(tmp_list)
    
    per = list(itertools.permutations(range(len(user_id)), len(banned_id)))
    
    for i in range(len(able_list)):
        tmp = []
        for j in range(len(able_list[i])):
            for k in range(len(per)):
                if per[k][i] == able_list[i][j]:
                    tmp.append(per[k])
        per = tmp
    ans = []
    for i in range(len(per)):
        per[i] = set(per[i])
        if per[i] not in ans:
            ans.append(per[i])
    return len(ans)

a = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
b = ["fr*d*", "*rodo", "******", "******"]
print(solution(a,b))