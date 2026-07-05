class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        low = 0
        res = 0
        n=len(nums)
        f = {}

        for high in range(n):
            f[nums[high]] = f.get(nums[high], 0) + 1

            while f.get(0, 0) > k:
                f[nums[low]] -= 1
                if f[nums[low]] == 0:
                    del f[nums[low]]
                low += 1
            length=high - low + 1
            res = max(res, length)

        return res