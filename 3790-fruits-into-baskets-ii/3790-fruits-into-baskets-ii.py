class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        n=len(fruits)
        unplaced=0

        for i in range(n):
            placed=0
            for j in range(n):
                if baskets[j]!=-1 and fruits[i]<=baskets[j]:
                    baskets[j]=-1
                    placed=1
                    break
            if placed==0:
                unplaced+=1

        return unplaced
                    