class Solution:
    from typing import List
    def sortedSquares(self, nums: List[int]) -> List[int]:
        size=len(nums)
        neg=[]
        pos=[]

        #separate
        for num in nums:
            if num<0:
                neg.append(num)
            else:
                pos.append(num)

        #case1: no negative
        if len(neg)==0:
            return [x * x for x in pos]
        #case2: no positive
        if len(pos)==0:
            res=[x*x for x in neg]
            res.reverse()
            return res
        #case3 : both
        neg = [x*x for x in neg][::-1]
        pos =[x*x for x in pos]

        n,m = len(neg),len(pos)
        res=[]
        i=j=0
        while i<n and j<m:
            if neg[i]<=pos[j]:
                res.append(neg[i])
                i+=1
            else:
                res.append(pos[j])
                j+=1
        while i<n:
            res.append(neg[i])
            i+=1
        while j<m:
            res.append(pos[j])
            j+=1

        return res
        
        
        