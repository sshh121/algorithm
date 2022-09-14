import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    cnt = [0]*1001 # 누적합
    res = 0
    arr = list(map(int, input()))
    for idx in range(len(arr)):
        cnt[idx+1] = cnt[idx] + arr[idx]
        if cnt[idx+1] < (idx+1):
            res += (idx+1-cnt[idx+1])
            cnt[idx+1] = idx+1
    print(f'#{tc} {res}')
