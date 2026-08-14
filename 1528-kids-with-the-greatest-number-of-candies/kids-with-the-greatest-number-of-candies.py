class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        li=[]
        tot_candy = max(candies)
        for candy in candies:
            if (candy+extraCandies) >= tot_candy:
                li.append(True)
            else: 
                li.append(False)

        return li

        