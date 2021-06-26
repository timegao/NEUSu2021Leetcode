# use a monotonically decreasing stack to keep track of decreasing temperatures
# when a higher temperature is found (compared to the last element in the stack),
# pop the last element in the stack, which is the index, and calculate the distance
# set the values in res default to 0 and change it if a higher values is found
# time: O(n)
# space: O(n)
# def dailyTemperatures(temperatures: list[int]) -> list[int]:
#     res, stack = [0] * len(temperatures), []
#     for i, num in enumerate(temperatures):
#         while stack and num > temperatures[stack[-1]]:
#             index = stack.pop()
#             res[index] = i - index
#         stack.append(i)
#     return res

# instead of going forward, go backwards and keep track of the highest
# decreases to O(1) space because we only track the highest from the right
# still O(n) time
def dailyTemperatures(temperatures: list[int]) -> list[int]:
    n, right_max = len(temperatures), float('-inf')
    res = [0] * n
    for i in range(n-1, -1, -1):
        temp = temperatures[i]
        if right_max <= temp:   # not possible to find higher
            right_max = temp
        else:
            days = 1
            # iterate through elements on the right to find out
            # what the next highest temperature is
            while temperatures[i + days] <= temp:
                days += res[i + days]
            res[i] = days
    return res


print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
