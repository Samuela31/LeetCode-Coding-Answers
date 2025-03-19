class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        unique_numbers = set()
        n = len(digits)
        
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i != j and i != k and j != k:  #no repitition of numbers
                        if digits[i] != 0:  #first digit can't be zero
                            if digits[k] % 2 == 0:  #last digit is even
                                number = digits[i]*100 + digits[j]*10 + digits[k]
                                unique_numbers.add(number)
        
        return len(unique_numbers)