class Solution:

    def get_recipient(self, message, position):
        occurence = -1
        for i in range(0,position):
            occurence = message.find("@", occurence + 1)
        
        if occurence != -1:
            output = ""
            
            for j in range (occurence+1,len(message)-1):
                if len(message) >= j+1:
                    if message[j].isalpha() or message[j].isnumeric() or message[j] == "-" or message[j] == "_" :
                        output = output + message[j]
                    else:
                        break
                else:
                    pass
        else:
            output = ""
            
        return(output)
