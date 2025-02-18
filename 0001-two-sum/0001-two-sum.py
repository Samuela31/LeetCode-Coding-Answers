class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mp = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in mp:
                return [mp[complement], i]
            mp[nums[i]] = i

        return []  # No solution found
        