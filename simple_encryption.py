plain_text = " This a test. ABC abc "

encrypted_text = ""

for c in plain_text:
    x = ord ( c )
    x = x + 1
    c2 = chr ( x )
    encrypted_text = encrypted_text + c2
    print ( encrypted_text )
