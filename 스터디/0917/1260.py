N, M, V = map(int, input().split())
N = 2
adjlst = [[] for _ in range(N+1)]
print(adjlst)
for _ in range(M):
    a, b = map(int, input().split())
