from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums))]
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            # max(not taking the previous house, taking the previous house)
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[-1]
