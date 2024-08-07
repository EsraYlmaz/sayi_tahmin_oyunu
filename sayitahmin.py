import random

alt_sinir = int(input("Alt sınırı giriniz:"))
ust_sinir = int(input("Üst sınırı giriniz:"))
sayi = random.randint (alt_sinir, ust_sinir) #verdiğiniz alt ve üst sınır arasında random sayı üretecek.

oyun_devam_ediyor_mu = True
while oyun_devam_ediyor_mu:

    tahmin= input("Tahmninin nedir?") #kullanıcıdan sayı istiyoruz.

    if tahmin.isdigit(): #girilen input sayılardan mı harflerden mi oluşuyor?
        tahmin = int(tahmin)
        
        if tahmin == sayi:
         print("Tebrikler, sayıyı bildin!")
         oyun_devam_ediyor_mu = False
        elif tahmin < sayi:
         print("Girdiğin sayı tuttuğum sayıdan küçük") 
        else:
         print("Girdiğin sayı tuttuğum sayıdan büyük")
    else:
      if tahmin == "pes" :
        print("Pes ettin! Tutuğum sayı:",sayi)
        oyun_devam_ediyor_mu = False
      else:
        print("Hatalı giriş yaptınız!")
          
#Furkan Aksoy sayı tahmin etme oyunu videosundan yararlanılmıştır.