class  Message:
    
    def change(self, string, key):
        new_key = key % 26
        char_array = [''] * len(string)
        
        for i in range(len(string)):
            letter_position = ord(string[i]) + new_key
            if letter_position <= 122:
                char_array[i] = chr(letter_position)
            else:
                char_array[i] = chr(96+ letter_position %122)
        message = str(char_array)
        print(message)
        return message

encrypt = Message()

encrypt.change("abc", 25)