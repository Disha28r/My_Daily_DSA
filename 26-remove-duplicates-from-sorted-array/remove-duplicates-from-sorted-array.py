class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        off=0
        cm=1
        res=1
        n=len(nums)
        while(cm<n):
            if nums[cm]==nums[cm-1]:
                cm+=1
                continue
            nums[off+1]=nums[cm]
            off+=1
            res+=1
            cm+=1

        return res
        return nums
        