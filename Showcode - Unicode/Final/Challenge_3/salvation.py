class Solution:
    
    
    def kill_switch(self, input):
        def split_lists(left,right=[],difference=0):
            left_sum = sum(left)
            right_sum = sum(right)
        
            if left_sum < right_sum or len(left) < len(right):
                return
        
            if left_sum - right_sum == difference:
                return left, right, difference
        
            for i,num in enumerate(left):
                result = split_lists(left[:i]+left[i+1:],right+[num], difference)
                if result:
                    return result
        
            if right or difference > 0:
                return
        
            for target in range(1,left_sum - min(left)+1):
                result = split_lists(left,right,target)
                if result:
                    return result
                
        best_split = (split_lists(input))
        
        if best_split[2] == 0:
            return True
        else:
            return False
