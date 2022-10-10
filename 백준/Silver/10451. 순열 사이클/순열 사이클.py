T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    visited = [0] * (N+1)
    adjL = [[] for _ in range(N+1)]
    for i in range(1, N+1):
        if i != nums[i-1] and (nums[i-1] not in adjL[i]):
            adjL[i].append(nums[i-1])
            adjL[nums[i-1]].append(i)
    # print(adjL)
    cnt = 0
    # dfs
    for i in range(1, N+1):
        if visited[i]:
            continue
        stack = [i]
        visited[i] = 1
        while stack:
            v = stack.pop()
            for w in adjL[v]:
                if not visited[w]:
                    visited[w] = 1
                    stack.append(w)
        cnt += 1
    print(cnt)