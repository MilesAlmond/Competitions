class PairValidator:

    def validate(self, input, input2):
        if len(input) != len(input2):
            return False
        else:
            out2 = True
            for char in input:
                out = False
                for i in range(len(input2)):
                    if char == input2[i]:
                        out = True
                        input2 = input2[:i] + input2[i+1:]
                        break
                    elif input2[i] in [chr(ord(char)-1),chr(ord(char)+1)]:
                        out = True
                        input2 = input2[:i] + input2[i+1:]
                        break
                    else:
                        pass
                out2 = out2 and out
            return out2
                    
                    
                        
