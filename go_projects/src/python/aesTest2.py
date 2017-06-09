from cryptography.fernet import Fernet

from Crypto.Cipher import AES
import base64


key = Fernet.generate_key() #this is your "password"
cipher_suite = Fernet(key)

encoded_text = cipher_suite.encrypt(b"Hello stackoverflow!")
decoded_text = cipher_suite.decrypt(encoded_text)


print("key = : ",key)
print("encoded_text = : ",encoded_text)
print("decoded_text = : ",decoded_text)

#print "encoded_text = : ",encoded_text   
#print "See result using inbuilt method capitalize() = : ",encoded_text
#print "key = : ",key






msg_text = 'test some plain text here cipher_suite.encrypt'.rjust(32)
secret_key = '1234567890123456' # create new & store somewhere safe

cipher = AES.new(secret_key,AES.MODE_ECB) # never use ECB in strong systems obviously
encoded = base64.b64encode(cipher.encrypt(msg_text))
# ...
decoded = cipher.decrypt(base64.b64decode(encoded))
print ("34. encoded = : ",encoded.strip())
print ("35. Decoded = : ",decoded.strip())

