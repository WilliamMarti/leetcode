class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = nums.count(0)
        
        for x in range(0, zeros):
            
            nums.remove(0)
            
        for x in range(0, zeros):
            
            nums.append(0)
        