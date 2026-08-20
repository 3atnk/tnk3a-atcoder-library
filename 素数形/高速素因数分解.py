class Eratosthenes:
    def __init__(self, N):
        # テーブル
        self.isprime = [True] * (N + 1)

        # 整数 i を割り切る最小の素数
        self.minfactor = [-1] * (N + 1)

        # 1 は予めふるい落としておく
        self.isprime[1] = False
        self.minfactor[1] = 1

        # 篩
        for p in range(2, N + 1):
            # すでに合成数であるものはスキップする
            if not self.isprime[p]:
                continue

            # p についての情報更新
            self.minfactor[p] = p

            # p 以外の p の倍数から素数ラベルを剥奪
            for q in range(p * 2, N + 1, p):
                # q は合成数なのでふるい落とす
                self.isprime[q] = False

                # q は p で割り切れる旨を更新
                if self.minfactor[q] == -1:
                    self.minfactor[q] = p

    # 高速素因数分解
    # (素因子, 指数) のリストを返す
    def factorize(self, n):
        res = []

        while n > 1:
            p = self.minfactor[n]
            exp = 0

            # p で割り切れる限り割る
            while n > 1 and self.minfactor[n] == p:
                n //= p
                exp += 1

            res.append((p, exp))

        return res

er = Eratosthenes(10**6)

print(er.isprime[17])       # True
print(er.isprime[18])       # False

print(er.minfactor[18])     # 2
print(er.factorize(360))
