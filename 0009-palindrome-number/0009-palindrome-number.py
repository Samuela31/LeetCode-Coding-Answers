class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        #Number Manipulation method
        if x>-1 and x<10:
            return True

        if x<0 or x%10==0: #if x is -ve or last digit is 0, then it can't be palindrome. Put this condition after ensuring x is not 0 here
            return False
        
        num=x
        rem=0
        res=0

        while num>0:
            rem=num%10
            res=res*10+rem
            num//=10

        if res==x:
            return True
        return False
        
        '''
        #Using Strings
        s = str(x)
        if s == s[::-1]:
            return True
        else:
            return False
        '''
        