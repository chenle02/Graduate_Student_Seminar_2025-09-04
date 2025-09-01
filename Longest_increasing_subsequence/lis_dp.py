def lis_dp(arr):
    n = len(arr)
    if n == 0:
        return 0, [], [], [], -1
    dp = [1] * n
    prev = [-1] * n
    best_len = 1
    best_end = 0
    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j
        if dp[i] > best_len:
            best_len = dp[i]
            best_end = i
    seq = []
    k = best_end
    while k != -1:
        seq.append(arr[k])
        k = prev[k]
    seq.reverse()
    return best_len, seq, dp, prev, best_end


def vdc_example():
    return [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

