
import random

buyuk_harfler = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
kucuk_harfler = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
yaygin_isaretler = ['.', ',', ';', ':', '!', '?', '-', '_', '(', ')', '[', ']', '{', '}', '"', "'", '/', '\\', '@', '#', '$', '%', '^', '&', '*']


tum_harfler = buyuk_harfler + kucuk_harfler + yaygin_isaretler 

uzunluk = 15

cekilenler = set()

sifre = []

while len(sifre) < uzunluk:
    rastgele_harf = random.choice(tum_harfler)

    if rastgele_harf not in cekilenler:
        sifre.append(rastgele_harf)  
        cekilenler.add(rastgele_harf)  

print("Oluşturulan şifre =>", ''.join(sifre))

