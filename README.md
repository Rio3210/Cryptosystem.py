# Cryptosystem.py
1.Affine Cipher
-The affine cipher is a type of monoalphabetic substitution cipher, where each letter in an alphabet is mapped to 
 its numeric equivalent, encrypted using a simple mathematical function, and converted back to a letter.  
 The formula used means that each letter encrypts to one other letter, and back again, meaning the cipher is
 essentially a standard substitution cipher with a rule governing which letter goes to which.
 Since the affine cipher encryption/decryption process is substantially mathematical, 
 the whole process relies on working modulo m (the length of the alphabet used). By performing a calculation on the plaintext letters, 
 we can encipher the plaintext.
#Encryption:
-The first step in the encryption process is to transform each of the letters in the plaintext alphabet 
 to the corresponding integer in the range 0 to m-1. With this done, the encryption process for each letter
 is given by E(x)=(ax + b)mod m where a and b are the key for the cipher. This means that we multiply our 
 integer value for the plaintext letter by a, and then add b to the result. Finally, we take this modulus m 
 (that is we take the remainder when the solution is divided by m, or we take away the length of the alphabet 
 until we get a number less than this length).
#Decryption:
In deciphering the ciphertext, we must perform the opposite (or inverse) functions on the ciphertext 
to retrieve the plaintext. Once again, the first step is to convert each of the ciphertext letters 
into their integer values. We must now perform the following calculation on each integer D(x) = n(x−b) mod m
where n is the modular multiplicative inverse of a. That is, a × n = 1 mod m (n is the number such that 
when you multiply a by it, and keep taking away the length of the alphabet, you get to 1).
------------------------------------------------------------------------------------------------------------------------
2.Transposition cipher
#Transposition Cipher is a cryptographic algorithm where the order of alphabets in the plaintext is rearranged 
 to form a cipher text.  Transposition ciphers reorder units of plaintext (typically characters or groups of 
 characters) according to a regular system to produce a ciphertext which is a permutation of the plaintext. 
 The cipher is written vertically, which creates an entirely different cipher text. It is writing the plaintext out
 in rows, and then reading the ciphertext off in columns one by one.
#Encryption:
-The message is written out in rows of a fixed length, and then read out again column by column, and the columns
 are chosen in some scrambled order.
-  Width of the rows and the permutation of the columns are usually defined by a keyword.
-  For example, the word HACK is of length 4 (so the rows are of length 4), and the permutation is defined by
 the alphabetical order of the letters in the keyword. In this case, the order would be “3 1 2 4”.
-  Finally, the message is read off in columns, in the order specified by the keyword.
#Decryption: 
-  To decipher it, the recipient has to work out the column lengths by dividing the message length by the key length.
-  Then, write the message out in columns again, then re-order the columns by reforming the key word.
--------------------------------------------------------------------------------------------------------------------------------------
3.RSA Cryptosystem
#In mathematics, the fundamental Euclidean theorem of arithmetic, also called the unique factorization theorem 
 and prime factorization theorem, states that every integer greater than 1 can be represented uniquely as 
 a product of prime numbers, up to the order of the factors. Using this Euclidean theorem and 
 Euler’s theorem (if n and a are coprime positive integers, and φ(n) is Euler’s totient function, then a raised 
 to the power φ(n)is congruent to 1 modulo n) concept Rivest, Shamir and Adleman in year 1978 invented
 new cryptography algorithm system called RSA.
#RSA algorithm is asymmetric cryptography algorithm (means that it works on two different keys i.e.,
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
