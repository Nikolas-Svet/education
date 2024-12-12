def min_coins_limited(n, coins, limits):

    memo = {}


    def backtrack(target, coin_index, limits):
        if target == 0:
            return (0, [])
        if coin_index == len(coins):
            return (float('inf'), [])

        key = (target, coin_index, tuple(limits[c] for c in coins))
        if key in memo:
            return memo[key]


        best_count, best_solution = backtrack(target, coin_index+1, limits)


        coin = coins[coin_index]
        if limits[coin] > 0 and coin <= target:
            limits[coin] -= 1
            count_take, sol_take = backtrack(target-coin, coin_index, limits)
            limits[coin] += 1
            if count_take + 1 < best_count:
                best_count = count_take + 1
                best_solution = sol_take + [coin]

        memo[key] = (best_count, best_solution)
        return memo[key]

    res = backtrack(n, 0, limits)
    if res[0] == float('inf'):
        return None
    else:
        return res[1]

if __name__ == "__main__":
    coins = [1,3,4,10,50,100]
    stock = {1:10, 3:5, 4:5, 10:10, 50:2, 100:2}

    clients = 3
    requests = [6, 134, 7]

    for amount in requests:
        print("Клиент хочет снять:", amount)
        res = min_coins_limited(amount, coins, stock)
        if res is None:
            print("Невозможно выдать сумму из-за нехватки купюр и монет.")
        else:
            print("Выдача монет/купюр:", res)

            for c in res:
                stock[c] -= 1
            print("Оставшиеся ресурсы:", stock)
        print("---")