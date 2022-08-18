######## Sqaures of sorted array (problem number 977 ############
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
    
        ptr1=0
        ptr2=len(nums)-1
        res=[]
        
        while ptr1<=ptr2:
            if (nums[ptr1] * nums[ptr1]) > (nums[ptr2] * nums[ptr2]):
                res.append(nums[ptr1] * nums[ptr1])
                ptr1 +=1
            else:
                res.append(nums[ptr2] * nums[ptr2])
                ptr2 -=1
        return res[::-1]
                
