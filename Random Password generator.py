
import random
import string

def pass_gen(length):
    lower_Alphabet = list(string.ascii_lowercase)
    upper_Alphabet = list(string.ascii_uppercase)
    Nums = list(string.digits)
    Special = ['@', '#', '&', '$']
    
    all_characters = lower_Alphabet + upper_Alphabet + Nums + Special
    final = ""
    
    for _ in range(length):
        final += random.choice(all_characters)
        
    return final
          
if (__name__ == "__main__"):
    print("----------------Random Password Generator----------------")
    response="yes"
    while response=="yes":
         length = int(input("Enter required length of the password: "))
         password = pass_gen(length)
         print(f"Password of length {length} is: {password}")
         response=input("Do you want to continue(yes/no) ?:")
