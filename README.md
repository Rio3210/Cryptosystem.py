# Cryptosystem.py
Public Key and Private Key). This cipher works as follows;                           
 Let, client (for example a browser) sends its public key to the server and requests for some data, 
 then the server encrypts the data using client’s public key and sends the encrypted data and finally 
 the client receives this data and decrypts it. 
#RSA algorithm uses the following procedure to generate public and private keys:
-Select two large prime numbers, p and q.
-Multiply these numbers to find n = p x q, where n is called the modulus for encryption and decryption.
-Choose a number e less than n, such that n is relatively prime to (p - 1) x (q -1). It means that 
 e and (p - 1) x (q - 1) have no common factor except 1. Choose "e" such that 1<e < φ (n), e is prime to φ(n), gcd (e, d(n)) =1
-If n = p x q, then the public key is <e, n>. A plaintext message m is encrypted using public key <e, n>. 
 To find ciphertext from the plain text following formula is used to get ciphertext(C). 
 C=me mod(n) Here, m must be less than n. A larger message (>n) is treated as a concatenation of messages, each of which is encrypted separately.
-To determine the private key, we use the following formula to calculate the d such that:
 De mod{(p-1) x(q-1)} =1 Or De mod φ (n) = 1
-The private key is <d, n>. A ciphertext message c is decrypted using private key <d, n>. 
To calculate plain text m from the ciphertext c following formula is used to get plain text m. m = cd mod n

#################################################################################################################
" How to run the Program ?????"
-While you run the Cryptosystem.py you will face 2 options that ask you whether you want to encrypt or decrypt.
-After you make descion ,again you wil face three options that ask you to enter the type of
 Cryptosystem that you want to encrypt or decrypt.

## Know let's discuss how each Cryptosystem in this program works
---------------------------------------------------------------------------------------------------------------------
1. Affine cipher
1.1Affine Encryption:
-First it ask you to insert the plain text.
-After that it will ask you for the value of a and b (which is in format of a*(plaintext)+b)
-Finally it will display you with the cipher text

1.2Affine Decryption:
-The process is almost the same as the encryption process except 
 the plaintext is cipher text and the form is a^-1(*(plaintext)-b
---------------------------------------------------------------------------------------------------------------------
2.Transposition cipher
2.1 Transposition Encryption
-it will ask you to insert the plain text that you want to decrypt
-Since the key and the block size are automatically inserted. It doesn't ask a user to fill them.
-Finally it will reveal the cipher text 
2.2 Transposition Decryption
The process is almost the same as the Encryption.It will ask you the cipher text.
But know that the plain text will be sorted equal with the length of the block size.
Thus, there may be some additional characters which are not significant.
-------------------------------------------------------------------------------------------------------------------
3.RSA Cryptosystem 
3.1 RSA Encryption
-First the program will ask you to insert two prime numbers 
 which help in generating the keys(public and private keys)
-After that it will display the public and the private keys in the consol, then ask you to enter the plaintext.
 Since in our program we intentionally make it to insert the public key automatically. It will simply ask you to insert the plaintext.
-Finally, it will display the encripted message and warns a user not to forgot the private key.
3.2 RSA Decryption
-Initially it will ask you to insert the private key 
-Then after it will ask you the encrypted message 
-Finaly it will pop up with the plaintext(decrypted message)
----------------------------------------------------------------------------------------------------------------------
