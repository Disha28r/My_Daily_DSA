class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        nodelete=arr[0]
        onedelete= float('-inf')
        result=arr[0]
        n = len(arr)
        res= arr[0]

        for i in range(1,n):
            prev_nodelete = nodelete
            prev_onedelete = onedelete

            nodelete = max(nodelete+arr[i],arr[i])

            if prev_onedelete == float('-inf'):
                v2 = arr[i]
            else:
                v2 = prev_onedelete + arr[i]

            onedelete = max(v2,prev_nodelete)

            res = max(res, max(onedelete,nodelete))
        return res
