
def solution(phone_book):
    n = len(phone_book)
    phone_book.sort()
    for i in range(n-1):
        # print(phone_book[i], phone_book[i+1][:len(phone_book[i])])
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False
    return True

phone_book = ["97674223", "1195524421", "110", "120", "1191", "30876", "9999"]
# phone_book.sort()
# print(phone_book)
print(solution(phone_book))

'''
# tc는 다 맞는데, 효율성 검사에서 2 fail.. (시간초과)
def solution(phone_book):
    n = len(phone_book)
    phone_book.sort(key=len)
    for i in range(n-1):
        for j in range(i+1, n): # 비교 대상
            if len(phone_book[i]) == len(phone_book[j]):
                continue
            if phone_book[i] == phone_book[j][:len(phone_book[i])]:
                return False
    else:
        return True
'''

'''
# 마찬가지로 효율성검사 2개 fail
def solution(phone_book):
    n = len(phone_book)
    phone_book.sort(key=len)
    for i in range(n-1):
        for j in range(i+1, n): # 비교 대상
            if len(phone_book[i]) == len(phone_book[j]):
                continue
            for k in range(len(phone_book[i])):
                if phone_book[i][k] != phone_book[j][k]:
                    break
            else:
                return False
    else:
        return True
'''