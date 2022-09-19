def preorder(v):
    if v != '.':
        print(v, end='')
        preorder(dict[v][0])
        preorder(dict[v][1])

def inorder(v):
    if v != '.':
        inorder(dict[v][0])
        print(v, end='')
        inorder(dict[v][1])

def postorder(v):
    if v != '.':
        postorder(dict[v][0])
        postorder(dict[v][1])
        print(v, end='')

N = int(input())
dict = {}
for _ in range(N):
    V, L, R = input().split()
    dict[V] = [L, R]
preorder('A')
print()
inorder('A')
print()
postorder('A')


# ch1 = [0] * (N+1)
# ch2 = [0] * (N+1)
# tree = [0] * (N+1)
# for n in range(1, N+1):
#     V, L, R = input().split()
#     tree[n] = V
#     # 인덱스 저장
#     ch1[n] = 2*n
#     ch2[n] = 2*n+1
# preorder(1)