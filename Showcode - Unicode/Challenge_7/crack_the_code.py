class Solution:

    def cipher(self, input, key):
        result = ""
        new_key = key%26
        for i in input:
            
            if i.isalpha():
                if 65 <= ord(i) <= 90:
                    if new_key+ord(i) > 90:
                        decode = chr(ord(i)-(26-new_key))
                        result += decode
                    else:
                        decode = chr(ord(i)+new_key)
                        result += decode
                elif 97 <= ord(i) <= 122:
                    if new_key+ord(i) > 122:
                        decode = chr(ord(i)-(26-new_key))
                        result += decode
                    else:
                        decode = chr(ord(i)+new_key)
                        result += decode
                else:
                    result += i
            else:
                result += i
        
        return(result)
