def greedy_coins(n, coins=[100,50,10,4,3,1]):
    res = []
    for c in coins:
        while n >= c:
            n -= c
            res.append(c)
    return res

def dp_coins(n, coins=[1,3,4,10,50,100]):
    dp = [float('inf')] * (n+1)
    dp[0] = 0
    parent = [-1]*(n+1)
    for i in range(1,n+1):
        for c in coins:
            if c <= i and dp[i-c]+1 < dp[i]:
                dp[i] = dp[i-c]+1
                parent[i] = c
    res = []
    cur = n
    while cur > 0:
        res.append(parent[cur])
        cur -= parent[cur]
    return res

if __name__ == "__main__":
    n = 6
    gr = greedy_coins(n)
    dp_sol = dp_coins(n)
    print("Жадное решение:", gr, "Количество:", len(gr))
    print("ДП решение:", dp_sol, "Количество:", len(dp_sol))
