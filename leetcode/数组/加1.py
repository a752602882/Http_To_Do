class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s = ''
        for i in digits:
            s += str(i)

        s= int(s)+1

        x = []
        for i in str(s):
            x.append(int(i))
        return x


if __name__ == '__main__':
      print( Solution().plusOne([9,9,9]))