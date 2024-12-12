def knapsack(items, W):
    n = len(items)
    dp = [[0]*(W+1) for _ in range(n+1)]

    for i in range(1, n+1):
        wt, val = items[i-1]
        for w in range(W+1):
            dp[i][w] = dp[i-1][w]
            if wt <= w:
                dp[i][w] = max(dp[i][w], dp[i-1][w-wt] + val)

    print("DP Table:")
    header = ["w\\i"] + list(range(W+1))
    print(" ".join(map(str,header)))
    for i in range(n+1):
        row = [i] + dp[i]
        print(" ".join(map(str,row)))

    res_value = dp[n][W]
    w = W
    chosen = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            chosen.append(items[i-1])
            w -= items[i-1][0]

    chosen.reverse()
    return chosen, res_value

if __name__ == "__main__":
    items = [(2,6),(1,3),(4,9),(1,5),(3,6)]
    W = 6
    chosen, val = knapsack(items, W)
    print("Оптимальный набор:", chosen)
    print("Макс. ценность:", val)