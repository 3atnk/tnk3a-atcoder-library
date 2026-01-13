#nCrについて、事前にk個のリストを作っといて各クエリにO(1)で答えることができるようにしてるやつ
#計算量はクエリはO(1)、事前計算はO(N)

class Combination:
    def __init__(self, max_n, mod=998244353):
        self.mod = mod
        self.max_n = max_n
        
        self.fact = [1] * (max_n + 1)      # 階乗 n!
        self.finv = [1] * (max_n + 1)      # 逆元 (n!)^-1
        
        # 1. 階乗の計算 O(N)
        for i in range(2, max_n + 1):
            self.fact[i] = (self.fact[i-1] * i) % mod
            
        # 2. 最後の値の逆元を計算 O(log mod)
        # フェルマーの小定理: a^(p-2) = a^-1 (mod p)
        self.finv[max_n] = pow(self.fact[max_n], mod - 2, mod)
        
        # 3. 逆元を後ろから埋める O(N)
        # (i!)^-1 = ((i+1)!)^-1 * (i+1)
        for i in range(max_n, 1, -1):
            self.finv[i-1] = (self.finv[i] * i) % mod

    def nCk(self, n, k):
        if n < k or n < 0 or k < 0:
            return 0
        # nCk = n! * (k!)^-1 * ((n-k)!)^-1
        return self.fact[n] * self.finv[k] % self.mod * self.finv[n-k] % self.mod


MAX_N = 2 * 10**5
comb = Combination(MAX_N)

#print(comb.nCk(N, K)) 
