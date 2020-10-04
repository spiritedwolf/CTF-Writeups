a = open("rev_challenge_1.dat_secret.encode","rb")

#print(a.read())
#text += char((b >> 4 | (b << 4 & 0xF0)) ^ 0x29)
decode = ""
for i in bytearray(a.read()):
    decode += chr((i>>4|(i<<4&0xF0))^0x29)
    
print("".join(decode))