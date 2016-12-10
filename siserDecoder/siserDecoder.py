def decode_siser_str(str_encoded, siser_key):
    if siser_key < 0:
        siser_key = siser_key % 26
    
    str_decoded = ""
    m = 0
    v = 0
    for x in str_encoded:
        n = ord(x)
        if x.isalpha():
            m = n
            v = 0
            n += siser_key

        if (m >= ord("A")) and (m <= ord("Z")):
            if n > ord("Z"):
                v = n - ord("Z")
                v = v % 26
                n = ord("A") + v - 1
                        
        elif (m >= ord("a")) and (m <= ord("z")):
            if n > ord("z"):
                v = n - ord("z")
                v = v % 26
                n = ord("a") + v - 1
                    
        str_decoded = str_decoded + chr(n)

    return str_decoded
