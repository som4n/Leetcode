class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        boat,low,high=0,0, len(people)-1
        people = sorted(people) 
        while low <= high:
            if people[high]+ people[low] <= limit:
                low+=1
            boat+=1
            high-=1
        return boat  