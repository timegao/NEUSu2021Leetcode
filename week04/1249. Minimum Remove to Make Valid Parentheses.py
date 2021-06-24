# Solution tries to keep the stack valid at all times
# However, it's much more complicated to keep track of the valid
# Rather than keep the invalid indices

# def minRemoveToMakeValid(self, s: str) -> str:
#         stack, cur = [], ""
#         for c in s:
#             if c == "(":
#                 stack += [cur]
#                 cur = ""
#             elif c == ")":
#                 if stack:
#                     cur = stack.pop() + "(" + cur + ")"
#             else:
#                 cur += c
#         while stack:
#             cur = stack.pop() + cur
#         return cur

def minRemoveToMakeValid(s: str) -> str:
    '''
    use stack for last in, first out

    "lee(t(c)o)de)"
    ["("] i = 3
    ["(", "("] i = 5
    ["("] i = 7
    [] i = 9
    [")"] = 12
    "lee(t(c)o)de)" becomes "leet(t(c)o)de

    start with a list of the s
    for invalid indexes, change the string to ""
    join the list together

    O(n) time, O(n) space
    '''
    stack = []
    lst = list(s)
    for i, char in enumerate(s):
        if char == "(":  # "(" may be invalid if no matching closing
            stack.append(i)
        elif char == ")":
            if stack:  # found matching "("
                stack.pop()
            else:  # no matching "(", so it's invalid
                lst[i] = ""
    for num in stack:
        lst[num] = ""
    return "".join(lst)


print(minRemoveToMakeValid("lee(t(c)o)de)"))
