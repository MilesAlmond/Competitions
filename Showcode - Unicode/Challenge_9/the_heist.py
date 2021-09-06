class Solution:

    def calculate_capacity(self, input):
        result = []
        for i in range(0,len(input)):
            if i == 0 or i == (len(input)-1):
                continue
            value = min(max(input[:i]),max(input[i+1:]))
            if value - input[i] < 1:
                pass
            else:
                result.append(value - input[i])
        
        return sum(result)
