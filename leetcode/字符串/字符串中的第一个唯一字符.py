import collections


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic=collections.Counter(s)
        print(type(dic))
        for i in range(len(s)):
            print(s[i])
            if dic[s[i]]==1:#如果字典中value为1
                return i
        return -1

if __name__ =='__main__':
       s = "loveleetcode"

       print(Solution().firstUniqChar(s))
