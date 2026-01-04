inf = 2 ** 63

import bisect 
def lis(l):
    # STEP1: LIS長パート with 使用位置
    n = len(l)
    lisDP = [inf] * n # 通常のLIS用リスト
    indexList = [None] * n # lの[i]文字目が使われた場所を記録する
    for i in range(n):
        # 通常のLISを求め、indexListに使った場所を記録する
        ind = bisect.bisect_left(lisDP, l[i])
        lisDP[ind] = l[i]
        indexList[i] = ind
    # STEP2: LIS復元パート by 元配列の使用した位置
    # 後ろから見ていくので、まずは、LIS長目(targetIndex)のindexListを探したいとする
    targetIndex = max(indexList)
    ans = [0] * (targetIndex + 1) # 復元結果(indexListは0-indexedなのでlen=4ならmax=3で格納されているので+1する)
    # 後ろから見ていく
    for i in range(n - 1, -1, -1):
        # もし、一番最後に出てきているtargetIndexなら
        if indexList[i] == targetIndex:
            ans[targetIndex] = l[i] # ansのtargetIndexを確定
            targetIndex -= 1
    return ans

#print(" ".join(list(map(str, lis([7,8,9,4,5,6,1]))))) # 4 5 6
#print(" ".join(list(map(str, lis([1,2,6,9,5,10]))))) # 1 2 6 9 10

# n = int(input())
# l = list(map(int, input().split()))
# print(" ".join(list(map(str, lis(l)))))
