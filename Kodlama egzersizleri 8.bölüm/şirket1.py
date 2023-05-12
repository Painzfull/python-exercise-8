import time 
def şirket_seç():
    print("""
    *** ŞİRKETLER ***

    1)YAŞARSOFTWARE
    2)BORANSOFTWARE

    LÜTFEN AŞAĞIDAKİ KONSOLA ŞİRKETLERDEN BİRİSİNİ KONSOLA GİRİNİZ
    """)
    a = int(input("Lütfen Şirket Seçiniz:"))

    if(a == 1):
        print("1.Şirket Bilgisi Gösteriliyor...")
        time.sleep(0.5)
    elif(a == 2):
        print("2.Şirket Bilgisi Gösteriliyor...")
        time.sleep(0.5)
    else:
        print("Belirtilen Şirket Bilgisi Yanlış.....")

    return a

def sınıfı_getir():
    a = şirket_seç()
    veriler = []
    if(a == 1):
        with open("C:\\Users\\metec\\OneDrive\\Masaüstü\\YasarSoftware.txt",encoding= "utf-8") as f:
            for satır in f:
                sütun1 = satır.strip().split(" ")
                veriler.append((sütun1))
    elif(a == 2):
         with open("C:\\Users\\metec\\OneDrive\\Masaüstü\\BoranSoftware.txt",encoding= "utf-8")as f:
            for satır in f:
                sütun1 = satır.strip().split(" ")
                veriler.append((sütun1))    

    veriler2 = []
    for veri in veriler:
        if all(veri):
            veriler2.append(veri)

    copy_veri = veriler2 
    per = int((len(copy_veri)/5))
    per_class = []
    for i in range(per):
        cal = copy_veri[0:5]
        copy_veri = copy_veri[5:]
        id = int(cal[0][0])
        soyisim = cal[1][-1]
        cal[1].pop(-1)
        isim = " ".join(cal[1])
        telefon ="".join(cal[2])
        maaş =int(cal[3][0])
        diller = cal[4]
        per_class.append(yazılımcı(id,isim,soyisim,telefon,maaş,diller))
    return per_class, per


def uyg():
    while True:
        cs, per = sınıfı_getir()
        print("*** ÇALIŞANLAR ***")
        for j in range(per):
            cs[j].bilgilerigöster()
            print("----------------")
        id = int(input("İstediğiniz Çalışanın ID'sini Seçiniz:"))-1
        if(id+1 > per):
            print("Seçtiğiniz Çalışanın ID'si Bulunamadı....")
            continue
        print("""

        *** İŞLEMLER ***
        
        1)ZAM YAP
        2)DİL EKLE

        LÜTFEN YUKARIDAKİ İŞLEMLERDEN BİRİSİNİ SEÇİNİZ...
        """)
        işlem = int(input("Yapmak İstediğiniz İşlemi Seçiniz:"))
        if(işlem == 1):
            print("Seçilen Çalışanın Maaşına Zam Yapılıyor...")
            time.sleep(0.5)
            zam(cs, id)
            print("Şirket Seçim Kısmına Dönülüyor...")
            time.sleep(0.5)
            continue 
        elif(işlem == 2):
            print("Seçilen Çlışanın Bildiği Dillere Yenisi Ekleniyor...")
            time.sleep(0.5)
            dil_ekle(cs, id)
            print("Şirket Seçim Kısmına Dönülüyor...")
            time.sleep(0.5)
            continue

def zam(x , id):
    zam = int(input("Yapılacak Olan Zammın Tutarını Giriniz:"))
    x[id].zam_yap(zam)
    x[id].güncel_bilgileri_göster()

def dil_ekle(x , id):
    dil = input("Eklenecek Dili Seçiniz:")
    x[id].dil_ekle(dil)
    x[id].güncel_bilgileri_göster()

class yazılımcı():
    def __init__(self,id,isim,soy_isim,numara,maaş,diller):
        self.id = id
        self.isim = isim
        self.soy_isim = soy_isim
        self.numara = numara 
        self.maaş = maaş 
        self.diller = diller
    def bilgilerigöster(self):
        print("Çalışan Bilgileri Gösteriliyor...")
        time.sleep(0.5)
        print("id: {}\nİsim: {}\nSoy İsim: {}\nTelefon Numarası: {}\nMaaş: {}\nBildiği Diller: {}".format(self.id,self.isim,self.soy_isim,self.numara,self.maaş,self.diller))

    def güncel_bilgileri_göster(self):
        print("Çalışanın Güncel Bilgileri Gösteriliyor...")
        time.sleep(0.5)
        print("id: {}\nİsim: {}\nSoy İsim: {}\nTelefon Numarası: {}\nMaaş: {}\nBildiği Diller: {}".format(self.id,self.isim,self.soy_isim,self.numara,self.maaş,self.diller))

    def zam_yap(self,zam_miktarı):
        self.maaş += zam_miktarı
        time.sleep(0.5)
        print("Çalışana Verilen Maaş Miktarı Güncellendi...")
        print("")

    def dil_ekle(self,yeni_dil):
        print("Çalışanın Bildiği Dillere Yenisi Ekleniyor...")
        self.diller.append(yeni_dil)
        time.sleep(0.5)
        print("Çalışanın Bildiği Diller Güncellendi...")
        print("")

s = uyg()



