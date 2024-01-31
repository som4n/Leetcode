class Solution:
    def dailyTemperatures(self, A: List[int]) -> List[int]:
        result = [0] * len(A)
        stack = [] #storing index in stack 
        for i in range(len(A) - 1, -1, -1):
            while stack and A[stack[-1]] <= A[i]:
                stack.pop()
            result[i] = stack[-1] - i if stack else 0
            stack.append(i)

        return result
