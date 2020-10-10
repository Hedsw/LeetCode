class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        left, right = 0, 0
        length = len(s)
        sets = set()
        
        while right < length and left < length:
            if s[right] not in sets:
                sets.add(s[right])
                right += 1
                longest = max(longest, right - left)
            else:
                sets.remove(s[left])
                left += 1
        return longest
        
        
    # Sliding Window Problem
    # Time Complexity O(N)
    # Space Complexity O(k)
    # [k = length of the longest substring w/o repeating characters]
