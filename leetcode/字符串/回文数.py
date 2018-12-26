import string


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #大小写字母
        letters =string.ascii_letters
        # 数字
        digits  = string.digits
        s = s.lower()
        print(s)
        s = [i for i in s if i in letters or i in digits ]
        print(s)
        return s[::-1] == s[:]


if __name__ == '__main__':
    s = 'A man, a plan, a c1#anal: Panama'
    print(Solution().isPalindrome(s))