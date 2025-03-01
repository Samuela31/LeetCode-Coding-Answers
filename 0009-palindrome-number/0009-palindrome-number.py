class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x>-1 and x<10:
            return True

        if x<0 or x%10==0: #if x is -ve or last digit is 0, then it can't be palindrome. Put this condition after ensuring x is not 0 here
            return False

        #Half Reverse Number Manipulation method (Optimized)
        res= 0
        num=x
        while res < num:
            res= res*10 + num%10
            num//= 10

        #res//10 is for number with odd number of digits to remove middle digit
        return num in (res, res//10) #returns true or false
        
        '''
        ##########################################
        #Number Manipulation method
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
        
        #########################################
        #Using Strings
        s = str(x)
        if s == s[::-1]:
            return True
        else:
            return False
        '''