# two sum

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].

class Solution(object):
    def twoSum(self, nums, target):
        for i, n in enumerate(nums):
            complement = target -n
            
            if complement in nums[i + 1:]:
                return nums.index(n), nums[i + 1:].index(complement) + (i+1)
        
        