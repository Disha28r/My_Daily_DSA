class Solution:
    def removeDuplicates(self, s: str) -> str:
        res=[]
        for x in s:
            if res and res[-1] == x:
                res.pop()
            else:
                res.append(x)
        return "".join(res)
        