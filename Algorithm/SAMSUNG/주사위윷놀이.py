import collections


def product(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for n in product(arr, r-1):
                yield [arr[i]] + n


def make_board():
    board = collections.defaultdict(list)
    for i in range(0, 40, 2):
        board[i].append(('r', i+2))
    for i in range(13, 18, 3):
        board[i].append(('b', i+3))
    for i in range(28, 25, -1):
        board[i].append(('b', i-1))
    for i in range(25, 40, 5):
        board[i].append(('b', i+5))
    board[10].append(('b', 13))
    board[20].append(('b', 22))
    board[30].append(('b', 28))
    board[19].append(('b', 25))
    board[22].append(('b', 25))
    board[24].append(('b', 25))
    print(board)
    return board


def solution(_dice):
    board = make_board()
    horses = [('r', 0), ('r', 0), ('r', 0), ('r', 0)]
    ret = 0
    for test_case in product([0, 1, 2, 3], 10):
        for i, t in enumerate(test_case):
            move, horse, score, flag = _dice[i], horses[t], 0, False
            for j in range(move):
                horses[t] = board[horses[t][1]][-1]
                if horses[t] in horses[:t] + horses[t+1:]:
                    if horses[t][1] != 40:
                        flag = True
                        break
                score += horses[t][1]
            if flag:
                break
            ret = max(ret, score)

    print(ret)


dice = list(map(int, input().split()))
solution(dice)