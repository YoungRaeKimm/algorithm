def solution(stones, k):
    left = 0
    right = max(stones)
    while left <= right:
        m = int((left + right)/2)
        tmp_len, tmp_max_len = 0, 0
        for i in range(len(stones)):
            if stones[i] <= m:
                tmp_len += 1
            else:
                if tmp_max_len < tmp_len: tmp_max_len = tmp_len
                tmp_len = 0
            if tmp_len >= k: break
        if tmp_max_len < tmp_len: tmp_max_len = tmp_len    
            
        if tmp_max_len < k:
            left = m + 1
        else:
            right = m - 1
            result = m
    return result
    
print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))