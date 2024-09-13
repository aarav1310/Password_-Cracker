# This is a program to crack passwords using brute force attack 
'''
Brute force attack is method that involves using trial and error method to guess the passwords, login credentials or encryption keys of the victim 

'''
import hashlib

def crack_password(hash, wordlist):    #This program will take a password hash as an input and try to decode it using the wordlist provided.
    with open(wordlist,'r')as file:
        for line in file:
            for word in line.split():
                hash_guess = hashlib.sha256(word.encode('utf-8')).hexdigest()
                if hash_guess == hash:
                    return word
    return None

password_hash='5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8'   #sample hashed password (Provide your hash code here)
wordlist='passwords.txt'            #Sample Word list in the same directory (give your password list here)

crack_password = crack_password(password_hash,wordlist)
if crack_password:
    print(f"Password cracked: {crack_password}")
else:
    print("Password not found in the word list!! Please provide another wordlist for the same.")
