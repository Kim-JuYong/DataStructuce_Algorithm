

from bisect import bisect, bisect_left, bisect_right
import collections
from copy import copy
from itertools import combinations

def make_query(q):  #query문 생성
    while 'and' in q:   
        q.remove('and')
    return q


def make_key(info): #언어 + 직군 + 경력 + 소울푸드를 key로, value에는 해당 key를 가지는 점수 저장
    ret = collections.defaultdict(list)

    for i in info:
        ret[i[0] + i[1] + i[2] + i[3]].append(int(i[4]))    #정보 그대로 key, value 생성
        for n in range(1, 5):   # query가 '-'인 상황을 고려하여 정보에 '-'가 포함될 수 있는 모든 경우를 key로 생성
            for c in combinations([0, 1, 2 ,3], n):
                temp = i[:4]
                for k in c:
                    temp[k] = '-'
                key = ''.join(temp)
                ret[key].append(int(i[4]))        
    return ret


def solution(info, query):
    answer = []
    info = sorted([i.split() for i in info], key=lambda x: int(x[4]))   # 점수 순으로 오름차순 정렬
    info_dict = make_key(info)
    for q in query:
        q = make_query(q.split())
        key = q[0] + q[1] + q[2] + q[3]
        scores = info_dict[key] 
        answer.append(len(scores) - bisect_left(scores, int(q[4]))) # 이진 탐색을 통해 조건을 만족하는 점수가 몇 개 인지 확인

    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))