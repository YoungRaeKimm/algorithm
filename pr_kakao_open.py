def solution(record):
    answer = []
    name_dict = {}
    record_list = []
    for i in range(len(record)):
        record_list.append(record[i].split(' '))
        if record_list[i][0] != 'Leave':
            name_dict[record_list[i][1]] = record_list[i][2]
    # print(name_dict)
    for i in range(len(record_list)):
        if record_list[i][0] == 'Enter':
            answer.append(name_dict[record_list[i][1]] + '님이 들어왔습니다.')
        elif record_list[i][0] == 'Leave':
            answer.append(name_dict[record_list[i][1]] + '님이 나갔습니다.')
        # elif record_list[i] == 'Change':
            
    return answer

# print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))