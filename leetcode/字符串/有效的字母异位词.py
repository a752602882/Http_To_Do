class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!= len(t):
            return False
        c = set(s)
        for i  in  c:
            if s.count(i) != t.count(i):
                return  False
        return True

if  '__name__' =='__main__':
    s = "anagram"
    t = "nagaram"
    print(Solution().isAnagram((s,t)))