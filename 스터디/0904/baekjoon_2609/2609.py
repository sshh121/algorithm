a, b = map(int, input().split())

n = 1
max_lst = []
# 최대 공약수
while n <= a:
    if a % n == 0:
        max_lst.append(n)
    n += 1

for idx in range(len(max_lst)-1, -1, -1):
    if b % max_lst[idx] == 0:
        print(max_lst[idx])
        break

i = 1
# 최소 공배수
while True:
    min_num = i * a
    if min_num % b == 0:
        print(min_num)
        break
    i += 1

