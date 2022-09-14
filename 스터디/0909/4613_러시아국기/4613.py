import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N행, M열
    flag = [list(input()) for _ in range(N)]
    res = N*M
    # L1(start_idx), L2(end_idx) 무작위로 잡아..
    for s_i in range(1, N-1):
        for e_i in range(s_i+1, N):
            swap = 0
            for w_i in range(s_i):
                for j in range(M):
                    if flag[w_i][j] != 'W':
                        swap += 1
            for b_i in range(s_i, e_i):
                for j in range(M):
                    if flag[b_i][j] != 'B':
                        swap += 1
            for r_i in range(e_i, N):
                for j in range(M):
                    if flag[r_i][j] != 'R':
                        swap += 1
            if swap < res:
                res = swap
    print(f'#{tc} {res}')


