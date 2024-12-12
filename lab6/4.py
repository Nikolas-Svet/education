def longest_common_substring_len(s1, s2):
    n, m = len(s1), len(s2)
    dp = [[0]*(m+1) for _ in range(n+1)]
    longest = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > longest:
                    longest = dp[i][j]
            else:
                dp[i][j] = 0
    return longest

if __name__ == "__main__":
    err_word = "blu"
    candidates = ["blue", "clue", "glue", "blur", "blye"]
    best_word = None
    best_len = -1
    for w in candidates:
        l = longest_common_substring_len(err_word, w)
        if l > best_len:
            best_len = l
            best_word = w
    print("Самое похожее слово по длине общей подстроки:", best_word)
