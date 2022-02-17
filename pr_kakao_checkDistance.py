def solution(places):
    answer = []
    y = [-1, 1, 1, -1, 0, 2, 0, -2]
    x = [1, 1, -1, -1, 2, 0, -2, 0]
    c_y = [[0, -1],[0, 1],[1, 0],[0, -1],0,1,0,-1]
    c_x = [[1, 0],[1, 0],[0, -1],[-1, 0],1,0,-1,0]
    y1 = [0,1,0,-1]
    x1 = [1,0,-1,0]
    for k in range(len(places)):
        check = False
        for i in range(5):
            for j in range(5):
                if places[k][i][j] == 'P':
                    for d in range(4):
                        if i + y[d] < 0 or i + y[d] > 4 or j + x[d] < 0 or j + x[d] > 4:
                            continue
                        new_y = i + y1[d]
                        new_x = j + x1[d]
                        if places[k][new_y][new_x] == 'P':
                            check = True
                            break
                        
                    if check:
                        break
                    
                    for d in range(4):
                        if i + y[d] < 0 or i + y[d] > 4 or j + x[d] < 0 or j + x[d] > 4:
                            continue
                        new_y = i + y[d]
                        new_x = j + x[d]
                        if places[k][new_y][new_x] == 'P':
                            if places[k][i + c_y[d][0]][j + c_x[d][0]] == 'X' and places[k][i + c_y[d][1]][j + c_x[d][1]] == 'X':
                                continue
                            else:
                                check = True
                                break
                    if check:
                        break
                
                    for d in range(4,8):
                        if i + y[d] < 0 or i + y[d] > 4 or j + x[d] < 0 or j + x[d] > 4:
                            continue
                        new_y = i + y[d]
                        new_x = j + x[d]
                        if places[k][new_y][new_x] == 'P':
                            if places[k][i + c_y[d]][j + c_x[d]] == 'X':
                                continue
                            else:
                                check = True
                                break
                    if check:
                        break
                if check:
                    break
            if check:
                break
        if check :
            answer.append(0)
        else :
            answer.append(1)
                    
    return answer
print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))