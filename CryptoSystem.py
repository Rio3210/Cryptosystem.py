from string import punctuation #important module which wil be used to include the punctuations with in the plain text or cipher text. 
class AffineCipher:
    def __init__(self):
        self.plaintext=None
        self.a=0
        self.b=0
    def GCDIN(self,a, b):   #This function finds both the gcd and multiplicative inverses
        x,y, u,v = 0,1, 1,0
        while a != 0:
            q = b//a
            r = b%a
            m = x-u*q
            n =  y-v*q
            b,a, x,y, u,v = a,r, u,v, m,n
        gcd = b
        return gcd, x, y
    
    def a_modinv(self,a, m):  #This code is to find the inverse of mod inverse of a 
        
        gcd, x, y =self.GCDIN(a, m)
        if gcd != 1:
            return None  # modular inverse does not exist
        else:
            return x % m

    #Encryption
    def encryption(self,plaintext, a, b): 
        result = ""
       # punctuation=['"',',','.','!','?',"'"] # this is to include the punctuation that are in the plaintext 
        for i in range(len(plaintext)):
            character = plaintext[i]
    
            # Code to Encrypt uppercase characteracters
            if (character.isupper()):
                result += chr((a *(ord(character)-ord('A')) +b)%26+ord('A'));
    
            #Code to Encrypt lowercase characteracters
            elif (character.islower()):
                result += chr((a *(ord(character)-ord('a')) +b)%26+ord('a'));
            
            # This code is for the space
            elif character==" ":
                result+=" "
            elif character in punctuation:
                result+=character
            else:           
                continue;
        return result

    #Decryption

    def decryption(self,ciphertext, a, b):
        result = ""
        a_inverse= self.a_modinv(a, 26)
        for i in range(len(ciphertext)):
            character = ciphertext[i]
            # Encrypt uppercase characteracters
            if (character.isupper()):
                result += chr(a_inverse *(ord(character)-ord('A') -b)%26+ord('A'))
    
            # Encrypt lowercase characteracters
            elif (character.islower()):
                result += chr((a_inverse *(ord(character)-ord('a') -b))%26+ord('a'))
            
            elif character==" ":
                result+=" "
            elif character in punctuation:
                result+=character
            else: 
                continue; 
        return result

#Transposition Cipher (We implemented the columnar Transposition)
import random
from string import ascii_uppercase
class Transposition:
    def __init__(self) :
        pass    
    def merge_elt(self,list_of_blocks,temp=None):    # a function takes a temp conditionally to add between two elements to be merged
        merged = ""
        if temp == None:
            for block in list_of_blocks:
                merged += block
        else:
            for block in list_of_blocks:
                merged += block
                merged += temp
        return merged

    # a function that mixes a given string given a key that states how to mix.
    # the key is a two dimensional array with each inner list having two elements that indicate
    # the destination index and initial starting index.
    def permute(self,string,key,Intetion):
        if Intetion == "To_encrypt":
            destination, starting = 1,0
        elif Intetion == "To_decrypt":
            destination, starting = 0,1
        uncipherd = []
        cipherd = [None]*len(string)
        for i in string:
            uncipherd += i
        for i in key:
            cipherd[i[destination]-1] = uncipherd[i[starting]-1]
        permuted = ''
        for i in cipherd:
            permuted+=i
        return permuted

    # a function to encrypt a string, takes the string, block_size that specifies how long the divided string should be and a key that encryptes the string in a specific way. 
    # the key used here is a 2D list(we used the example 6 from our text book p.313 to generate the key with block size of 4)
    def encrypt(self,string, block_size,key):
        # removing spaces from the string and makes it uppercase (which is important for the encryption process)
        string = string.replace(" ", "").upper()
        # checks weather the string size is divisible by the block size and if not adding random letter from the alphabet
        alphabet=list(ascii_uppercase)
        if len(string)%block_size==0:
            pass
        else:
            left_over = len(string)%block_size
            ran_letter = random.choices(alphabet, k=block_size-left_over)
            filler = self.merge_elt(ran_letter)
            string += filler
        
        unencrypted_list = []
        while string != "":
            unencrypted_list.append(string[0:block_size])
            string = string[block_size:]

        # encrypting each element of the unencrypted_list using the permute function and storing them in theencrypted blocks list. 
        encrypted_list = []
        for block in unencrypted_list:
            encrypted = self.permute(block, key, "To_encrypt")
            encrypted_list.append(encrypted)

        # returning encrypted_list list by merging its elemnts using the merge function.
        return self.merge_elt(encrypted_list, " ")

    # a function to decrypt a string takes the string, block length and a key that describes how the string was encrypted.
    #Since most of the operation in encryption is the same as decryption no need to explain each process
    def decrypt(self,string,block_size,key):
        string = string.replace(" ", "")
        undecrypted_list = []
        while string != "":
            undecrypted_list.append(string[0:block_size])
            string = string[block_size:]
        decrypted_list= []
        for block in undecrypted_list:
            decrypted = self.permute(block, key, "To_decrypt")
            decrypted_list.append(decrypted)
        return self.merge_elt(decrypted_list, " ")
