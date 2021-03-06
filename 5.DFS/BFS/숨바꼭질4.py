from collections import deque

n, K = map(int, input().split())
q = deque()
move = [0] * 100001  # move λ°°μ΄ π move[νμ¬λΈλ] = μ΄μ  λΈλ (=λΆλͺ¨λΈλ)
dist = [0] * 100001  # dist λ°°μ΄ π dist[νμ¬ λΈλ] = κ±Έλ¦¬λ μκ°(μ΄)
q.append(n)


def path(x):
    arr = []
    temp = x
    for _ in range(dist[x] + 1):
        arr.append(temp)
        temp = move[temp]
    print(" ".join(map(str, arr[::-1])))


def bfs():
    while q:
        x = q.popleft()
        if x == K:
            print(dist[x])
            path(x)
            return x
        for i in (x - 1, x + 1, x * 2):
            if 0 <= i <= 100000 and dist[i] == 0:
                q.append(i)
                dist[i] = dist[x] + 1
                move[i] = x


bfs()
