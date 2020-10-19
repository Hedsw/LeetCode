class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        threshold1 = threshold2 = float("inf") # Bring Lastest Number 
        for num in nums: 
            if threshold1 >= num:
                threshold1 = num
            elif threshold2 >= num:
                threshold2 = num
            else:
                return True
        return False
    
    # 제일 큰 작은 숫자부터 threshold1에 넣고, 그 다음 작은 숫자를 threshold2에 넣고 계속적으로 숫자를 늘려가면 됨
    