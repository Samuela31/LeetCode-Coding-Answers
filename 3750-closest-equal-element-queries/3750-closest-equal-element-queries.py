class Solution(object):
    def solveQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        indices = {}

        #stores all occurrences of each number in the array
        for i in range(n):
            if nums[i] in indices:
                indices[nums[i]].append(i)
            else:
                indices[nums[i]]=[i]

        #Precompute minimum distances for each element
        for occ in indices.values():
            l = len(occ)
            if l == 1: #if dont't want to modify nums directly means take temp copy and do modifications there, but space used doubles
                nums[occ[0]] = -1 #only 1 occurrence so no valid distance
                continue

            for i in range(l):
                #f (forward neighbor) is next occurrence of the number
                #b (backward neighbor) is previous occurrence of the number
                #%l used for circular wrap around
                f, b = occ[(i + 1) % l], occ[(i - 1 + l) % l]

                #take min of direct and circular distance
                forward = min((n - occ[i] - 1) + f + 1, abs(occ[i] - f))
                backward = min(abs(b - occ[i]), occ[i] + (n - b))
                nums[occ[i]] = min(backward, forward)

        for i in range(len(queries)):
            queries[i] = nums[queries[i]]

        return queries

        '''
        #Brute force, doesn't pass some testcases
        arr=[]
        n=len(nums)

        for q in queries:
            mini=float('inf')
            flag=0
            
            for j in range(n):
                if j==q:
                    continue
                
                if nums[j]==nums[q]:
                    flag=1
                    
                    dist = abs(q - j) #direct distance
                    cirdist = n - dist #circular distance
                    mini = min(mini, dist, cirdist)
            
            if flag==0:
                arr.append(-1)
            else:
                arr.append(mini)
                
        return arr
        '''