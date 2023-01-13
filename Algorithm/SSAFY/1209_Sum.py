import sys

sys.stdin = open("input.txt", "r")


def rotate(_board):
    return list(map(list, zip(*_board[::-1])))


def sum_line(_board):
    ret = 0
    for line in _board:
        ret = max(ret, sum(line))
    return ret


def sum_cross(_board, start_x, dest_x, dx):
    ret, y = 0, 0

    for i in range(start_x, dest_x, dx):
        ret += _board[y][i]
        y += 1
    return ret


def solution(_board):
    cross_ret = max(sum_cross(_board, 0, 100, 1), sum_cross(_board, 99, -1, -1))
    line_ret = max(sum_line(_board), sum_line(rotate(_board)))
    return max(cross_ret, line_ret)


T = 10
for test_case in range(1, T + 1):
    answer = 0
    test_case = int(input())
    board = [list(map(int, input().split())) for _ in range(100)]
    answer = solution(board)
    print(f"#{test_case} {answer}")
