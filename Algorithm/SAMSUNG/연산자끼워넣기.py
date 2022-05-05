
N = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))


def permutation(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        for n in permutation(arr[:i] + arr[i+1:], r-1):
            yield [arr[i]] + n


def solution():
    operator, min_ret, max_ret = [], float('inf'), float('-inf')
    for i in range(4):
        if operators[i] != 0:
            for j in range(operators[i]):
                operator.append(i)
    for can in permutation(operator, len(operator)):
        num = numbers[0]
        for i in range(N-1):
            if can[i] == 0:
                num += numbers[i+1]
            if can[i] == 1:
                num -= numbers[i+1]
            if can[i] == 2:
                num *= numbers[i+1]
            if can[i] == 3:
                num = int(num / numbers[i+1])
        min_ret = min(min_ret, num)
        max_ret = max(max_ret, num)

    print(max_ret)
    print(min_ret)


solution()