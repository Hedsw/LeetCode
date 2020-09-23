class Solution:
    def reverse(self, x: int) -> int:
        always = 0
        pm = False # True = - , False = + 
        
        if x < 0:
            always = abs(x)
            pm = True 
        else:
            always = x 
        
        always = str(always)[::-1]
        always = int(always)
        if always > 2**31 -1:
            return 0 
        
        if pm:
            always = always*(-1)
            if always < (-2)**31:
                return 0
                    
        return always