class Solution:

    def is_prime(self, input):
        answer = True
        for i in range(2,input):
            if input%i == 0:
                answer = False
                break
            else:
                continue
        
        return answer
