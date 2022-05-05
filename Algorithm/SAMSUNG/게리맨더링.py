import copy

n = int(input())
people = list(map(int, input().split()))
adj_list = [[0]*11 for _ in range(11)]
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(1, line[0] + 1):
        adj_list[i+1][line[j]] = 1


def dfs(nodes, start):
    visit = [0] * 11
    for no in nodes:
        visit[no] = 1
    stack = [start]
    nodes = set()
    while stack:
        cur = stack.pop()

        visit[cur] = 1
        nodes.add(cur)

        for i in range(1, n + 1):
            if adj_list[cur][i] == 1 and visit[i] == 0:
                stack.append(i)
    return nodes


def combination(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        for ne in combination(arr[i+1:], r - 1):
            yield [arr[i]] + ne


def solution():
    ret = float('inf')
    for r in range(1, n // 2 + 1):
        for can in combination(range(1, n+1), r):
            start_nodes = list(set(range(1, n+1)) - set(can))
            visit1 = dfs(can, start_nodes[0])
            people1 = sum([people[v-1] for v in visit1])
            visit2 = dfs(start_nodes, can[0])
            people2 = sum([people[v-1] for v in visit2])
            if set(visit1) | set(visit2) == set(range(1, n+1)):
                ret = min(ret, abs(people1 - people2))
    if ret == float('inf'):
        print(-1)
    else:
        print(ret)


solution()