import sys
sys.stdin = open("input.txt", "r")


import collections


def solution(_scores):
    counter = collections.Counter(_scores)
    ret = [[item[0], item[1]] for item in counter.items()]
    ret = sorted(ret, key=lambda x: (-x[1], -x[0]))
    return ret[0][0]


T = int(input())
for test_case in range(1, T+1):
    answer = 0
    test_case = int(input())
    scores = list(map(int, input().split()))
    answer = solution(scores)
    print(f"#{test_case} {answer}")