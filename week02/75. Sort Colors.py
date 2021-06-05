# Dutch flag problem
# Solvable also with a merge sort or a counting sort

def sortColors(nums: list[int]) -> None:
    index, low, high = 0, 0, len(nums) - 1
    while index <= high:
        if nums[index] == 0:
            nums[index], nums[low] = nums[low], nums[index]  # swap
            low += 1
            index += 1
        elif nums[index] == 2:  # swap but redo number by not incrementing index
            nums[index], nums[high] = nums[high], nums[index]
            high -= 1
        else:  # nums[index] == 1 so nothing to change
            index += 1
    print(nums)


sortColors([2, 0, 2, 1, 1, 0])
