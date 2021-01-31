import pyDes
import rsa
import sys

if __name__ == "__main__":
    data = "This is fun".encode("ascii", "ignore")
    
    print("Original data: " + str(data) + "\n")
    
    if sys.argv[1] == "des":
        des = pyDes.des("DESCRYPT", pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
        print("Key: " + str(des.getKey()) + "\n")
        encrypted_data = des.encrypt(data)

        print("Encrypted data: " + str(encrypted_data) + "\n")
        print("Decrypted data: " + str(des.decrypt(encrypted_data)) + "\n")
    elif sys.argv[1] == "rsa":
        (pub, priv) = rsa.newkeys(512)

        print("Public Key: " + str(pub.save_pkcs1()) + "\n")
        print("Private Key: " + str(priv.save_pkcs1()) + "\n")

        encrypted_data = rsa.encrypt(data, pub)

        print("Encrypted data: " + str(encrypted_data) + "\n")
        print("Decrypted data: " + str(rsa.decrypt(encrypted_data, priv)) + "\n")