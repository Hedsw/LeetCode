class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        RawLength = len(matrix)
        ColumnLength = len(matrix[0])
        
        setRaw, setCol = set(), set()
        
        for i in range(RawLength):
            for j in range(ColumnLength):
                if matrix[i][j] == 0:
                    setRaw.add(i)
                    setCol.add(j)
        
        for i in range(RawLength):
            for j in range(ColumnLength):
                if i in setRaw or j in setCol:
                    matrix[i][j] = 0
                    
        
        # Time Complexity = Big oh ->  (M*N) M and N is Raw and Column length
        # Sapce Completxity is  Big oh- >  M + N