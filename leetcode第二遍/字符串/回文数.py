import string


class Solution(object):
    def isPalindrome(self, s):

        dights = string.digits
        letters = string.ascii_letters

        s=s.lower()

        s = [i for i in s if i in dights or i in letters]
        print(type(s))
        return s[:] ==s[::-1]


if __name__ == '__main__':
    s = 'A man, a plan, a canal: Panama'
    print(Solution().isPalindrome(s))