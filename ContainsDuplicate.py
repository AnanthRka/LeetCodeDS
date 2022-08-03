def containsDuplicate(nums: list[int]):
    return not len(nums) == len(set(nums))

print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))