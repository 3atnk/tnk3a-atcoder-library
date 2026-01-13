#Nが10**9などでも対応可能
#計算量はO(k+logmod)

n = 10 ** 9
k = 2 * 10 ** 5
mod = 998244353 

# 逆元計算 (組み込みのpowを使用)
def modinv(x):
    return pow(x, mod-2, mod)

def binomial_coefficients(n, k):
    numera = 1
    denomi = 1

    for i in range(k):
        numera *= n-i
        numera %= mod
        denomi *= i+1
        denomi %= mod
        
    return numera * modinv(denomi) % mod

print(binomial_coefficients(n, k))
