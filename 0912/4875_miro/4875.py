import sys
sys.stdin = open('input.txt')

def find_s():
    for i in range(N-1, -1, -1):
        for j in range(N):
            if arr[i][j] == 2:
                return i, j

def bfs(si, sj):
    visited = [[0]*N for _ in range(N)]
    q = []
    q.append((si, sj))
    visited[si][sj] = 1
    while q:
        si, sj = q.pop(0)
        visited[si][sj] = 1
        for d in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            ni = si + d[0]
            nj = sj + d[1]
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] != 1 and visited[ni][nj] == 0:
                if arr[ni][nj] == 3:
                    return 1
                q.append((ni, nj))
    # tc 3에서 0이 출력안됨.... -> 왜??? -> visited 안해서 ㅎ
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    # visited = [[0]*N for _ in range(N)]
    s_i, s_j = find_s()
    res = bfs(s_i, s_j)
    print(f'#{tc} {res}')