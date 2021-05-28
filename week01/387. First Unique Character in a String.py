def firstUniqChar(s: str) -> int:
    '''
    time complexity: O(n) because we iterate through all the characters in the string s
    space complexity: O(1) because there are only 26 lowercase English letters
    '''
    d = {}  # dictionary
    for i, char in enumerate(s):  # iterate index i and character char
        if char in d:  # alternatively, d.keys()
            d[char] += 1  # track count to know whether character is unique
        else:
            d[char] = 1
        # lines# 5 - 7 could also be written as d[char] = d.get(char, 0) + 1
        # where d.get has a default value of 0 and always increments by 1
    for i, char in enumerate(s):  # iterate index i and character char
        if d[char] == 1:  # unique character found
            return i  # return index
    return -1  # return not found index


print(firstUniqChar("leetcode"))
