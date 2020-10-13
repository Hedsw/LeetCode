class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        sets = set()
        length = len(s)
        right, left = 0, 0
        
        while right < length and left < length:
            if s[right] not in sets:
                sets.add(s[right])
                right += 1
                answer = max(answer, right - left)
                
            else:
                sets.remove(s[left])
                left += 1
        return answer
                
        
    # Sliding Window Problem
    # Time Complexity O(N)
    # Space Complexity O(k)
    # [k = length of the longest substring w/o repeating characters]

        
    # Sliding Window Problem
    # Time Complexity O(N)
    # Space Complexity O(k)
    # [k = length of the longest substring w/o repeating characters]
