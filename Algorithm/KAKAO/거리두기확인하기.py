

dy, dx = [1, 0, -1, 0], [0, -1, 0, 1]


def bfs(_n: int, _m: int, _y: int, _x: int,  _place: list) -> int:
    q = [(_y, _x)]
    d = [[0] * 5 for i in range(5)]
    visit = [[0] * 5 for i in range(5)]
    visit[_y][_x] = 1
    while len(q) != 0:
        y, x = q[0][0], q[0][1]
        q.pop(0)
        for i in range(4):
            next_y, next_x = y + dy[i], x + dx[i]
            if -1 < next_y < _n and -1 < next_x < _m and visit[next_y][next_x] == 0 and _place[next_y][next_x] != 'X':
                if _place[next_y][next_x] == 'P' and d[y][x] + 1 <= 2:
                    return 0
                q.insert(0, (next_y, next_x))
                d[next_y][next_x] = d[y][x] + 1
                visit[next_y][next_x] = 1
    return 1


def solution(places: list) -> int:
    answer = [1 for i in range(5)]
    c = 0
    for place in places:
        persons = [(i, j) for i in range(5) for j in range(5) if place[i][j] == 'P']
        for person in persons:
            if not bfs(5, 5, person[0], person[1], place):
                answer[c] = 0
        c += 1
    return answer


if __name__ == '__main__':
    print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
