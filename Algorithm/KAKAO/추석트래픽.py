import decimal


def calculate(time1, offset):
    hour, minute, second = map(float, time1.split(':'))
    end = hour * 3600 + minute * 60 + second
    start = float(str(end - float(offset) + 0.001)[:10])
    return start, end


def solution(lines):
    answer = 0
    times = [[0, 0] for i in range(len(lines))]
    change_log = []
    for i in range(len(lines)):
        line = lines[i]
        start, end = calculate(line[11: 24], line[24: len(line) - 1])
        times[i][0], times[i][1] = start, end
        change_log.append(start)
        change_log.append(end)
    ret = 0
    for log in change_log:
        start, end = log, float(decimal.Decimal(str(log)) + decimal.Decimal('0.999'))
        for time in times:
            if time[1] < start or time[0] > end:
                continue
            else:
                ret += 1
        answer = max(ret, answer)
        ret = 0
    return answer


if __name__ == '__main__':
    a = ["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]
    print(solution(a))