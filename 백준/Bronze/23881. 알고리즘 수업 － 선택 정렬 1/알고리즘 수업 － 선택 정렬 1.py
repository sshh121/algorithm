N, K = map(int, input().split())
arr = list(map(int, input().split()))

def selection_sort(arr):
    cnt = 0
    for i in range(N-1, 0, -1):
        maxIdx = i
        for j in range(i-1, -1, -1):
            if arr[maxIdx] < arr[j]:
                maxIdx = j
        if i != maxIdx:
            arr[i], arr[maxIdx] = arr[maxIdx], arr[i]
            cnt += 1
            if cnt == K:
                print(arr[maxIdx], arr[i])
                break
    else:
        print(-1)

selection_sort(arr)