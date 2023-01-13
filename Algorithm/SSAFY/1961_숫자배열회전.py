import sys
sys.stdin = open("input.txt", "r")


def rotate(_board):
    return list(map(list, zip(*_board[::-1])))


def to_string(_list):
    return ''.join(_list) + " "


def solution(_board, _n):
    ret = ""
    board_list = []
    for i in range(3):
        _board = rotate(_board)
        board_list.append(_board)

    for i in range(_n):
        line = to_string(board_list[0][i]) + to_string(board_list[1][i]) + to_string(board_list[2][i])
        if i < _n - 1:
            line += '\n'
        ret += line
    return ret


T = int(input())
for test_case in range(1, T+1):
    answer = ""
    n = int(input())
    board = [list(input().split()) for _ in range(n)]
    print(f"#{test_case}")
    print(solution(board, n))
