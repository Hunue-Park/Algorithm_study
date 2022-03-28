#longest palindromic substring

# Input: s = "babad" => two pointer available??
# Output: "bab"
# Note: "aba" is also a valid answer.

class Solution(object):
    def longestPanlindrome(self, s):
        letter_list = list(s.strip())
        N = len(list(letter_list))
        dp = [[0] * N for _ in range(N)]
        for len_of_num in range(N):
            for start in range(N - len_of_num):
                end = start + len_of_num
                if start == end:
                    dp[start][end] = 1
                elif s[start] == s[end]:
                    if start + 1 == end:
                        dp[start][end] = 1
                    elif dp[start+1][end-1] == 1:
                        dp[start][end] = 1
        flag = 0
        for i in range(N-1, -1, -1):
            for j in range(N):
                if dp[i][j] != 0:
                    flag = 1
                    target_start = i
                    target_end = j
                    break
            if flag == 1:
                break
        target = letter_list[start:end+1]
        result = "".join(target)
        return result