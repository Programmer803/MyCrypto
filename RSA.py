import rsa

def Generate_key():
    (publickey, privatekey) = rsa.newkeys(2048)

    return privatekey , publickey 


def enc(message , pubkey):

    return rsa.encrypt(str(message).encode() , pubkey)

def dec(message , prikey):

    return str(rsa.encrypt(message , prikey)).decode()