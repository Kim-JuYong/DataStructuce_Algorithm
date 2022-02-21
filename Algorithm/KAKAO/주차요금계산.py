import math


def solution(fees, records):
    answer = []
    inform = {r.split()[1]: [] for r in records}
    for r in records:
        inform[r.split()[1]].append(r.split()[0])
    for name, times in sorted(inform.items()):
        if len(times) % 2 == 1:
            inform[name].append("23:59")
        # 시간 계산
        use_time = 0
        for i in range(0, len(times) - 1, 2):
            out_time = int(times[i+1][:2]) * 60 + int(times[i+1][3:])
            in_time = int(times[i][:2]) * 60 + int(times[i][3:])
            use_time += (out_time - in_time)
        # 요금 계산
        fee = fees[1]
        if use_time > fees[0]:
            fee += math.ceil((use_time - fees[0]) / float(fees[2])) * fees[3]
        answer.append(fee)

    return answer


if __name__ == '__main__':
    solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])