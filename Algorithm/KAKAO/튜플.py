import collections


def solution(s):
    answer = []
    d, num = collections.defaultdict(int), ''
    for i in range(len(s)):
        if s[i].isdigit():
            num += s[i]
        if len(num) > 0 and s[i] in [',', '}']:
            d[num] += 1
            num = ''
    d = sorted(d.items(), key=lambda x: -x[1])
    answer = [int(i[0]) for i in d]
    return answer

solution("{{20,111},{111}}")