class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n = len(customers)
        currTime=0
        totalTime=0

        for i in range(n):
            if currTime <=customers[i][0]:
                totalTime+= customers[i][1]
                currTime = customers[i][0] + customers[i][1]
            else:
                totalTime += (currTime - customers[i][0] +customers[i][1])
                currTime += customers[i][1]
        return totalTime/n