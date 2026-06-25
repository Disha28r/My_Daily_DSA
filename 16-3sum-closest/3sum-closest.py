class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n=len(nums)
        max_diff=float('inf')
        res_sum=0

        for i in range(n-2):
            left=i+1
            right=n-1

            while left < right:
                total = nums[left] + nums[right] + nums[i]
                diff = abs(total - target)

                if max_diff > diff:
                    max_diff = diff
                    res_sum = total

                if total == target:
                    return res_sum

                if total < target:
                    left +=1
                else:
                    right-=1
        return res_sum