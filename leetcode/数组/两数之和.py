class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a ={}
        n = len(nums)
        for x in range(n):
            b = target-nums[x]
            if b in nums:
                y = nums.index(b)
                print('-----下标：----',y)
                if y!=x:
                    a[x]=y

        return  a


if __name__ == '__main__':
    nums = [2, 7, 11, 15,3,4,5]
    target = 9

    print(Solution().twoSum(nums, target))
