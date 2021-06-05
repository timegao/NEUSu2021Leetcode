def twoSumLessThanK(nums: list[int], k: int) -> int:
    # alternatively sorted_nums = sorted(filter(lambda x: x < k, nums))
    sorted_nums = sorted([x for x in nums if x < k])
    i, j, closest = 0, len(sorted_nums) - 1, -1
    while i < j:
        # you can use walrus operator to initialize inline variables
        if (two_sum := sorted_nums[i] + sorted_nums[j]) < k:
            closest = max(closest, two_sum)
            i += 1
        else:
            j -= 1
    return closest


print(twoSumLessThanK([34, 23, 1, 24, 75, 33, 54, 8], 60))
