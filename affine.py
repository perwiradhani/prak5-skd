import os

def egcd(a, b): 
  x,y, u,v = 0,1, 1,0
  while a != 0: 
    q, r = b//a, b%a 
    m, n = x-u*q, y-v*q 
    b,a, x,y, u,v = a,r, u,v, m,n 
  gcd = b 
  return gcd, x, y 

def modinv(a, m): 
  gcd, x, y = egcd(a, m) 
  if gcd != 1: 
    return None # modular inverse tidak ada
  else: 
    return x % m 
 
def encrypt(text, key): 
  #E = (a*x + b) % 26 
  return ''.join([ chr((( key[0]*(ord(t) - ord('A')) + key[1] ) % 26) + ord('A')) for t in text.upper().replace(' ', '') ]) 


def decrypt(cipher, key): 
  #D(E) = (a^-1 * (E - b)) % 26
  return ''.join([ chr((( modinv(key[0], 26)*(ord(c) - ord('A') - key[1])) % 26) + ord('A')) for c in cipher ]) 


def main(): 
    print("==== Affine Chiper ====")
    print("1. Enkripsi")
    print("2. Dekripsi")
    menu = input("Pilih menu : ")

    os.system("cls")

    if menu == "1":
        text = 'perwira dzakwan ramadhani'
        key = [3, 5]
        cipher = encrypt(text,key)
        print('Plain Text : ', text)
        print('Cipher Text : ', cipher)
    elif menu == "2":
        text = 'YRETDEFOCFJTFSEFPFOAFSD'
        key = [3, 5]
        decrypted = decrypt(text,key)
        print('Cipher Text : ', text)
        print('Plain Text : ', decrypted)
    else:
        print("Menu tidak tersedia")



if __name__ == '__main__': 
  main() 