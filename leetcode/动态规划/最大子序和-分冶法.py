class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left= 0
        right = len(nums)-1

        maxSum  = self.divide(nums,left,right)

        return maxSum



    def divide(self,nums,left,right):

        if left ==right:
            return  nums[left]

        center= (left+right)//2

        leftMaxSum= self.divide(nums,left,center)
        rightMaxSum= self.divide(nums,center+1,right)

        leftBorderSum =nums[center]
        leftSum = nums[center]
        for i in range(center-1,left-1,-1):
            leftSum+= nums[i]
            if leftSum>leftBorderSum:
                leftBorderSum = leftSum

        rightBorderSum =nums[center+1]
        rightSum=nums[center+1]
        for j  in range(center+2,right+1):
            rightSum+= nums[j]
            if rightSum>rightBorderSum:
                rightBorderSum = rightSum

        borderSum= leftBorderSum +rightBorderSum
        return max(leftMaxSum,rightMaxSum,borderSum)



if  __name__=='__main__':
    list = [8,-19,5,-4,20]

    print(Solution().maxSubArray(list))