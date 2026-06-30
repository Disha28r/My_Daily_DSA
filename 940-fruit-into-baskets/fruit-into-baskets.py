class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        high = 0
        low = 0
        f = {}
        res = -1
        for high in range(n):
            f[fruits[high]] = f.get(fruits[high],0)+1
            while(len(f)>2):
                f[fruits[low]]-=1
                if f[fruits[low]]==0:
                    del f[fruits[low]]
                low+=1
            if len(f)<=2:
                window_len=high-low+1
                res=max(res,window_len)
        return res