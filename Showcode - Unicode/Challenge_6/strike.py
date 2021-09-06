class Solution:

    def get_score(self, input):
        i = 0
        p = len(input) - 1
        frame = []
        while i < len(input) and len(frame) <= 10:
            if len(frame) == 9:
                
                for n,q in enumerate(input[i:]):
                    if q == "X":
                        input[i+n] = 10
                        
                    if q == "/":
                        input[i+n] = 10 - int(input[n-1])
                        print(input[n])
                        print(input[i:])
                        print(input)
                
                if i+2 == p:      
                
                    frame.append((input[i],input[i+1],input[i+2]))
                    break
                
                elif i+1 == p:
                    
                    frame.append((input[i],input[i+1]))
                    break
                
            else:
                if input[i] == "X":
                    frame.append([10])
                    i = i+1
                    continue
                
                elif input[i+1] == "/":
                    frame.append((input[i],10 - int(input[i])))
                    i = i+2
                    continue
                    
                else:
                    frame.append((input[i],input[i+1]))
                    i = i+2
                    continue
        
        print(frame)
        score = [0,0,0,0,0,0,0,0,0,0]
        
        
        for j in range(0,10):
            
            for i in range(0,len(frame[j])):
                
                score[j] = score[j] + int(frame[j][i])
            
            if frame[j-1] == [10]:
                score[j-1] = score[j-1] + score[j]
            
            elif score[j-1] == 10:
                score[j-1] = score[j-1] + int(frame[j][0])
            
            print(score)
            
        
        final = sum(score)
        
        return(final)
                    
