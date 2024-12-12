def longest_common_substring_table(s1, s2):
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
    return dp, longest

if __name__ == "__main__":
    s1 = "blue"
    s2 = "clue"
    dp, length = longest_common_substring_table(s1, s2)
    print("DP Table:")
    for row in dp:
        print(row)
    print("Longest Common Substring Length:", length)
