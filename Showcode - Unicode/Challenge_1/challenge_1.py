class Cipher:

    def halliday(self, message):
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        ciphertext = ""
        for character in message:
            if character.isalpha():
                if character.isupper():
                    key = 1
                else: 
                    key = 0
                character = character.lower()
                char_index = alphabet.index(character)
                new_index = (char_index + 13) % 26
                if key == 1:
                    cipher_char = alphabet[new_index].upper()
                else:
                    cipher_char = alphabet[new_index]
            else:
                cipher_char = character
            
            ciphertext += cipher_char
            
        return(ciphertext)
