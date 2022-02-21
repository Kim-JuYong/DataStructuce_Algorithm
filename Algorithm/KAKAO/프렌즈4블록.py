import copy


def crush_block(m, n, board):
    temp = [[board[i][j] for j in range(n)] for i in range(m)]
    flag = False
    for i in range(m - 1):
        for j in range(n - 1):
            if board[i][j] != '-':
                if board[i][j] == board[i + 1][j] == board[i][j + 1] == board[i + 1][j + 1]:
                    temp[i][j], temp[i + 1][j], temp[i + 1][j + 1], temp[i][j + 1] = '-', '-', '-', '-'
                    flag = True
    if flag:  # 깨질게 있었다.
        return [True, temp]
    return [False, temp]


def down_block(m, n, board):
    temp = [[board[i][j] for i in range(m - 1, -1, -1)] for j in range(n)]
    for line in temp:
        while '-' in line:
            line.remove('-')
        for i in range(m - len(line)):
            line.append('-')
    temp = [[temp[i][j] for i in range(n)] for j in range(m - 1, -1, -1)]
    return temp


def solution(m, n, board):
    answer = 0
    while True:
        ret = crush_block(m, n, board)
        if not ret[0]:
            break
        board = ret[1]
        board = down_block(m, n, board)
    answer = len([1 for i in range(m) for j in range(n) if board[i][j] == '-'])
    return answer


if __name__ == '__main__':
    print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
