class WeightedUnionFind():
    def __init__(self, n):
        self.n = n
        # parents[i] < 0 のとき、iは根であり、その値は -(集合のサイズ)
        self.parents = [-1] * n
        # 親ノードとの重みの差 (weight[i] = weight[parent] + diff_weight[i])
        self.diff_weight = [0] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            root = self.find(self.parents[x])
            # 経路圧縮時に、親から根までの重みを累積させる
            self.diff_weight[x] += self.diff_weight[self.parents[x]]
            self.parents[x] = root
            return root

    def weight(self, x):
        """根からの重み（ポテンシャル）を返す"""
        self.find(x) # 経路圧縮を実行
        return self.diff_weight[x]

    def diff(self, x, y):
        """xからyへの重み（距離）を計算する (V[y] - V[x])"""
        return self.weight(y) - self.weight(x)

    def union(self, x, y, w):
        """weight(y) = weight(x) + w となるように併合する"""
        # 根を探すとともに経路圧縮
        rx = self.find(x)
        ry = self.find(y)
        
        if rx == ry:
            return

        # 重みの整合性をとる: w_new = w + weight(x) - weight(y)
        # ※ weight(x)などはfind()内で更新されている
        w += self.diff_weight[x]
        w -= self.diff_weight[y]

        # Union by Size: サイズが大きい方に小さい方を繋げる
        if self.parents[rx] > self.parents[ry]:
            rx, ry = ry, rx
            w = -w

        # サイズの更新
        self.parents[rx] += self.parents[ry]
        # 木の結合
        self.parents[ry] = rx
        self.diff_weight[ry] = w

    def size(self, x):
        """xが属する集合のサイズを返す"""
        return -self.parents[self.find(x)]

    def same(self, x, y):
        """xとyが同じ集合に属するかを判定する"""
        return self.find(x) == self.find(y)
