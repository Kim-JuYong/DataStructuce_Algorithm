import sys
sys.stdin = open("input.txt", "r")

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]


def solution(_board, _n):

    pass


T = int(input())
for test_case in range(1, T+1):
    answer = 0
    n = int(input())
    board = [list(map(int, list(input()))) for _ in range(n)]
    solution(board, n)
    print(f"#{test_case} {answer}")