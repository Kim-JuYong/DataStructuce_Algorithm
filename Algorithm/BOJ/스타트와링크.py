import itertools


n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

def ability(team: list) -> int:
    ret, m = 0, len(team)
    for i in range(m-1):
        for j in range(i, m):
            ret += s[team[i]][team[j]]
            ret += s[team[j]][team[i]]
    return ret

def solution():
    answer = float('inf')
    for start in itertools.combinations(range(n), n//2):
        start_ret = ability(list(start))
        link = [l for l in range(n) if l not in list(start)]
        link_ret = ability(list(link))
        answer = min(answer, abs(start_ret - link_ret))
    print(answer)

solution()