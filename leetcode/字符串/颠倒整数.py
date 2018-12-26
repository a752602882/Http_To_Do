class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if  -10<x<10:
            return x

        str_x=str(x)

        if str_x[0]!= '-':
            str_x = str_x[::-1]
            x = int(str_x)
        else:
            str_x = str_x[:0:-1]
            x = int(str_x)
            x = -x

        return x if -2147483648 < x < 2147483647 else 0



if __name__=='__main__':
    print(Solution().reverse(-123450))

    # a = [1,3,4,2,'a','d']
    # #a = (1,2,3)
    # print (a[4:1:-1])