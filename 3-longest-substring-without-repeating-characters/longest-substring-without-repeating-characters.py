class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        low=0
        high=0
        n=len(s)
        res=0
        f={}
        for high in range(n):
            f[s[high]] = f.get(s[high],0)+1
            k=high - low +1
            while len(f)<k:
                f[s[low]]-=1
                if f[s[low]] == 0:
                    del f[s[low]]
                low+=1
                k=high-low+1
            window_len = high - low + 1
            res = max(res,window_len)
        return res

        