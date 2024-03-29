from string import ascii_lowercase
from unidecode import unidecode

#avec la table ascii
#ord --> symbole ASCII à code ASCII
#chr --> code ASCII à symbole ASCII
def ROT13(txt, n = 13, way = 'encrypt'):
    output_string = ''
    txt = unidecode(txt)
    if n > 26 or n < 1:
        print("La valeur de n est invalide")
    else:
        for i in range(len(txt)):
            char = ord(txt[i].lower())
            if char != 32:                  #gestion des espaces (code ascii du caractère ' ' --> 32)
                if way == 'encrypt':
                    char += n
                elif way == 'decrypt':
                    char -= n
                if char > 122:              #z --> 122
                    char -= 26
                elif char < 97:             #a --> 97  
                    char += 26
            output_string += chr(char)
    return output_string

if __name__ == '__main__':
    print(ROT13('Ceci est une phrase secrète'))
    print(ROT13('prpv rfg har cuenfr frpergr', 13, 'encrypt'))

# def ROT13_dict(txt, n = 13, way = 'encrypt'):  
#     table         = {letters : index for index, letters in enumerate(' ' + ascii_lowercase, start = 0)}
#     reverse_table = {letters : index for letters, index in enumerate(' ' + ascii_lowercase, start = 0)}
#     output_string  = ""
#     txt = unidecode.unidecode(txt)
#     if n > 26 or n < 1:
#         print("La valeur de n est invalide")
#     elif way != 'encrypt' and way != 'decrypt':
#        print("L'argument 'way' peut seulement être 'decrypt' ou 'encrypt'") 
#     else:
#         char_pos  = [table[letter] for letter in txt.lower() if letter in table]
#         for i in range(len(char_pos)):
#             if char_pos[i] != 0:
#                 if way == 'encrypt':
#                     char_pos[i] += n
#                 elif way == 'decrypt':
#                     char_pos[i] -= n
#                     if char_pos[i] < 0:
#                         char_pos[i] += 26
#                 if char_pos[i] > 26:
#                     char_pos[i] -= 26
#         nb_pos  = [reverse_table[number] for number in char_pos if number in reverse_table]
#         for i in range(len(char_pos)):    
#             output_string += str(nb_pos[i])
# print(output_string)