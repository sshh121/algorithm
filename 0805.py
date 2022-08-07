#2577
num_product = 1
for n in range(3):
    num = int(input())
    num_product *= num

for i in range(10):
    result = 0
    for j in list(str(num_product)):
        if str(i)==j:
            result += 1
    print(result)
'''


#3052
number = []
for i in range(10):
    num = int(input())
    if num%42 not in number:
        number.append(num%42)
print(len(number))

#1546
import sys
N = int(input())
nums = list(map(int, sys.stdin.readline().split()))
total = 0
for i in nums:
    total += i/max(nums)*100
print(total/N)

'''