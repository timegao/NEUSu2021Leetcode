def twoSum(self, nums: List[int], target: int) -> List[int]:
    '''
    must be distinct?
    does not need to account for empty or null case
    return indices


    brute force solution: O(n^2) time, O(1) space
    nested loop through all numbers
    check if the two numbers add up to the target
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target: return [i, j]

    loop through all the numbers once
    a dictionary to track the numbers and their indices
    add number/index on each loop
    we trade space for time by storing values in the dictionary
    time complexity: O(n) because we iterate through all the numbers in the list
    space complexity: O(n) because we store all the numbers in the list
    '''
    d = {}  # tracks existing numbers and their index
    for index, num in enumerate(nums):  # O(n)  [0, 3], [1, 2], [2, 4]
        if target - num in d:  # nothing, 6 - 2 = 4 not in d, 6 - 4 = 2 in d
            return [d[target - num], index]  # [1, 2]
        d[num] = index  # d = {3: 0}, {3: 0, 2: 1}
