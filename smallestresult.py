#  moj 1., nije dobar za iste brojeve:
# def smallestresult(n):
#     p = 0
#     result = sum(n[0])
#     for e in range(1, len(n)):
#         result = result + min(n[e][p], n[e][p + 1])
#         p = n[e].index(min(n[e][p], n[e][p + 1]))
#     return result

#  moj 2., nije dobar:
# def minimalresult(n):
#     p = 0
#     k = 0
#     result = sum(n[0])
#     for e in range(1, len(n)):
#         if e <= k:
#             continue
#         if n[e][p] == n[e][p + 1]:
#             result = result + min(n[e][p], n[e][p + 1])
#             k = k + e
#             if e < len(n) - 1:
#                 p = n[e + 1].index(min(n[e + 1][p], n[e + 1][p + 1], n[e + 1][p + 2]))
#                 if p == len(n[e]):
#                     p = p - 1
#                 continue
#         else:
#             result = result + min(n[e][p], n[e][p + 1])
#             p = n[e].index(min(n[e][p], n[e][p + 1]))
#     return result

# kumova ideja:
def minimalresult(n):
    p = 0
    e = len(n) - 1
    while e > 0:
        while p < len(n[e]) - 1:
            n[e - 1][p] = (min(n[e-1][p] + n[e][p], n[e-1][p] + n[e][p + 1]))
            p = p + 1
        e = e - 1
        p = 0
    return sum(n[0])




list = [[4], [8, 7], [5, 6, 6], [3, 9, 4, 1], [18, 2, 6, 4, 9]]
print(minimalresult(list))
list1 = [[53], [3, 2], [1, 7, 8], [2, 5, 8, 27], [14, 17, 33, 4, 2]]
print(minimalresult(list1))
list2 = [[53], [3, 24], [1, 7, 4], [2, 5, 8, 27], [14, 17, 33, 4, 2]]
print(minimalresult(list2))
list3 = [[7], [4, 2], [2, 4, 4], [6, 2, 1, 1], [9, 3, 8, 8, 2]]
print(minimalresult(list3))
list4 = [[5], [4, 4], [3, 3, 3], [2, 2, 2, 2], [1, 1, 1, 1, 1], [9, 9, 9, 9, 9, 1]]
print(minimalresult(list4))


