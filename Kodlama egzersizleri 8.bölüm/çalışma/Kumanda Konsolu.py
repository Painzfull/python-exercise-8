import random
import time

class kumanda():

    def __init__(self,tvdurum = "kapalı",tvses = 0,kanallistesi = ["TRT"],kanal = "TRT"):
        self.tvdurum = tvdurum
        self.tvses = tvses
        self.kanallistesi = kanallistesi
        self.kanal = kanal

    def tvaç(self):

        if(self.tvdurum == "Açık"):
            print("Televizyon zaten açık")
        else:
            print("Televizyon açılıyor...")
            self.tvdurum = "Açık"

    def tvkapat(self):

        if(self.tvdurum == "Kapalı"):
            print("Televizyon zaten kapalı")
        else:
            print("Televizyon kapatılıyor...")
            self.tvdurum = "Kapalı"

    def sesayarları(self):
        while True:
            cevap = input("SESİ AZALT: '<'\nSESİ ARTIR: '>'\nÇIKIŞ : ''çıkış'\n===>>")

            if(cevap == "<"):
                if(self.tvses != 0):
                    self.tvses -= 1

                print("SES:",self.tvses)
            elif(cevap == ">"):
                if(self.tvses != 31):
                    self.tvses += 1
                print("SES:",self.tvses)
            else:
                print("Ses Güncellendi:",self.tvses)
                break
    def kanalekle(self,kanalismi):

        print("Kanal ekleniyor....")
        time.sleep(1)

        self.kanallistesi.append(kanalismi)

        print("Kanal eklendi......")
    def rastgelekanal(self):

        rastgeele = random.randint(0,len(self.kanallistesi)-1)

        self.kanal = self.kanallistesi[rastgeele]

        print("Şu anki kanal:",self.kanal)

    def __len__(self):

        return len(self.kanallistesi)
    def __str__(self):

        return "TV DURUMU: {}\nTV SES: {}\nŞU ANKİ KANAL: {}\n".format(self.tvdurum,self.tvses,self.kanallistesi,self.kanal)

kumanda = kumanda()

print("""

televizyon Uygulaması


1.TV AÇ

2.TV KAPAT

3.SES AYARLARI

4.KANAL EKLE

5.KANAL SAYISI ÖĞRENME

6.RASTGELA KANALA GEÇME

7.TELEVİZYON BİLGİLERİ

ÇIKMAK İÇİN q YA BASIN.

""")



while True:

    işlem = input("İşlem Seçiniz:")

    if(işlem == "q"):
        print("Program Sonlandırılıyor..")
        break
    elif(işlem == "1"):
        kumanda.tvaç()
    elif(işlem == "2"):
        kumanda.tvkapat()
    elif(işlem == "3"):
        kumanda.sesayarları()
    elif(işlem == "4"):
        kanalisimleri = input("kanalk isimlerini ',' ayrırarak girin:")

        kanallistesi = kanalisimleri.split(",")
        for eklenecekler in kanallistesi:
            kumanda.kanalekle(eklenecekler)
    elif(işlem == "5"):
        print("Kanal Sayısı:",len(kumanda))
    elif(işlem == "6"):
        kumanda.rastgelekanal()
    elif(işlem == "7"):
        print(kumanda)
    else:
        print("Geçersiz işlem")









