class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()  
        arr = []
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:  # Compare current element with the previous one
                arr.append(nums[i])
        return arr
            