def calculate(str_time):
    return int(str_time[:2]) * 60 + int(str_time[3:])


def re_calculate(int_time):
    hour, minute = str(int_time // 60), str(int_time % 60)
    if len(hour) < 2:
        hour = '0' + hour
    if len(minute) < 2:
        minute = '0' + minute
    return hour + ':' + minute


def solution(n, t, m, timetable):
    answer = ''
    start_bus, end_bus, c = calculate('09:00'), calculate('09:00') + (n - 1) * t, 0
    timetable = sorted([calculate(t) for t in timetable if calculate(t) <= end_bus])  # 막차 이후는 어차피 못탐

    while c < n - 1:  # 막차 전 까지 모두 탑승
        for i in range(m):
            if i < len(timetable) and timetable[i] <= start_bus:
                timetable.pop(i)
        start_bus += t
        c += 1

    if len(timetable) < m:  # 막차 시간에 대기 사람이 탑승 수 보다 작으면 막차 시간에 가면 됨
        answer = re_calculate(end_bus)
    else:  # 막차 시간에 대기 사람이 탑승 수 보다 많으면 마지막 탑승자 1분 전에 도착 해야함
        answer = re_calculate(timetable[m - 1] - 1)
    return answer


if __name__ == '__main__':
    print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))