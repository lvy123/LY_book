class Solution(object):
    def twoSum(self,nums, target):
        
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict_buff={}
        for i,n in enumerate(nums):
            a=target-n
            if a in dict_buff:
                return (dict_buff[a],i)
            else:
                dict_buff[n]=i




def
