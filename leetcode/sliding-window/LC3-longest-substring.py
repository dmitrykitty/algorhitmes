def lengthOfLongestSubstring(s):
    begin = 0
    d = {}
    max_len = 0
    for end in range(len(s)):
        while s[end] in d:
            del d[s[begin]]
            begin += 1
        d[s[end]] = 1
        max_len = max(max_len, end - begin + 1)

    return max_len


s = "abcabcbb"
print(lengthOfLongestSubstring(s))