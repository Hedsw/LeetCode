# Prime Number 는 2 또는 3으로 나눠지는 숫자를 Prime Number라고 함. 
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3: return 0
        lst = [1] * n
        lst[0], lst[1] = 0, 0
        
        m = 2
        while m * m < n:
            if lst[m]:
                for i in range(m * m, n , m):
                    lst[i] = 0
            
            m += 1
        return sum(lst)
      
        
        # Sieve of Eratosthenes를 사용해서 푸는 것 
        
        