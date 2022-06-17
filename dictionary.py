### Dictionary  Code 1 ###########

from collections import Counter 

dict1= [1,2,1,3,4,1,1,1]
print(Counter(dict1))

############# Code 2 #############
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict2={}
        
        for i in nums:
            if i not in dict2:
                dict2[i]=1
            else:
                dict2[i]+=1
                return True
        
        return False
