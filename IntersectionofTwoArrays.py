'''
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        sorted1 = sorted(nums1)
        sorted2 = sorted(nums2)
        fast = slow = 0
        result = []
           
        while True:
            try: 
                if sorted1[fast] == sorted2[slow]:
                    result.append(sorted1[fast])
                    fast += 1 
                    slow += 1

                elif sorted1[fast] < sorted2[slow]:
                    fast += 1
                else:
                    slow += 1

            except IndexError:
                break
                
        return result
 ''' 
# Collections.Counter를 하면, nums1 안에 있는 숫자들이 Dictionary처럼 정리되어서 몇번 반복되는지가 나와 있음. 그리고 count[nus]으로 서치한다면, count안에 있는 것들이 몇번 있는지가 나오고, 그 숫자를 하나씩 까면서 res에 값을 넣어주면 그게 중복값의 갯수를 카운트 함과 동시에 중복되는거만 뽑아낼 수가 있다. 
class Solution(object):
    def intersect(self, nums1, nums2):

        counts = collections.Counter(nums1)
        res = []
        
        for num in nums2:
            if counts[num] > 0:
                res += num,
                counts[num] -= 1

        return res
        
