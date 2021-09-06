class Solution:

    def parse_roman_numerals(self, input):
        
        new = list()
        
        for char in input:
            if char == "M":
                new.append(1000)
            elif char == "D":
                new.append(500)
            elif char == "C":
                new.append(100)
            elif char == "L":
                new.append(50)
            elif char == "X":
                new.append(10)
            elif char == "V":
                new.append(5)
            elif char == "I":
                new.append(1)
            else:
                new.append(0)
                break
        
        result = new[:]
            
        for i in range(0,len(new)-1):
            if new[i] == new[i+1]:
                result[i+1] = result[i] + result[i+1]
                result[i] = 0
            
            elif new[i] < new[i+1]:
                result[i] = -result[i]
                
            else:
                pass
            
        return(sum(result))
