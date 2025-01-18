# Program: Secure Password Generator
# Entropy: The entropy of a password is based
#  on the number of characters each space can have * the number of spaces (length)
import random as rd
import string as str

def password_gen():
    pwd_len = rd.randint(8, 16)
    pwd_char_low = str.ascii_lowercase
    pwd_char_up = str.ascii_uppercase
    pwd_char_dig = str.digits
    pwd_char_pnt = str.punctuation
    pwd_char = pwd_char_low + pwd_char_up + pwd_char_dig + pwd_char_pnt
    pwd = ''
    possition = rd.sample(range(1, pwd_len), 4)
    for i in range(pwd_len):
        if (i == possition[0]):
            pwd = pwd + rd.choice(pwd_char_low)
        elif (i == possition[1]):
            pwd = pwd + rd.choice(pwd_char_up)
        elif (i == possition[2]):
            pwd = pwd + rd.choice(pwd_char_dig)
        elif (i == possition[3]):
            pwd = pwd + rd.choice(pwd_char_pnt)
        else:
            pwd = pwd + rd.choice(pwd_char)
    return(pwd)
    
def main():
    print(password_gen())

if __name__ == "__main__":
    main()