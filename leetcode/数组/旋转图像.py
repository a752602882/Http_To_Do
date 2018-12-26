class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = matrix.copy()
        n = len(matrix)
        for i in range(n):
            matrix[i] = [m[j][i] for j in range(n - 1, -1, -1)]
        return
if  __name__=='__main__':
    matrix =  [
                [ 5, 1, 9,11],
                [ 2, 4, 8,10],
                [13, 3, 6, 7],
                [15,14,12,16]
            ]
    Solution().rotate(matrix)
    print(matrix)