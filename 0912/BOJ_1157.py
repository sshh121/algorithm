word = input().upper()
dict_cnt = {}
for alpha in word:
    if alpha not in dict_cnt.keys():
        dict_cnt[alpha] = 1
    else:
        dict_cnt[alpha] += 1
lst = []
max(dict_cnt.values())
for k, v in dict_cnt.items():
    if v == max(dict_cnt.values()):
        if len(lst) == 0:
            lst.append(k)
        else:
            print('?')
            break
else:
    print(*lst)