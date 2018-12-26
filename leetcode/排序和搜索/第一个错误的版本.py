def isBadVersion(n):
    pass
    '''
    模拟方法
    return true 表示错误版本
    return false 表示正确版本 
    '''

class Solution:



    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n

        while(True):
            mid = (left+right)//2

            if  isBadVersion(mid)==True and isBadVersion(mid+1) ==True:
                  right ==mid
            elif isBadVersion(mid)==False and isBadVersion(mid+1) ==False:
                  left==mid
            elif isBadVersion(mid)==False and isBadVersion(mid+1) ==True:
                return mid+1


if __name__ =='__main__':
    print(5//2)
    print(6//2)