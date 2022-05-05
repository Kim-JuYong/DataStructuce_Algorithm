def solution(record):
    answer = []
    record = [r.split() for r in record]
    id_record = {r[1] : '' for r in record}
    for r in record:
        if r[0] == "Enter" or r[0] == "Change":
            id_record[r[1]] = r[2]

    for r in record:
        if r[0] == "Enter":
            answer.append(id_record[r[1]] + "님이 들어왔습니다." )
        elif r[0] == "Leave":
            answer.append(id_record[r[1]] + "님이 나갔습니다.")
    
    return answer

solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])