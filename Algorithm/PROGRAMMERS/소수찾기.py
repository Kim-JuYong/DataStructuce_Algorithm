import itertools


primes = set()

def isPrime(num):
    global primes
    num = int(num)
    if num in primes or num == 0 or num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    primes.add(num)
    return True

def solution(numbers):
    answer = 0
    for r in range(1, len(numbers) + 1):
        for can in itertools.permutations(numbers, r):
            if isPrime(''.join(can)):
                print(''.join(can))
                answer += 1
    return answer

solution("011")