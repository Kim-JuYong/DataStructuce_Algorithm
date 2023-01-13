import sys
sys.stdin = open("input.txt", "r")

import collections


dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]


def solution(_board):
    start_y, start_x = map(int, [[i, j] for i in range(16) for j in range(16) if _board[i][j] == 2][0])
    dest_y, dest_x = map(int, [[i, j] for i in range(16) for j in range(16) if _board[i][j] == 3][0])

    queue = collections.deque()
    queue.append([start_y, start_x])
    visit = [[0] * 16 for _ in range(16)]
    visit[start_y][start_x] = 1

    while len(queue) != 0:
        cur_y, cur_x = map(int, queue.popleft())

        for i in range(4):
            next_y, next_x = cur_y + dy[i], cur_x + dx[i]
            if -1 < next_y < 16 and -1 < next_x < 16:
                if _board[next_y][next_x] != 1 and visit[next_y][next_x] == 0:
                    if _board[next_y][next_x] == 3:
                        return 1
                    queue.append([next_y, next_x])
                    visit[next_y][next_x] = 1

    return 0


T = 10
for test_case in range(1, T+1):
    answer = 0
    test_case = int(input())
    board = [list(map(int, input())) for _ in range(16)]
    answer = solution(board)
    print(f"#{test_case} {answer}")