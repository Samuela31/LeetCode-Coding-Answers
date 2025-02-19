class Solution(object):
    def hasSpecialSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        n=len(s)
        start,end='',''

        if k==1 and n==1: 
            return True

        for i in range(1,n+1): #we put n+1 for case like "jjbbbaaf", 1 where we don't have to compare characters and just check front and back char of substring
            start=s[i-2] if i>=2 else '' #prev char of substring
            st=s[i-1] #1st char of substring (previous char of curr i)
            cnt=1 #to include 1st char of substring
            j=i #index of current char (now 2nd char of substring)

            #compare with previous character to match 
            while j<n and st==s[j] and cnt<k: #dont' put st==s[j] condition before j<n otherwise when j>=n it'll throw list index out error because st==s[j] is evaluated first
                cnt+=1
                j+=1

            end=s[j] if j<n else '' #next char of substring
            
            if cnt==k and start!=st and end!=st:
                return True

            if n-i<k: #no need to check when remaining string to be searched has less length than k
                #keep this condition at last for cases like "jkjhfgg", 2 where we need to process last character before breaking and update cnt if char matches
                break

        return False 
        