#final projec: Caesar Cipher

alphabet= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y' , 'z']

should_continue = True
while should_continue:
   direction = input("Type 'encode' to encrypt type 'decode' to decrypt:\n")
   text= input("Type your message:\n").lower()
   shift = int(input("Type the shift number:\n"))
   result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
   if result == "no":
      should_continue = False
      print("Goodbye")

# def encrypt(plain_text, shift_amount):
#    cipher_text=''
#    for letter in plain_text:
#       position= alphabet.index(letter)
#       new_position = (position + shift_amount) % 26
#       new_leter= alphabet[new_position]
#       cipher_text += new_leter
#    print(f"The encoded text is: {cipher_text}")
   
# def decrypt(cipher_text, shift_amount):
#    plain_text=''
#    for letter in cipher_text:
#       position= alphabet.index(letter)
#       new_position = (position - shift_amount) % 26
#       new_leter= alphabet[new_position]
#       plain_text += new_leter
#    print(f"The decoded text is: {plain_text}")

# if direction == 'encode':
#    encrypt(plain_text=text, shift_amount=shift)
# elif direction == 'decode':
#    decrypt(cipher_text=text, shift_amount=shift) 


def ceasar(start_text,shift_amount,cipher_direcction):
   end_text=''
   if cipher_direcction == "decode":
      shift_amount *= -1
   for char in start_text:
      if char in alphabet:
       position = alphabet.index(char)
       new_position = (position + shift_amount) % 26
       end_text += alphabet[new_position]
      else:
         end_text += char
   print(f"Here's the {cipher_direcction}d result: {end_text}")