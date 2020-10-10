class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        right, left = 0, 0
        maxLength = len(s)
        chars = set()
        
        while right < maxLength and left < maxLength:
            if s[right] not in chars:
                chars.add(s[right])
                right += 1
                longest = max(longest, right - left)
            else:
                chars.remove(s[left])
                left += 1
        return longest
        
        
    # Sliding Window Problem
    # Time Complexity O(N)
    # Space Complexity O(k)
    # [k = length of the longest substring w/o repeating characters]
