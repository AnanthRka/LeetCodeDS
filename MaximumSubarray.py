def maxSubArray(nums: list[int]) -> int:
    if len(nums) ==1:
        return nums[0]
    
    max_so_far = max(nums)
    max_here = 0
    
    for i in nums:
        max_here += i
        
        if max_so_far < max_here:
            max_so_far = max_here
            
        if max_here < 0:
            max_here = 0
            
    return max_so_far


print(maxSubArray([ [-2,1,-3,4,-1,2,1,-5,4]]))