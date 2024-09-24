FINAL_STATES = {12, 15, 18, 19, 20}

class URLValidatorDFA:
    def __init__(self):
        self.current_state = 0

    def reset(self):
        self.current_state = 0

    def is_letter(self, char):
        return 'a' <= char <= 'z' or 'A' <= char <= 'Z'
    
    def all_letters_except(self, char, exceptLetters):
        return ('a' <= char <= 'z' or 'A' <= char <= 'Z') and char not in exceptLetters
    
    def is_valid_number(self, char):
        return char == '0' or char == '1' or char == '2' or char == '3' or char == '4' or char == '5' or char == '6' or char == '7' or char == '8' or char == '9'
    
    def is_special_characters(self, char):
        return char == '-' or char == '_' or char == '~'
    
    def transition(self, char):
        if self.current_state == 0:
            if char == 'h':
                self.current_state = 1
                return True        
        elif self.current_state == 1:
            if char == 't':
                self.current_state = 2
                return True
        elif self.current_state == 2:
            if char == 't':
                self.current_state = 3
                return True
        elif self.current_state == 3:
            # http
            if char == 'p':
                self.current_state = 4  
                return True
        elif self.current_state == 4:
            # https
            if char == 's':
                self.current_state = 5 
                return True
            # http:
            elif char == ':':
                self.current_state = 6 
                return True
        elif self.current_state == 5:
            # https:
            if char == ':':
                self.current_state = 6
                return True
        elif self.current_state == 6:
            # https:/ o http:/
            if char == '/':
                self.current_state = 7
                return True
        elif self.current_state == 7:
            # https:// o http://
            if char == '/':
                self.current_state = 8
                return True  
        elif self.current_state == 8:
            # https://fafae o http://fafea
            if self.is_letter(char) or self.is_valid_number(char):
                self.current_state = 21
                return True
            elif char == '.':
                # https://fafae. o http://fafea.
                self.current_state = 9
                return True
        elif self.current_state == 9:
            # https://fafae.fsafs o http://fafea.fsafsa
            if self.all_letters_except(char, {'c', 'o', 'n'}) or self.is_valid_number(char):
                self.current_state = 21
                return True
            # https://fafae.c o http://fafea.c
            elif char == 'c':
                self.current_state = 10
                return True
            # https://fafae.o o http://fafea.o
            elif char == 'o':
                self.current_state = 13
                return True
            # https://fafae.n o http://fafea.n
            elif char == 'n':
                self.current_state = 16
                return True
        elif self.current_state == 10:
            if self.all_letters_except(char, {'o'}) or self.is_valid_number(char) or self.is_special_characters(char):
                self.current_state = 22
                return True
            # https://fafae.co o http://fafea.co
            elif char == 'o':
                self.current_state = 11
                return True
        elif self.current_state == 11:
            if self.all_letters_except(char, {'m'}) or self.is_valid_number(char) or self.is_special_characters(char):
                self.current_state = 22
                return True
            # https://fafae.com o http://fafea.com
            elif char == 'm':
                self.current_state = 12
                return True
        elif self.current_state == 12:
            if self.is_letter(char) or self.is_valid_number(char) or self.is_special_characters(char):
                self.current_state = 22
                return True
            # https://fafae.com/ o http://fafea.com/
            elif char == '/':
                self.current_state = 19
                return True
        elif self.current_state == 13:
            if self.all_letters_except(char, {'r'}) or self.is_valid_number(char) or self.is_special_characters(char):
                self.current_state = 22
                return True
            # https://fafae.or o http://fafea.or
            elif char == 'r':
                self.current_state = 14
                return True
        elif self.current_state == 14:
            if self.all_letters_except(char, {'g'}) or self.is_valid_number(char) or self.is_special_characters(char):
                self.current_state = 22
                return True
            # https://fafae.org o http://fafea.org
            elif char == 'g':
                self.current_state = 15
                return True
        elif self.current_state == 15:
            if self.is_letter(char) or self.is_valid_number(char) or self.is_special_characters(char):
                self.current_state = 22
                return True
            # https://fafae.org/ o http://fafea.org/
            elif char == '/':
                self.current_state = 19
                return True
        elif self.current_state == 16:
            if self.all_letters_except(char, {'e'}) or self.is_valid_number(char) or self.is_special_characters(char):
                self.current_state = 22
                return True
            # https://fafae.ne o http://fafea.ne
            elif char == 'e':
                self.current_state = 17
                return True
        elif self.current_state == 17:
            if self.all_letters_except(char, {'t'}) or self.is_valid_number(char) or self.is_special_characters(char):
                self.current_state = 22
                return True
            # https://fafae.net o http://fafea.net
            elif char == 't':
                self.current_state = 18
                return True
        elif self.current_state == 18:
            if self.is_letter(char) or self.is_valid_number(char) or self.is_special_characters(char):
                self.current_state = 22
                return True
            # https://fafae.net/ o http://fafea.net/
            elif char == '/':
                self.current_state = 19
                return True
        elif self.current_state == 19:
            # https://fafae.net/feaf o http://fafea.net/faef
            # https://fafae.com/feaf o http://fafea.com/feaf
            # https://fafae.org/feaf o http://fafea.org/feaf
            if self.is_letter(char) or self.is_valid_number(char):
                self.current_state = 20
                return True
        elif self.current_state == 20:
            # https://fafae.net/feaf/ o http://fafea.net/faef/
            # https://fafae.com/feaf/ o http://fafea.com/feaf/
            # https://fafae.org/feaf/ o http://fafea.org/feaf/
            if self.is_letter(char) or self.is_valid_number(char):
                return True
            elif char == '/' or self.is_special_characters(char):
                self.current_state = 19
                return True
        elif self.current_state == 21:
            if self.is_letter(char) or self.is_valid_number(char):
                return True
            elif self.is_special_characters(char):
                self.current_state = 22
                return True
            elif char == '.':
                self.current_state = 9
                return True
        elif self.current_state == 22:
            if self.is_letter(char) or self.is_valid_number(char):
                self.current_state = 21
                return True
        
        # Transición fallida, rechaza la URL
        return False

    def is_valid_url(self, text):
        self.reset()
        self.text = text
        self.current_pos = 0  # Posición actual en la cadena

        for char in text:
            if not self.transition(char):
                return False
            self.current_pos += 1
        print(self.current_state)
        # Verificar si terminó en un estado de aceptación
        return self.current_state in FINAL_STATES