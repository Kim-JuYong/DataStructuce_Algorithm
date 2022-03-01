def solution(s):
    answer = 0
    alpha_num = {'zero': 0, 'one': 1, 'two': 2, 'three': 2, 'four': 4,
                 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    alpha = list(alpha_num.keys())
    temp = ''
    start, end = 0, 1
    while start < len(s):
        cur_s = s[start: end]
        print(cur_s)
        if cur_s.isdigit():
            temp += str(cur_s)
            start += 1
            end += 1
        elif cur_s in alpha:
            temp += str(alpha_num[cur_s])
            start = end
            end = start
        else:
            end += 1
    print(temp)
    answer = temp
    return answer

solution("2three45sixseven")