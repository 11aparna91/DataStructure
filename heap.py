import heapq
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        arr=heapq.nlargest(2,nums)
        return (arr[0]-1) * (arr[1]-1)
