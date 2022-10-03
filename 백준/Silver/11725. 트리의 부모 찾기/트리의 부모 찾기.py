N = int(input())
adjLst = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    adjLst[a].append(b)
    adjLst[b].append(a)

par = [0] * (N+1)
q = [1]
visited = [0] * (N+1)
visited[1] = 1
while q:
    n = q.pop(0)
    for w in adjLst[n]:
        if not visited[w]:
            visited[w] = 1
            par[w] = n
            q.append(w)
for i in range(2, N+1):
    print(par[i])