from copy import deepcopy
def padding(key, lock):
    padding_y = [[0]*(len(lock)+(len(key)-1)*2)]
    padding_x = [0]*(len(key)-1)
    for i in range(len(key)-1):
        lock = padding_y + lock
    for i in range(len(lock) - (len(key)-1)):
        lock[i+(len(key)-1)] = padding_x + lock[i+(len(key)-1)] + padding_x
    for i in range(len(key)-1):
        lock = lock + padding_y
    return lock
        
def concat_and_check(key, lock, n_y, n_x):
    # print(lock)
    tmp_key = deepcopy(key)
    tmp_lock = deepcopy(lock)
    for i in range(len(tmp_key)):
        for j in range(len(tmp_key)):
            tmp_lock[n_y + i][n_x + j] += tmp_key[i][j]
    for i in range(len(tmp_key)-1,len(tmp_lock) - len(tmp_key) + 1):
        for j in range(len(tmp_key)-1,len(tmp_lock) - len(tmp_key) + 1):
            if tmp_lock[i][j] == 0 or tmp_lock[i][j] > 1:
                return False
    return True
        
def solution(key, lock):
    after_padding = padding(key, lock)
    keys = [
    key,                                                                        # 0도, 기본
    list(zip(*reversed(key))),                                                  #90도, 회전
    list(map(lambda e:list(reversed(e)), reversed(key))),                       #180도, 회전
    list(map(lambda e:list(reversed(e)), reversed(list(zip(*reversed(key)))))), #270도, 회전
    ]
    for i in range(4):
        after_rotate_key = keys[i]
        for j in range(len(lock)+len(key)-1):
            for k in range(len(lock)+len(key)-1):
                if concat_and_check(after_rotate_key, after_padding, j, k):
                    return True
    return False

print(solution([[1]], [[0]]))