class RSA:
  def __init__(self):
    pass
  def isPrime(self,num):  # checks whether a number is a prime or not
      flag=True
      if num>1:
        for i in range(2,num):
          if (num%i)==0:
            flag=False
            break
        return flag
  def gcd(self,m,n): # finds the gcd of number using Ecludian algorithm
    if m< n:
        (m,n) = (n,m)
    if(m%n) == 0:
        return n
    else:
        return (self.gcd(n, m % n))
  def generate_key_pair(self,p, q):   # This function is used to find the public key and private key with the given primeNumbers
      if not (self.isPrime(p) and self.isPrime(q)):
          raise ValueError("NUMBER MUST BE PRIME")
      elif p == q:
          raise ValueError("THE PRIMES DON'T HAVE TO BE THE SAME")
      n = p * q

      phi = (p-1) * (q-1)

      e = random.randrange(1, phi)

      g = self.gcd(e, phi)
      while g != 1:
          e = random.randrange(1, phi)
          g = self.gcd(e, phi)

      d = self.multiplicative_inverse(e, phi)

      return ((e, n), (d, n))

  def multiplicative_inverse(self,e, phi):
      d = 0
      x1 = 0
      x2 = 1
      y1 = 1
      temp_phi = phi

      while e > 0:
          temp1 = temp_phi // e
          temp2 = temp_phi - temp1 * e
          temp_phi = e
          e = temp2

          x = x2 - temp1 * x1
          y = d - temp1 * y1

          x2 = x1
          x1 = x
          d = y1
          y1 = y

      if temp_phi == 1:
          return d + phi
    #This code is to encrypt the given plain text
  def encrypt(self,public_key, plaintext):
      key, n = public_key
      cipher = [pow(ord(character), key, n) for character in plaintext]
      return cipher

  #This code is to decrypt the given plain text
  def decrypt(self,private_key, ciphertext):
      key, n = private_key
      dba = [str(pow(character, key, n)) for character in ciphertext]
      plainText = [chr(int(character2)) for character2 in dba]
      return ''.join(plainText)

#Main function 
def main():
    print("Welcome to the  Cipher World!!!!!!!")
    value=int(input("Press1:For Encryption \nPress2: For Decryption \n"))
    Aff=AffineCipher()
    Trans=Transposition()
    RSa=RSA()
    if value==1:
        print("In which Cryptosystem you want to Encript: ")
        value2=int(input("press\n 1.AffineCipher\n 2.TranspositonCipher\n 3.RSA Cryptosystem\n"))
        if value2==1:
            
            plaintext= input("Enter the plaintext to encrypt using affine cipher : \n")
            print("Assuming the format a*(plaintext)+b")
            a= int(input("Enter the a: \n"))
            b= int(input("Enter the b: \n"))
            print("Ciphertext:",Aff.encryption(plaintext,a,b))
            print("Thankyou for working with us")
        elif value2==2:
            OrginalText=input("Enter the Plain text you want to Encriypt: \n")
            key = [[1,3],[2,1],[3,4],[4,2]]
            print("Ciphertext:",Trans.encrypt(OrginalText,4,key))
            print("Thankyou for working with us")
        elif value2==3:
            print("To generate the private and public keys insert two prime numbers which are greater than 7\n") 
            p = int(input("Enter the 1st prime number\n"))
            q=int(input("Enter the 2nd prime number\n"))
            if p>7and q>7:  # limited the primes because for a prime less than or equal to 7 the generated private key is not unique.
                public, private = RSa.generate_key_pair(p, q)
                print("Public key: ", public)
                print("Private key: ", private)

                message = input("Enter the message ")
                encrypted_msg = RSa.encrypt(public, message)

                print("The Encrypted Message is ", ''.join(map(lambda x: str(x) + " ", encrypted_msg)))
                print("Remember the private key because it's vital to decrypt the upper Cipher Code, Thanks for woking with us ")
            else:
                print("Your input are not primes, please make sure the primes are greater than 7")

        else:
            print("Invalid input ;) ")
    elif value==2:
        value3=int(input("press\n 1.AffineCipher\n 2.TranspositonCipher\n 3.RSA Cryptosystem\n"))
        if value3==1:

            ciphertext= input("Enter the ciphertext to decrypt in affine cipher ): \n")
            print("Assuming the format a^-1(*(plaintext)-b")
            a= int(input("Enter the a: \n"))
            b= int(input("Enter the b: \n"))
            print ("Ciphertext:",ciphertext)
            print ("Plaintext:",Aff.decryption(ciphertext,a,b))
            print("Thankyou for working with us :)")
        elif value3==2:
            EncryptedText=input("Enter the Cipher text you want to decrypt: \n")
            key = [[1,3],[2,1],[3,4],[4,2]]
            dec_text=Trans.decrypt(EncryptedText,4,key) #In the out put there may be some additional characters which were added during the encription process
            print("The decrypted plain text",dec_text)
            print("Thankyou for working with us :)")
        elif value3==3:
            private=tuple(map(int, input("Enter Private Key(Just simply give space b/n the two numbers): ").split())) #This code accepts private key from the user and add them in to a tuple
            encrypted_msg=list(map(int,input("please,Enter the encrypted Code(Just simply give space b/n the numbers): ").split()))#This code accepts cipher code(Text) from the user and add them in to a list
            print("The Decrypted Message is: ", RSa.decrypt(private, encrypted_msg))
            print("Thankyou for working with us :)")
        else:
            print("Invalid input ;) ")
    else:
            print("Invalid input ;)...try again ")
        
if __name__=='__main__':
    main()
