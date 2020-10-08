class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        R = len(matrix)
        L = len(matrix[0])
        
        setR, setC = set(), set()
     # Essentially, we make the rows and columns that are to be made zero
       
        for i in range(R):
            for j in range(L):
                if matrix[i][j] == 0:
                    setR.add(i)
                    setC.add(j)
        
          # Iterate over the array once again and using the rows and cols sets, update the elements
      
        for i in range(R):
            for j in range(L):
                if i in setR or j in setC:
                    matrix[i][j] = 0
        
                
    # M and N is row length and column length 
    # Time Complextiy is O(M * N) 
    # Space Complexity is O(M + N)
    
    
    