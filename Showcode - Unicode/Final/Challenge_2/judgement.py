class Solution:
    
    def is_launch_code_fibonacci(self, input):
        
        import math
        
        if input < 0:
            return False
            
        if input == 0:
            return True
        
        a = (5*input*input)+4
        b = (5*input*input)-4
        flag = 0
        if round(math.sqrt(a))*round(math.sqrt(a)) == a:
            flag = flag + 1
        if round(math.sqrt(b))*round(math.sqrt(b)) == b:
            flag = flag + 1
            
        if flag == 0:
            return False
        else:
            return True
