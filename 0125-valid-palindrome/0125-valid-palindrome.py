class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)==0:
            return True
        
        #OPTIMIZED METHOD
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
        return True

        '''
        #RECURSIVE METHOD
        def pal(s,st,ed):
            if st<ed:
                if s[st]==s[ed]:
                    return pal(s,st+1,ed-1)
                else:
                    return False
            return True

        t=''
        for i in range(len(s)):
            if s[i].isalnum():
                t+=s[i].lower()

        return pal(t,0,len(t)-1)
        '''

        '''
        #BETTER METHOD
        t=''
        for i in range(len(s)):
            if s[i].isalnum():
                t+=s[i].lower()

        for i in range(len(t)//2):
            if t[i]!=t[len(t)-i-1]:
                return False
        return True
        '''