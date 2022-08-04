def twoSum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        if target-nums[i] in nums[:i] + nums[i+1:]:
            num = nums.pop(i)
            return [i, nums.index(target- num)+1]

print(twoSum([2,7,11,19], 13))