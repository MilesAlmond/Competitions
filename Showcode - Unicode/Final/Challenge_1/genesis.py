class Solution:

    def final_function(self, input):
        if (input < 1):
            result = 0
        else:
            flag = 0
            for i in range(2,input):
                if (input % i) == 0:
                    flag = 1
                    break
            if (flag == 0):
                result = 0
            else:
                if (input % 3) == 0:
                    result = 3**(input/3)
                elif (input % 3) == 1:
                    result = 2*2*3**((input-4)/3)
                else:
                    result = 2*3**((input-2)/3)
        return result
