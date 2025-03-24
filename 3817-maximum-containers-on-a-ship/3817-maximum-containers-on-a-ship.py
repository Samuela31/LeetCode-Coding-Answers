class Solution(object):
    def maxContainers(self, n, w, maxWeight):
        """
        :type n: int
        :type w: int
        :type maxWeight: int
        :rtype: int
        """
        cells=n*n

        #w*x <=maxWeight where x is no. of containers that can be filled and x<=n*n
        x=maxWeight//w

        #Eg: n=2,w=3,maxWeight=15
        if x>cells:
            return cells
        else:
            return x
        