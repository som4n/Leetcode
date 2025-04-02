class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Early termination for small arrays
        if n < 3:
            return 0

        max_result = 0
        max_value = nums[0]
        max_diff = 0

        for i in range(1, n):
            # Use current number as nums[k]
            max_result = max(max_result , max_diff * nums[i])

            # Use current number as nums[j]
            max_diff = max(max_diff , max_value - nums[i])


            # Use current number as nums[i] for future calculations
            max_value = max(max_value , nums[i])

        return max_result
    