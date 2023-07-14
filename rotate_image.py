class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        i=0
        while i<len(matrix)-1:
            j=i+1
            while j<len(matrix):
                if i!=j:
                    matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
                j+=1
            i+=1
        
        for i in matrix:
            i.reverse()