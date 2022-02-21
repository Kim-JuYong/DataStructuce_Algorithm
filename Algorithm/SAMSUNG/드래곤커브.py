import sys

d_to_p = {0: (0, 1), 1: (-1, 0), 2: (0, -1), 3: (1, 0)}
right = {0: 0, 1: 1, 2: 2, 3: 3}
up = {0: 1, 1: 2, 2: 3, 3: 0}
down = {0: 3, 1: 0, 2: 1, 3: 2}
left = {0: 2, 1: 3, 2: 0, 3: 1}


def change_direction(direction):  # ->를 기준으로 시작 방향이 다르면 어떻게 처리할지
    if direction == 1:
        return up
    if direction == 2:
        return left
    if direction == 3:
        return down
    return right


def dragon_curve():  # 시작 방향 -> 를 기준으로 드래곤 커브
    ret = [[] for i in range(11)]
    ret[0] = [0]
    for i in range(1, 11):
        ret[i] += ret[i - 1]
        for j in range(len(ret[i - 1]) - 1, -1, -1):
            ret[i].append((ret[i][j] + 1) % 4)
    return ret


def square(board):
    ret = 0
    for i in range(100):
        for j in range(100):
            if board[i][j] == board[i + 1][j] == board[i][j + 1] == board[i + 1][j + 1] == 1:
                ret += 1
    return ret


def solution(n, informs):
    answer = 0
    generations = dragon_curve()
    board = [([0] * 101) for i in range(101)]
    for inform in informs:
        direction_map = change_direction(inform[2])
        curve = generations[inform[3]]
        y, x = inform[1], inform[0]
        board[y][x] = 1
        for g in curve:
            dy, dx = map(int, d_to_p[direction_map[g]])
            y += dy
            x += dx
            board[y][x] = 1
    answer = square(board)
    return answer


if __name__ == '__main__':
    n = int(sys.stdin.readline().rstrip())
    informs = [list(map(int, sys.stdin.readline().rstrip().split())) for i in range(n)]
    print(solution(n, informs))
