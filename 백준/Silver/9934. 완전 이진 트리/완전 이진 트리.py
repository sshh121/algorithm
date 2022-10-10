def inorder(n):
    global cnt
    if n < 2**K:
        inorder(n*2)
        cnt += 1
        tree[n] = buildings[cnt]
        inorder(n*2+1)

K = int(input())
buildings = list(map(int, input().split()))
tree = [0] * (2**K)
cnt = -1
inorder(1)
for k in range(K):
    print(*tree[2**k:2**(k+1)])