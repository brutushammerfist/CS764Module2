# CS764 - Module 2
Homework for CS764 - Module 2

## Question 1

The file ```question1.py``` within the Question1 folder holds the encryption method used to generate the hashes in the Merkle tree for the homework.

## Question 2

The file ```question2.py``` within the Question2 folder generates the DES and RSA keys that used to encrypt and decrypt the message, "This is fun". The syntax for running the script is as follows:

```
python question2.py {key-type}
```

Examples:

```
python question2.py des
        OR
python question2.py rsa
```

The output of the script is dependent upon the {key-type} parameter. If ```des``` is chosen, the original data, key, encrypted data, and decrypted data are all displayed to the terminal. Likewise, if ```rsa``` is input, the original data, encrypted data, and decrtyped data are all displayed, alongside both the public and private keys.