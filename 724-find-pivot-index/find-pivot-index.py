class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        arr_sum = sum(nums)

        # Check index 0 separately
        if arr_sum - nums[0] == 0:
            return 0

        left = 0
        for i in range(1, len(nums)):
            left += nums[i - 1]
            right = arr_sum - nums[i] - left

            if left == right:
                return i

        return -1