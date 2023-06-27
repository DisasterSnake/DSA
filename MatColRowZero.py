import ast
class Solution:
    def markRow(self, matrix, n, m, i):
        for j in range(m):
            if matrix[i][j]!=0:
                matrix[i][j]=-1

    def markCol(self, matrix, n, m, j):
        for i in range(n):
            if matrix[i][j]!=0:
                matrix[i][j]=-1

    def setZeroes(self, matrix, n, m):
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    self.markRow(matrix, n, m, i)
                    self.markCol(matrix, n, m, j)
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==-1:
                    matrix[i][j]=0
        return matrix

solutionInstance=Solution()
print("Enter any matrix comprised of only 0s and 1s:")
matrix=ast.literal_eval(input())
n=len(matrix)
m=len(matrix[0])
finalMatrix=solutionInstance.setZeroes(matrix, n, m)
print("Thee final matrix is:")
for row in finalMatrix:
    for ele in row:
        print(ele,end=" ")
    print()