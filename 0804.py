N = input()
lst = []
for i in N:
    lst.append(i)


while lst[-1]!=N:
    new = 0
    for num in lst[len(lst)-2:len(lst)]:
        if len(num)==1: #한자리 숫자면 바로 더함
            new += int(num)
        else:
            new +=int(num[-1])
            
    lst.append(str(new))


# -----------

h, m = map(int, input().split())

if m-45 <0:
    if h == 0:
        h=23
    else:
        h=h-1
    m=60-abs(m-45)
else:
    m -= 45
print(h,m)


#15552
import sys
sentence = sys.stdin.readline().rstrip()
print(sentence)

#10871
a = list(map(int, input().split()))
print(a)


# 10818
import sys

N = int(input())
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()
print(numbers[0], numbers[-1])


#2562
lst = []
for i in range(9):
    n = int(input())
    lst.append(n)
max_num = sorted(lst)[-1]
print(max_num)
print(lst.index(max_num)+1)