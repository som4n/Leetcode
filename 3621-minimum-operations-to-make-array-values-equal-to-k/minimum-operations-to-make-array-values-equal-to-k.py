class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        mini=min(nums)
        if mini <k:
            return -1
        st = set(nums)
        return len(st)-(mini==k)