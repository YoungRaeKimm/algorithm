import datetime

def solution(lines):
    answer = 0
    time_window = []
    for i in range(len(lines)):
        end_time = datetime.datetime.strptime(lines[i].split(' ')[0] + ' ' + lines[i].split(' ')[1], '%Y-%m-%d %H:%M:%S.%f')
        start_time = end_time - datetime.timedelta(seconds= float(lines[i].split(' ')[2].strip('s')) - 0.001)
        # print(float(lines[i].split(' ')[2].strip('s')))
        # print(start_time, end_time)
        time_window.append([start_time, end_time])
    # print(time_window[0][0])
    for i in range(len(lines)):
        start_traf = 0
        end_traf = 0
        start_traf2 = 0
        end_traf2 = 0
            
        for j in range(i, len(lines)):
            # start +- 1
            # if time_window[j][0] <= time_window[i][0] and time_window[i][0] <= time_window[j][1]:
            #     start_traf += 1
            # elif time_window[i][0] - datetime.timedelta(seconds = 0.999) <= time_window[j][0] and time_window[j][0] <= time_window[i][0]:
            #     start_traf += 1
            # elif time_window[i][0] - datetime.timedelta(seconds = 0.999) <= time_window[j][1] and time_window[j][1] <= time_window[i][0]:
            #     start_traf += 1
                
            # if time_window[j][0] <= time_window[i][0] and time_window[i][0] <= time_window[j][1]:
            #     start_traf2 += 1
            # elif time_window[i][0] <= time_window[j][0] and time_window[j][0] <= time_window[i][0] + datetime.timedelta(seconds = 0.999):
            #     start_traf2 += 1
            # elif time_window[i][0] <= time_window[j][1] and time_window[j][1] <= time_window[i][0] + datetime.timedelta(seconds = 0.999):
            #     start_traf2 += 1
                
            
            if time_window[j][0] <= time_window[i][1] and time_window[i][1] <= time_window[j][1]:
                end_traf += 1
            elif time_window[i][1] - datetime.timedelta(seconds = 0.999) <= time_window[j][0] and time_window[j][0] <= time_window[i][1]:
                end_traf += 1
            elif time_window[i][1] - datetime.timedelta(seconds = 0.999) <= time_window[j][1] and time_window[j][1] <= time_window[i][1]:
                end_traf += 1
                
            if time_window[j][0] <= time_window[i][1] and time_window[i][1] <= time_window[j][1]:
                end_traf2 += 1
            elif time_window[i][1] <= time_window[j][0] and time_window[j][0] <= time_window[i][1] + datetime.timedelta(seconds = 0.999):
                end_traf2 += 1
            elif time_window[i][1] <= time_window[j][1] and time_window[j][1] <= time_window[i][1] + datetime.timedelta(seconds = 0.999):
                end_traf2 += 1
                
        # print([start_traf, end_traf, start_traf2, end_traf2])
        if answer < max([start_traf, end_traf, start_traf2, end_traf2]) : answer = max([start_traf, end_traf, start_traf2, end_traf2])
    
    return answer

# print(datetime.datetime('2016-09-15 01:00:04.001 2.0s'))
# date_time_str = '2016-09-15 01:00:04.001'
# print(datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f') - datetime.timedelta(seconds = 1))
print(solution( [
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]))