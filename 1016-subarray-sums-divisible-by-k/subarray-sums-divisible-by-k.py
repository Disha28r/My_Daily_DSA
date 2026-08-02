class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n=len(nums)
        sum_tillnow=0
        f={0:1}
        res=0
        for i in range(n):
            sum_tillnow += nums[i]
            rem = sum_tillnow % k
            freq = f.get(rem,0)
            res+=freq
            f[rem] = f.get(rem,0)+1

        return res