class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        #WHEN 64bit NOT allowed, OPTIMIZED LOGIC
        if x>-10 and x<10:
            return x #single digit numbers

        lower, upper= -2**31, 2**31-1
        num= abs(x)

        rem=0
        res=0

        while num>0:
            rem=num%10

            #before updating res, check if updating res causes overflow of 32bit int
            #res*10+rem>upper -->res*10>upper-rem --> res>(upper-rem)//10 means return 0
            if res> (upper-rem)//10:
                return 0

            res=res*10+rem
            num//=10

        if x<0:
            res*=-1 #restore original -ve sign

        return res


        '''
        #64bit allowed method, passed all testcases, BRUTE FORCE
        if x>-10 and x<10:
            return x #single digit numbers

        lower, upper= -2**31, 2**31-1
        num= x if x>0 else -1*x #before reversing remove -ve sign, can use abs() function also

        l=len(str(num)) #to find number of digits
        mul=10**(l-1)
        rem=0
        res=0

        while num>0:
            rem=num%10
            res=rem*mul+res
            mul//=10
            num//=10

        if x<0:
            res*=-1

        if res>=lower and res<=upper:
            return res
        return 0
        '''



        
        