def solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer

## 나의 풀이....
# def solution(id_list, report, k):
#     id_idx = {}
#     for i in range(len(id_list)):
#         id_idx[id_list[i]] = i
    
#     arr = [[0 for i in range(len(id_list))] for j in range(len(id_list))]
    
#     for i in range(len(report)):
#         er, ee = report[i].split(' ')
#         arr[id_idx[er]][id_idx[ee]] = 1
#     stop_list = []
#     tmp = [0 for i in range(len(id_list))]
    
#     for i in range(len(id_list)):
#         for j in range(len(id_list)):
#             if arr[i][j] == 1:
#                 tmp[j] += 1
#     for i in range(len(tmp)):
#         if tmp[i] >= k:
#             stop_list.append(i)
#     answer = [0 for i in range(len(id_list))]
#     for i in stop_list:
#         for j in range(len(arr)):
#             if arr[j][i] == 1:
#                 answer[j] += 1
#     return answer

# id_list = ["muzi", "frodo", "apeach", "neo"]
# report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
# k = 2
# print(solution(id_list, report, k))

# a = [[1,2,3], [4,5,6]]
# print(sum(a[0]))