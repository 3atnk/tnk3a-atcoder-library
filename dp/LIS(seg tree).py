N = int(input())
seq = list(map(int,input().split()))

from atcoder.segtree import SegTree

INF = 1 << 63

def op(ele1, ele2):
    return max(ele1, ele2)

e = 0
id_ = 0

# TODO (初期リストlst)
lst = [0] * N
seg = SegTree(op, e, [0] * N)

sortseq = []
for i in range(N):
    sortseq.append((seq[i],-i))
#同率の場合は、indexが後の方から処理する。 
#広義単調増加の場合は、前の方から処理する

sortseq.sort()

for i in range(N):
    Ai = sortseq[i][0]
    idx = -sortseq[i][1]
    tmp = seg.prod(0,idx)
    seg.set(idx,tmp+1)

print(seg.prod(0,N))
