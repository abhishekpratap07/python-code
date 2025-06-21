alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
             'u', 'v', 'w', 'x', 'y', 'z']

descrption = input("type encode to encrypt or decode for decrypt\n")
text = input("type the message\n").lower()
shift = int(input("type shift number\n"))

def encryption(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        if letter in alphabets:
            shifted_position = (alphabets.index(letter) + shift_amount) % len(alphabets)
            cipher_text += alphabets[shifted_position]
        else:
            cipher_text += letter
    print(f"this is your encode result: {cipher_text}")   
 
def decryption(original_text, shift_amount):
    outer_text = ""
    for letter in original_text:
        if letter in alphabets:
            shifted_position = (alphabets.index(letter) - shift_amount) % len(alphabets)
            outer_text += alphabets[shifted_position]
        else:
            outer_text += letter
    print(f"this is your decode result: {outer_text}")   

def caser(direction):
    if direction == "encode":
        encryption(original_text=text, shift_amount=shift)
    elif direction == "decode":
        decryption(original_text=text, shift_amount=shift)
    else:
        print("Invalid input. Type 'encode' or 'decode'.")

caser(direction=descrption)
