import collections

# two pointers solution using defaultdict

# def lengthOfLongestSubstring(s: str) -> int:
#     counts = collections.defaultdict(int)
#     length, i, j, duplicates = 0, 0, 0, 0
#     while j < len(s):
#         if duplicates < 1:
#             counts[s[j]] += 1
#             if counts[s[j]] > 1:
#                 duplicates += 1
#             j += 1
#         else:
#             counts[s[i]] -= 1
#             if counts[s[i]] == 1:
#                 duplicates -= 1
#             i += 1
#         length = max(length, j - i) if duplicates < 1 else length
#     return length


def lengthOfLongestSubstring(s: str) -> int:
    d = {}
    longest, j = 0, 0
    for i in range(len(s)):
        if s[i] in d:  # duplicate found
            j = max(j, d[s[i]] + 1)  # move j pointer to last occurrence
        d[s[i]] = i  # update current occurrence
        longest = max(longest, i - j + 1)
    return longest


print(lengthOfLongestSubstring("abcabcbb"))
