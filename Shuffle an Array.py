class Solution:

    def __init__(self, nums: List[int]):
        self._array = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self._array
        

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        shuffled_copy = self._array[:]
        random.shuffle(shuffled_copy)
        return shuffled_copy

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()