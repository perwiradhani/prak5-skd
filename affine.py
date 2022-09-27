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
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    menu = input("Pilih menu : ")

    os.system("cls")

    if menu == "1":
        text = 'PERWIRADZAKWANRAMADHANI'
        key = [3, 5]
        encrypt(text,key)
    elif menu == "2":
        text = 'YRETDEFOCFJTFSEFPFOAFSD'
        key = [3, 5]
        decrypt(text,key)
    elif menu == "3":
        exit()
    else:
        print("Menu tidak tersedia")
#   text = 'YRETDEFOCFJTFSEFPFOAFSD'
#   key = [3, 5] 

#   enc_text = encrypt(text, key) #memanggil fungsi enkripsi
#   dec_text = decrypt(text, key) #memanggil fungsi dekripsi

#   print('Plain Text : ', text)
#   print('Encrypted Text: {}'.format(enc_text)) 
#   print('Decrypted Text: {}'.format(dec_text))




if __name__ == '__main__': 
  main() 