# 2798 블랙잭
N, M = map(int, input().split())
cards = sorted(list(map(int, input().split())))

lst = []
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            card_sum = cards[i] + cards[j] + cards[k]
            lst.append(card_sum)
max_sum = lst[0]
for _ in range(1, len(lst)):
    if max_sum < lst[_] <= M:
        max_sum = lst[_]
print(max_sum)