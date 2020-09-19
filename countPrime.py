class Solution:
    def countPrimes(self, n: int) -> int:
        # Prime Number 는 2 또는 3으로 나눠지는 숫자를 Prime Number라고 함. 
        if n < 2:
            return 0
        sieve = [True] * n
        sieve[0] = 0
        sieve[1] = 0
        
        m = int(n**0.5)
        for i in range(2, m+1):
            if sieve[i] == True:
                for j in range(i+i, n ,i):
                    sieve[j] = False
        
        return sum(sieve)

        #에라토스테네스의 체로 구함 
        '''
        2부터 소수를 구하고자 하는 구간의 모든 수를 나열한다. 그림에서 회색 사각형으로 두른 수들이 여기에 해당한다.
        2는 소수이므로 오른쪽에 2를 쓴다. (빨간색)
        자기 자신을 제외한 2의 배수를 모두 지운다.
        남아있는 수 가운데 3은 소수이므로 오른쪽에 3을 쓴다. (초록색)
        자기 자신을 제외한 3의 배수를 모두 지운다.
        남아있는 수 가운데 5는 소수이므로 오른쪽에 5를 쓴다. (파란색)
        자기 자신을 제외한 5의 배수를 모두 지운다.
        남아있는 수 가운데 7은 소수이므로 오른쪽에 7을 쓴다. (노란색)
        자기 자신을 제외한 7의 배수를 모두 지운다.
        위의 과정을 반복하면 구하는 구간의 모든 소수가 남는다.
        '''