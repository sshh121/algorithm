lst = [0]*1001
lst[1] = 1
lst[2] = 2
for i in range(3, 1001):
    lst[i] = lst[i-1]+lst[i-2]
print(lst[int(input())]%10007)
