N = int(input())
plan = []
for _ in range(N):
    s, e = map(int, input().split())
    plan.append((s, e))
plan.sort()
plan.sort(key=lambda x:x[1]) # 종료시간 기준 정렬

now_end = 0
cnt = 0
for s, e in plan:
    # 이전의 종료시간보다는 크거나 같아야됨
    if s >= now_end:
        cnt += 1
        now_end = e
print(cnt)