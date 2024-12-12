import itertools

def brute_force_knapsack(items, W):
    n = len(items)
    best_value = 0
    best_set = []
    for subset_size in range(n+1):
        for subset in itertools.combinations(range(n), subset_size):
            total_w = sum(items[i][0] for i in subset)
            total_v = sum(items[i][1] for i in subset)
            if total_w <= W and total_v > best_value:
                best_value = total_v
                best_set = [items[i] for i in subset]
    return best_set, best_value

def greedy_knapsack(items, W):
    sorted_items = sorted(items, key=lambda x: x[1]/x[0], reverse=True)
    result = []
    total_w = 0
    total_v = 0
    for wt, val in sorted_items:
        if total_w + wt <= W:
            result.append((wt,val))
            total_w += wt
            total_v += val
    return result, total_v

def dp_knapsack(items, W):
    n = len(items)
    dp = [[0]*(W+1) for _ in range(n+1)]
    for i in range(1, n+1):
        wt, val = items[i-1]
        for w in range(W+1):
            dp[i][w] = dp[i-1][w]
            if wt <= w:
                dp[i][w] = max(dp[i][w], dp[i-1][w-wt]+val)
    res_value = dp[n][W]
    w = W
    chosen = []
    for i in range(n,0,-1):
        if dp[i][w] != dp[i-1][w]:
            chosen.append(items[i-1])
            w -= items[i-1][0]
    chosen.reverse()
    return chosen, res_value

if __name__ == "__main__":
    W = 6
    items = [(2,6),(1,3),(4,9),(1,5),(3,6)]

    br_set, br_val = brute_force_knapsack(items, W)
    gr_set, gr_val = greedy_knapsack(items, W)
    dp_set, dp_val = dp_knapsack(items, W)

    print("Полный перебор:", br_set, br_val)
    print("Жадный алгоритм:", gr_set, gr_val)
    print("ДП:", dp_set, dp_val)
