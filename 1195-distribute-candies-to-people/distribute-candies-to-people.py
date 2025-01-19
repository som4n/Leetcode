class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        people = [0]*num_people
        index=1
        while candies>0:
            if candies >index:
                people[(index-1) % num_people ] += index
            else:
                people[(index-1)% num_people] +=candies
            candies -= index
            index +=1
        return people
         