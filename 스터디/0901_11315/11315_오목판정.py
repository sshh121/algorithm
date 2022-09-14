import sys
sys.stdin = open('input.txt')

def five(arr):
    # 가로, 세로
    for i in range(N):
        cnt_r, cnt_c = 0, 0
        for j in range(N):
            if arr[i][j] == 'o':
                cnt_r += 1
                if cnt_r == 5:
                    return True
            else:
                cnt_r = 0

            if arr[j][i] == 'o':
                cnt_c += 1
                if cnt_c == 5:
                    return True
            else:
                cnt_c = 0
    else: # 가로 세로 안나오면 대각선
        # 대각선 정방향
        cnt_diag = 0
        for j in range(N-4):
            i = 0
            while j < N:
                if arr[i][j] == 'o':
                    cnt_diag += 1
                    if cnt_diag == 5:
                        return True
                else:
                    cnt_diag = 0
                i += 1
                j += 1
        else:
            if N > 5:
                for i in range(1, N-4):
                    j = 0
                    while i < N:
                        if arr[i][j] == 'o':
                            cnt_diag += 1
                            if cnt_diag == 5:
                                return True
                        else:
                            cnt_diag = 0
                        i += 1
                        j += 1
        # 대각선 역방향
        cnt_diag_r = 0
        for j in range(N-1, 3, -1):
            i = 0
            while j >= 0:
                if arr[i][j] == 'o':
                    cnt_diag_r += 1
                    if cnt_diag_r == 5:
                        return True
                else:
                    cnt_diag_r = 0
                i += 1
                j -= 1
        else:
            if N > 5:
                for i in range(1, N-4):
                    j = N-1
                    while i < N:
                        if arr[i][j] == 'o':
                            cnt_diag_r += 1
                            if cnt_diag_r == 5:
                                return True
                        else:
                            cnt_diag_r = 0
                        i += 1
                        j -= 1


        '''
        if N == 5:
            for i in range(N):
                if arr[i][i] == 'o':
                    cnt_diag += 1
                    if cnt_diag == 5:
                        return True
                else:
                    cnt_diag = 0
    
                if arr[i][N-1-i] == 'o':
                    cnt_diag_reverse += 1
                    if cnt_diag_reverse == 5:
                        return True
                else:
                    cnt_diag_reverse = 0
        else:
            for _ range(N-5):
            
            
        '''



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    # 가로 확인
    # 세로 확인
    # 대각선 확인 (X 형태)
    print(f'#{tc}', end=' ')
    if five(arr):
        print('YES')
    else:
        print('NO')