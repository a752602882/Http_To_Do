class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)==len(set(nums)):
            return False
        else:
            return True



if  __name__=='__main__':
    list = [1,1,1,3,3,4,3,2,4,2]
    list1 = [7,3,1,5,6]
    print(Solution().containsDuplicate(list))