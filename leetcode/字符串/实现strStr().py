class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # 方法1
        # if needle not in haystack:
        #     return -1
        # return haystack.find(needle)

        # 方法2

        l = len(needle)
        for i in range(len(haystack)-l):
            if haystack[i:i+l]==needle:
                return i
        return  -1

if __name__=='__main__':
    h = 'hello'
    n = 'll'
    print(Solution().strStr(h,n))