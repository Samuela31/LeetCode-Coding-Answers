class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False

        if x>-1 and x<10:
            return True
        
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
        