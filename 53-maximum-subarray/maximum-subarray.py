class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum =0 
        ans = -sys.maxsize -1
        for i in range (0,len(nums)):
            sum = sum+nums[i]
            ans = max(ans,sum)
            if(sum<0):
                sum=0
        return(ans)