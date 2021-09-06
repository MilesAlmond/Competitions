class AttackCleanup:

    
    def restore_data(self, message):
        
        output = ''
        
        for i in range(len(message)):
            
            if i == 0:
                
                if message[i].isnumeric():
                    output = output + message[i]
                elif message[i] == "z":
                    output = output + "a"
                elif message[i] == "g":
                    output = output + "t"
                elif message[i] == "t":
                    output = output + "g"
                elif message[i] == "x":
                    output = output + "c"
                else:
                    continue
                    
            elif message[i-1].isnumeric():
                
                if message[i].isnumeric():
                    if message[i+1] == "z":
                        output = output + 10*int(message[i-1])*"a"
                    elif message[i+1] == "g":
                        output = output + 10*int(message[i-1])*"t"
                    elif message[i+1] == "t":
                        output = output + 10*int(message[i-1])*"g"
                    elif message[i+1] == "x":
                        output = output + 10*int(message[i-1])*"c"
                    else:
                        continue
                
                else:
                    
                    if message[i] == "z":
                        output = output + int(message[i-1])*"a"
                    elif message[i] == "g":
                        output = output + int(message[i-1])*"t"
                    elif message[i] == "t":
                        output = output + int(message[i-1])*"g"
                    elif message[i] == "x":
                        output = output + int(message[i-1])*"c"
                    else:
                        continue
            else:
                
                if message[i] == "z":
                    output = output + "a"
                elif message[i] == "g":
                    output = output + "t"
                elif message[i] == "t":
                    output = output + "g"
                elif message[i] == "x":
                    output = output + "c"
                else:
                    continue
            
        return output
