class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """

        #Best method
        if n==0:
            return 0
        elif n==1 or n==2:
            return 1

        t1,t2=1,1 #terms 1 & 2

        #to start from term 3
        for i in range(n-2):
            temp=t2
            t2=t1+t2
            t1=temp
        
        return t2

        
        '''
        #Recursion
        if n==0:
            return 0
        elif n==1 or n==2:
            return 1

        return self.fib(n-1) + self.fib(n-2)
        '''
        