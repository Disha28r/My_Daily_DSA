class Solution:
    def func(self,n):
        sum = 0
        while (n>0):
            d = n% 10
            sum += d*d
            n = n//10
       
        return sum
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = n
        while(fast!=1):
            slow = self.func(slow)
            fast = self.func(fast)
            fast = self.func(fast)
            
            if (slow == fast and slow!=1):
                return False
        fast = 1
        return True
        