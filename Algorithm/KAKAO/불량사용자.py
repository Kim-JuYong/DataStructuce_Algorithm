def translate(sounds):
    ret = ""
    for i in range(len(sounds) - 1):
        if sounds[i] == "#":
            continue
        if sounds[i+1] != "#":
            ret += sounds[i]
            continue
        ret += sounds[i].lower()
    if sounds[-1] != "#":
        ret += sounds[-1]
    return ret


def getTime(time):
    hh, mm = map(int, time.split(":"))
    return hh * 60 + mm


def playMusic(start, end, sounds):
    playTime = getTime(end) - getTime(start)
    soundsTime = len(sounds)
    sounds = sounds * (playTime // soundsTime) + sounds[:playTime % soundsTime]
    return sounds
    

def solution(m, musicinfos):
    answer = "(None)"
    m = translate(m)
    ret = []
    for idx, var in enumerate(musicinfos):
        start, end, title, sounds = map(str, var.split(","))
        sounds = translate(sounds)
        sounds = playMusic(start, end, sounds)
        if m in sounds:
            playTime = getTime(end) - getTime(start)
            ret.append([playTime, idx, title])
    if len(ret) == 0:
        return answer
    ret.sort(key=lambda x:(-x[0], x[1]))
    answer = ret[0][2]
    return answer