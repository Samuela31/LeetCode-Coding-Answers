class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        ans=''
        s1,s2=len(word1),len(word2)
        i,j=0,0

        #FASTER METHOD
        while i<s1 or j<s2:
            if i<s1:
                ans+=word1[i]
                i+=1

            if j<s2:
                ans+=word2[j]
                j+=1

        return ans

        '''
        #PASSES ALL TESTCASES
        while i<s1 and j<s2:
            ans+=word1[i]
            ans+=word2[j]
            i+=1
            j+=1

        while i<s1:
            ans+=word1[i]
            i+=1

        while j<s2:
            ans+=word2[j]
            j+=1

        return ans
        '''
        