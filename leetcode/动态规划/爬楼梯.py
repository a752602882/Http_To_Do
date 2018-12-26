'''
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。
'''
import time

class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        elif n==2:
            return 2
        else:
            tmp = [1,2]
            for i in range(2,n):
                print(tmp)
                tmp.append(tmp[i-1] + tmp[i-2])
            return tmp[-1]


if __name__ == '__main__':
      Solution().climbStairs(5)


    # result = [0, 1,2,3,4,5,6,7]
    # print(result[-1])
    # print(result[-2])
