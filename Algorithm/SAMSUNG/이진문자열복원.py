import sys
import itertools

sys.stdin = open(
    "/Users/juyong/Desktop/DataStructure_Algorithm/Algorithm/SAMSUNG/input.txt", "r")

str_dict = {'00': 0, '01': 0, '10': 0, '11': 0}

def check(_n, _str):
    global str_dict
    check_dict = {'00': 0, '01': 0, '10': 0, '11': 0}
    for i in range(_n-1):
        part = _str[i] + _str[i+1]
        check_dict[part] += 1
        if check_dict[part] > str_dict[part]:
            return False
    if check_dict == str_dict:
        return True
    return False


def solution(_n):
    for s in itertools.product("01", repeat=_n):
        if check(_n, s):
            return ''.join(s)
    return "impossible"



T = int(input())

for test_case in range(1, T+1):
    line = list(map(int, input().split()))
    n = sum(line) + 1
    str_dict['00'], str_dict['01'], str_dict['10'], str_dict['11'] = line[0], line[1], line[2], line[3]
    print(f"#{test_case}", solution(n))