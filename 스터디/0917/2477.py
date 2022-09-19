N = int(input())
dict = {}
for _ in range(1, 7):
    d, l = map(int, input().split())
    if d not in dict.keys():
        dict[d] = [(_, l)]
    else:
        dict[d].append((_, l))
total = 1
for i in range(1, 5):
    if len(dict[i]) == 1:
        total *= dict[i][0][1]
print(dict)
cnt = 0
rest = 1
for k, v in dict.items():
    if len(v) == 2:
        cnt += 1
        if cnt == 1:
            rest *= v[1][1]
        else:
            rest *= v[0][1]
res = total - rest
print(res*N)
