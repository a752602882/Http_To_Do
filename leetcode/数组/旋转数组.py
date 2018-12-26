

class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        k=k%len(nums)#保证循环次数在0-len(nums)之间
        print(nums[len(nums)-k:])
        print(nums[:len(nums)-k])
        nums[:]=nums[len(nums)-k:]+nums[:len(nums)-k]


if  __name__=='__main__':
    list = [7,1,5,3,6,4]

    print(Solution().rotate(list,2))