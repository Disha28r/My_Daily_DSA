class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        low =0
        high=0
        result = float('inf')
        window_sum=0
        n=len(nums)
        while(high<n):
            window_sum += nums[high]
            while(window_sum >= target):
                window_len= high-low+1
                result = min(result,window_len)
                window_sum -= nums[low]
                low+=1
            high+=1
        return 0 if result == float('inf') else result