import re
import string
import secrets

counter=0
def get_string(length):
    all_digit=string.digits
    all_alpha=string.ascii_letters
    all_char=string.punctuation
    all_letter=all_alpha+all_char+all_digit
    return ("".join(secrets.choice(all_letter) for i in range(length)))


   

def get_same_string(rule):
    """checking purpose"""
    while True:
        global counter
        counter+=1
        res=re.search(rule,get_string())

print(get_string(6))
