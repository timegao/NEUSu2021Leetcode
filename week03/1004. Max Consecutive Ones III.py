# two pointers sliding window using O(1) space
# takes advantage of the fact that we're trying to find the longest subarray


def longestOnes(nums: List[int], k: int) -> int:
    i = 0
    for j in range(len(nums)):
        k -= 1 - nums[j]
        # we move left pointer at most one to keep track of longest subarray
        # if k remains negative, move left pointer every iteration
        # if k becomes non-negative, the longest subarray can get longer
        if k < 0:
            k += 1 - nums[i]
            i += 1
    return j - i + 1

# from collections import deque


# # two pointers sliding window using O(n) space
# def longestOnes(nums: list[int], k: int) -> int:
#     q = deque([])
#     longest, j = 0, 0
#     for i in range(len(nums)):
#         if nums[i] == 0:
#             q.append(i)
#         if len(q) > k:
#             j = q.popleft() + 1
#         longest = max(longest, i - j + 1)
#     return longest


print(longestOnes([0, 0, 1, 1, 0, 0, 1, 1,
      1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))
