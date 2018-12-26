class Solution:
    def longestCommonPrefix(self, strs):


        if not strs :
            return ''
        if len(strs) ==1:
            return  strs[0]

        minl  =  min(len(x) for x in strs)
        end = 0
        while end<minl:
            for i in range(1,len(strs)):
                if strs[0][end]!=strs[i][end]:
                    return strs[0][:end]
            end+=1

