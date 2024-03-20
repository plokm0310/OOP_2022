from random import *

def fill(N, M):
#    a = [[] * M] * N
#    ad = [1]
#    for i in range(1, M):
#        ad.append(randint(ad[i - 1] + 1, ad[i - 1] + 11))
#    a[0] = ad
#    for i in range(1, N):
#        ad = [randint(a[i - 1][0] + 1, a[i - 1][0]+11)]
#        for j in range(1, M):
#            ad.append(randint(max(a[i-1][j], ad[j-1]) + 1, max(a[i-1][j], ad[j-1])+11))
#        a[i] = ad
    a = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
    return a
                
def fnd(lst, K):
    ans, cnt = False, 0
    i, j = 0, m - 1
    down, left = True, True
    while lst[i][j] != K:
        if i == n:
            down = False
        if j == 0:
            left = False
        if (lst[i][j] > K and left == True):
            j -= 1
            cnt += 1
        elif (lst[i][j] < K and down == True):
            i += 1
            cnt += 1
        else:
            break
    else:
        ans = True
    print(ans, cnt)
    for i in range(n):
        for j in range(m):
            print(" " * (3 - len(str(lst[i][j]))), lst[i][j], end = "")
        print()

n, m, k = map(int, input().split())
fnd(fill(n, m), k)
