from collections import deque


def solution(priorities, location):
    answer = 0
    priolist = []
    wait = deque()
    for idx, prio in enumerate(priorities):
        wait.append((idx, prio))
        priolist.append((idx, prio))
    priolist = sorted(priolist, key=lambda x: x[1])
    while len(wait) != 0:
        first = wait.popleft()
        if first[1] == priolist[-1][1]:
            priolist.pop()
            answer += 1
            if first[0] == location:
                return answer
        else:
            wait.append(first)
    return answer


solution([2, 1, 3, 2], 2)

# solution([1, 1, 9, 1, 1, 1], 0)
