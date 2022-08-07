# 8958번
import sys
N = int(input())

scores_list = []
for i in range(N):
    problem = sys.stdin.readline().rstrip()
    scores = 0
    score = 0
    for j in range(len(problem)):
        if problem[j] == 'O':
            score += 1
        else:
            score = 0 #X이면 score 초기화
        scores += score
    scores_list.append(scores)

for _ in range(N):
    print(scores_list[_])


# import sys
# problem = sys.stdin.readline().rstrip() #!!!!!!!!!!
# scores = 0
# score = 0
# scores_list = []

# for j in range(len(problem)):
#     print(j)
#     if problem[j] == 'O':
#         score += 1
#         print(j, score)
#     else:
#         score = 0 #X이면 score 초기화
#         print(j, score)
#     scores += score
# scores_list.append(scores)




# problem = 'OOXXOXXOOO'
# print(len(problem))
# print(list(range(len(problem))))