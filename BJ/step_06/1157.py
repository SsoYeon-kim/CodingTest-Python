# sentence = input()
# word = set()
# word.update(sentence.upper())
# dic = dict()

# for w in word:
#     cnt = 0
#     for s in sentence.upper():
#         if w == s:
#             cnt += 1
#         dic[w] = cnt

# max_key = max(dic, key=dic.get)

# count = 0
# for i in dic.values():
#     if i == max(dic.values()):
#         count += 1

# if count == 1:
#     print(max_key)
# else:
#     print('?')

word = input().upper()
word_list = list(set(word))

cnt = []
for i in word_list:
    count = word.count(i)
    cnt.append(count)

if cnt.count(max(cnt)) > 1:
    print('?')
else:
    print(word_list[cnt.index(max(cnt))])