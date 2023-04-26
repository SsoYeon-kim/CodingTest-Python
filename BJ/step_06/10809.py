# s = list(map(str, input()))

# for i in range(ord('a'), ord('z')+1):
#     for j in s:
#         ans = -1
#         if chr(i) == j:
#             ans = s.index(j)
#             break
#     print(ans, end=' ')


word = input()
alphabet = list(range(ord('a'),ord('z')+1))
for x in alphabet :
    print(word.find(chr(x))) 