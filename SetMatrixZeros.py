class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        R = len(matrix)
        C = len(matrix[0])
        
        rows, cols = set(), set()
        
        # Essentially, we make the rows and columns that are to be made zero
        
        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
                    
        # Iterate over the array once again and using the rows and cols sets, update the elements
        
        for i in range(R):
            for j in range(C):
                if i in rows or j in cols:
                    matrix[i][j] = 0
            
            
        # Time Complexity = O(M * N) M and N is row and column length 
        # Space Completixy = O(M + N) 
        