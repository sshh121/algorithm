import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    words = list(input())
    max_len = 1
    while max_len < 10:
        for i in range(max_len):
            if words[i] != words[i+max_len]:
                max_len += 1
                break
        else:
            break
    print(f'#{tc} {max_len}')