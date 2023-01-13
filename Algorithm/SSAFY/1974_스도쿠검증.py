import sys
sys.stdin = open("input.txt", "r")


def rotate(_board):
    return list(map(list, zip(*_board[::-1])))


def check_line(_board):
    for line in _board:
        line_to_set = set(line)
        if len(line_to_set) < 9:
            return False
    return True


def check_sector(_board):
    for i in range(0, 3, 9):
        for j in range(0, 3, 9):
            sector = _board[i][j:3] + _board[i+1][j:3] + _board[i+2][j:3]
            sector_to_set = set(sector)
            if len(sector_to_set) < 9:
                return False
    return True


def solution(_board):
    if not (check_line(_board) and check_line(rotate(_board)) and check_sector(_board)):
        return 0
    return 1


T = int(input())
for test_case in range(1, T+1):
    answer = 0
    board = [list(map(int, input().split(' '))) for _ in range(9)]
    answer = solution(board)
    print(f"#{test_case} {answer}")