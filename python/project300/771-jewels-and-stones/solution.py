class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stonesCount = {}

        # Populate a hash table with our stones count.
        for i in range(len(stones)):
            stonesCount[stones[i]] = stonesCount.get(stones[i], 0) + 1  


        # Count the jewels that are in this list.
        total = 0
        for j in jewels:
            total += stonesCount.get(j,0)

        return total
  

s = Solution()
jewels = "aA"
stones = "aAAbbbb"
print(s.numJewelsInStones(jewels, stones))