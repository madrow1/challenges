import string
import time 
from time import sleep

start_time= time.time() 

alphabet = string.ascii_lowercase + string.ascii_uppercase # "abcdefghijklmnopqrstuvwxyz"

def decrypt():
    
    encrypted_message = ("Wkh pdq lq eodfn iohg dfurvv wkh ghvhuw dqg wkh jxqvolqjhu iroorzhg. Wkh ghvhuw zdv wkh dsrwkhrvlv ri doo ghvhuwv, kxjh, vwdqglqj wr wkh vnb iru zkdw orrnhg olnh hwhuqlwb lq doo gluhfwlrqv. Lw zdv zklwh dqg eolqglqj dqg zdwhuohvv dqg zlwkrxw ihdwxuh vdyh iru wkh idlqw, forxgb kdch ri wkh prxqwdlqv zklfk vnhwfkhg wkhpvhoyhv rq wkh krulcrq dqg wkh ghylo-judvv zklfk eurxjkw vzhhw guhdpv, qljkwpduhv, ghdwk. Dq rffdvlrqdo wrpevwrqh vljq srlqwhg wkh zdb, iru rqfh wkh guliwhg wudfn wkdw fxw lwv zdb wkurxjk wkh wklfn fuxvw ri dondol kdg ehhq d kljkzdb. Frdfkhv dqg exfndv kdg iroorzhg lw. Wkh zruog kdg pryhg rq vlqfh wkhq. Wkh zruog kdg hpswlhg")
    print()
    
    print("-------------------")
    print("| Caesar Cipher   |")
    print("-------------------")


    
    for de_key in range(26):
      

        key = int(de_key)
    
        decrypted_message = ""

        for c in encrypted_message:

            if c in alphabet:
                position = alphabet.find(c)
                new_position = (position - key) % 26
                new_character = alphabet[new_position]
                decrypted_message += new_character
            else:
                decrypted_message += c

    
        print("")
        print("Enciphered: " + encrypted_message)
        print("Deciphered: " + decrypted_message)
        print("--- %s seconds ---" % (time.time() - start_time))
        print("")
    

decrypt()