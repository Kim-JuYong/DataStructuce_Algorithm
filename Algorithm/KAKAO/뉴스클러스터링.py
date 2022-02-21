import collections
import math


def have_union_and_intersection(elements1, elements2) -> list:
    union = []
    intersection = []
    e1 = collections.Counter(elements1)
    e2 = collections.Counter(elements2)
    for k, v in e1.items():
        if k in elements2:
            bigger = max(e2[k], v) # 합집합
            union.extend([k for i in range(bigger)])
            smaller = min(e2[k], v)
            intersection.extend([k for i in range(smaller)])
        else:
            union.extend([k for i in range(v)])
    for k, v in e2.items():
        if k not in elements1:
            union.extend([k for i in range(v)])
    return union, intersection


def solution(str1, str2):
    answer = 0
    str1, str2 = str1.upper(), str2.upper()
    elements1 = [str1[i] + str1[i + 1] for i in range(len(str1) - 1) if str1[i].isalpha() and str1[i + 1].isalpha()]
    elements2 = [str2[i] + str2[i + 1] for i in range(len(str2) - 1) if str2[i].isalpha() and str2[i + 1].isalpha()]
    if elements1 == [] and elements2 == []:
        return 65536
    union, intersection = have_union_and_intersection(elements1, elements2)
    answer = math.trunc(len(intersection) / len(union) * 65536) if len(intersection) != 0 else 0
    return answer