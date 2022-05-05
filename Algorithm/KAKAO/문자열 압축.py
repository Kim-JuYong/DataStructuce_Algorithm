

def string_zip(sliced_s, i = 0):  #연속된 중복 문자열 세기
    ret = ''
    while i < len(sliced_s):
        j = i + 1
        while j < len(sliced_s) and sliced_s[i] == sliced_s[j]:
            j += 1
        if j > i + 1:
            ret += (str(j - i) + sliced_s[i])
        else:
            ret += sliced_s[i]
        i = j
    return ret
    

def solution(s):   
    answer = 1001
    if len(s) == 1:
        return 1
    for window in range(1, len(s) // 2  + 1):
        sliced_s = [s[i: i+window]for i in range(0, len(s), window)]
        print(sliced_s)
        zip_s = string_zip(sliced_s)
        answer = min(answer, len(zip_s))
    return answer


solution("a")

