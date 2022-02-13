import math
def solution(s):
    if len(s) == 1:
        return 1
    len_list = []
    for sub in range(1, int(len(s)/2)+1):
        tmp_len = len(s)
        i=0
        tmp_count, tmp_ten = 1, 1
        while i < len(s)-sub+1:
            if i >= sub and s[i-sub:i] == s[i: i+sub]:
                tmp_count += 1
                tmp_len = tmp_len - sub
                if tmp_count == math.pow(10, tmp_ten):
                    tmp_len += 1
                    tmp_ten += 1
                i += sub
                continue
            elif s[i:i+sub] == s[i+sub:i+2*sub]:
                tmp_count = 2
                tmp_len = tmp_len - sub + 1
                i += sub*2
            else:
                tmp_count = 1
                tmp_ten = 1
                i += sub
        len_list.append(tmp_len)
        # print(tmp_len)
        
    return min(len_list)

print(solution("xxxxxxxxxxyyy"))