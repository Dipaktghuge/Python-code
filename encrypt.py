def encrypt(text, key="dddddddddddddddddddd"):
    if len(key)<len(text):
        key=key*3
    if key =="":
        raise ValueError("key cannot be empty")
    eng_ab="abcdefghijklmnopqrstuvwxyz"
    cipher=" "
    for i , char in enumerate(text):
        step= eng_ab.index(key[i])
        pos=eng_ab.index(char)
        new_pos=pos+step
        cipher=cipher + eng_ab[new_pos]
    return cipher
print(encrypt("dontlookup"))
print(encrypt("aaaaaaaaaa","aaaaaaaaaa"))
print(encrypt("abcdefghij","abcdefghij"
))
def decrypt(text, key="dddddddddddddddddddd"):
    if len(key)<len(text):
        key=key*3
    if key =="":
        raise ValueError("key cannot be empty")
    eng_ab="abcdefghijklmnopqrstuvwxyz"
    plain=" "
    for i , char in enumerate(text):
        step= eng_ab.index(key[i])
        pos=eng_ab.index(char)
        new_pos=pos-step
        plain=plain + eng_ab[new_pos]
    return plain
print(decrypt("dontlookup"))
