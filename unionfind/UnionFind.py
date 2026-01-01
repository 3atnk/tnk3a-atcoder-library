from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        #根を返す
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
      　#xとyを結合
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
      　#xが属するグループのサイズを返す
        return -self.parents[self.find(x)]

    def same(self, x, y):
      　#x,yが同じグループに属するか返す
        return self.find(x) == self.find(y)

    def members(self, x):
      　#xが属するグループに属する要素を返す
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
      　#全ての根の要素を返す
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
      　#グループの数を返す
        return len(self.roots())

    def all_group_members(self):
      　#ルート要素: [そのグループに含まれる要素のリスト], ...のdictを返す
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())
