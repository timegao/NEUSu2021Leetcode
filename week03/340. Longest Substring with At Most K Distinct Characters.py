def lengthOfLongestSubstringKDistinct(s: str, k: int) -> int:
    d = {}
    j, longest = 0, 0
    for i in range(len(s)):
        # default 0 otherwise d.get(s[i]) then add 1
        d[s[i]] = d.get(s[i], 0) + 1
        while len(d) > k:  # keep incrementing j until duplicate count goes down
            d[s[j]] -= 1
            if d[s[j]] == 0:  # duplicate removed
                d.pop(s[j])
            j += 1
        longest = max(longest, i - j + 1)
    return longest


print(lengthOfLongestSubstringKDistinct("eceba", 2))
