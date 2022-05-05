

def solution(id_list, report, k):
    answer = []
    count_report = {i : 0 for i in id_list}     #(유저 이름: 신고 당한 횟수)
    who_report = {i : set() for i in id_list}   #(이용자 유저 이름: 신고한 유저 이름 목록)
    stop_id = set()     # 금지 당한 아이디 목록
    for rep in report:
        user_id, report_id = map(str, rep.split())
        temp = len(who_report[user_id])
        who_report[user_id].add(report_id)
        if temp != len(who_report[user_id]):    # 신고한 유저 이름 목록의 길이에 변화가 없다 -> 중복됐다.
            count_report[report_id] += 1 
            if count_report[report_id] >= k:
                stop_id.add(report_id)
    for user_id, report_id in who_report.items():
        answer.append(len(report_id & stop_id))

    return answer


solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2)
