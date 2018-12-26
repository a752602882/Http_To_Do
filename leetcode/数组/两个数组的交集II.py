class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        res = []
        for k in nums1:
            if k in nums2:
                res.append(k)
                nums2.remove(k)
        return res

if  __name__=='__main__':
       num1 = [1,2,2,1]
       num2 = [2,2]
       print(Solution().intersect(num2,num1))


