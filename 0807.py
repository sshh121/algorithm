#3003
chess = list(map(int, input().split()))
original = [1, 1, 2, 2, 2, 8]
for i in range(6):
    print(original[i]-chess[i], end=' ')

#1110 ;;;
N = input()
lst = []
if int(N) < 10:
    N ='0'+N

new_num = N[1]+str(int(N[0])+int(N[1]))[-1]
cycle_len = 1
while True:
    if new_num == N: #새로운 숫자가 N과 동일한지 판별 먼저!
        print(cycle_len)
        break
    else:
        new_num = new_num[1]+str(int(new_num[0])+int(new_num[1]))[-1]
        cycle_len += 1

#25304
total_price = int(input())
N = int(input())
self_sum = 0

for i in range(N):
    lst = list(map(int, input().split()))
    self_sum += lst[0]*lst[1]

if self_sum == total_price:
    print('Yes')
else:
    print('No')

#4344
import sys

C = int(input())
for tc in range(C):
    N_scores = list(map(int, sys.stdin.readline().rstrip().split()))
    avg = sum(N_scores[1:])/N_scores[0]
    top = 0
    for score in N_scores[1:]:
        if score > avg:
            top += 1
    print('%.3f%%' %(top/N_scores[0]*100)) #%를 출력하기 위해서는 %% 두번 사용 (포매팅 구분자와 구별하기 위해)
    # print('{:.3f}%'.format(top/N_scores[0]*100))으로도 출력 가능
