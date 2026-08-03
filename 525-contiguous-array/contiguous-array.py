class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n= len(nums)
        zeros=0
        ones=0
        f={}
        res=0
        for i in range(n):
            if nums[i]==0:
                zeros+=1
            else:
                ones+=1
            diff = zeros - ones
            if diff == 0:
                res = max(res,i+1)
            elif diff not in f:
                f[diff] = i
            else:
                idx = f.get(diff,0)
                subarray_len = i - idx
                res = max(subarray_len,res)
        return res