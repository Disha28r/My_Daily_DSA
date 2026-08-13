class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.sort()
        
        new_int=[]
        res=[]
        insert=False
        for i in range(len(intervals)):
            if insert == False and intervals[i][0] >= newInterval[0]:
                new_int.append(newInterval)
                insert = True
            new_int.append(intervals[i])
        if insert == False:
                new_int.append(newInterval)
                
        start1= new_int[0][0]
        end1=new_int[0][1]
        for i in range(1,len(new_int)):
            start2=new_int[i][0]
            end2=new_int[i][1]

            if end1>=start2:
                start1=start1
                end1=max(end1,end2)
            else:
                res.append([start1,end1])
                start1=start2
                end1=end2
        res.append([start1,end1])
        return res

        