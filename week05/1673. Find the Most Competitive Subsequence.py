def mostCompetitive(nums: list[int], k: int) -> list[int]:
    '''
    [3, 5, 2, 6, 5] k = 2 res = [2, 5]
    brute force would be k! time complexity

    solve by monotonically increasing stack
    3 - [3]
    5 - [3, 5]
    2 - [2]
    2 - [2, 6]

    [2, 3, 4, 5] k = 4 6 does not go in

    [2, 3, 4] k = 4 6 would go in

    time: O(n)
    space: O(n)
    '''
    stack = []
    for i, num in enumerate(nums):
        # check that there is enough numbers left
        # if the number of empty space in the stack equals
        # the numbers left, then add everything to the stack
        if len(nums) - i + len(stack) == k:
            return stack + nums[i:]
        # monotonically increasing stack
        # check that the while loop doesn't pop too many numbers so that
        # the number left doesn't cover the space left open in the stack
        while stack and stack[-1] > num and len(stack) - 1 + len(nums) - i >= k:
            stack.pop()
        if len(stack) < k:  # checking if any elements were popped at all OR
            # checking that the stack is not already full
            stack.append(num)
    return stack


print(mostCompetitive([2, 4, 3, 3, 5, 4, 9, 6], 4))
