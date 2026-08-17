class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total=0
        li=[]
        for i in range(len(nums)):
            total=total+nums[i]
            li.append(total)
        return li