class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''

        if len(strs)==1:
            return  strs[0]

        minl = min(len(x) for x in strs)

        if minl ==0:
            return ''


        end = 0

        while end <minl:
            for i in range(1,len(strs)):
                if strs[0][end]!= strs[i][end]:
                   return strs[0][:end]
            end += 1

        return strs[0][:end]



if __name__ =='__main__':
    strs = ["flower","flow","floight"]
    #print(strs[0][0:1])

    strs1 = ["cc","cc1"]
    print(Solution().longestCommonPrefix(strs1))

