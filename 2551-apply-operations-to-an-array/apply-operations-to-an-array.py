class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        
        # Step 2: Move zeros to the end while maintaining order of non-zero elements
        non_zeros = [num for num in nums if num != 0]  # Corrected variable usage
        zeros = [0] * (len(nums) - len(non_zeros))
        
        return non_zeros + zeros
