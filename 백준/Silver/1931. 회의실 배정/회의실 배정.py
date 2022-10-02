N = int(input())
meeting = []
for _ in range(N):
    meeting.append(list(map(int, input().split())))
# 회의 종료 시간 기준으로 정렬
meeting.sort()
meeting.sort(key=lambda x:x[1])
# print(meeting)
cnt = 1
i = 0
while i < N-1:
    for j in range(i+1, N):
        # 이전 회의 종료 시간이 다음 회의 시작 시간보다 빠르거나 같을 때
        if meeting[i][1] <= meeting[j][0]:
            cnt += 1
            i = j
            break
    else:
        break

print(cnt)