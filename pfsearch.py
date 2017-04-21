import os
class Help():
    """Bu yardım sınıfı PFSEARCH sınıfına yardım etmesi için yazıldı ve
     amacı girilen uzantılardaki tüm dosları ve klasörleri bulmaktır"""
    def __init__(self,driv):
        self.isdir=[]# bu bulunan klasör leri geçeci depoluyor
        self.isfile=[]
        self.driv=driv
    def Folder(self):# girilen uzantının altındaki klasör lerin bbulur vemliste olarak verir
        try:
            for sea in os.listdir(self.driv):
                full_ex=os.path.join(self.driv,sea)
                if "windows" in full_ex.lower(): # burda amaç pc deki windows klasöründe arama yapmamasını sağlamak
                    pass
                else:
                    if os.path.isdir(full_ex) and full_ex not in self.isdir:
                        self.isdir.append(full_ex) # ve girilen driv deki sürücülerinde ki klasörleri kaydediyoruz
        except PermissionError:
            pass
        return self.isdir
    def File(self): # girilen uzantının altındaki dosya ları bulup liste olarak verir
        try:
            for sea in os.listdir(self.driv):
                full_ex=os.path.join(self.driv,sea)
                if "windows" in full_ex.lower(): # burda amaç pc deki windows klasöründe arama yapmamasını sağlamak
                    pass
                else:
                    if os.path.isfile(full_ex) and full_ex not in self.isfile:
                        self.isfile.append(full_ex) # ve girilen driv deki sürücülerinde ki klasörleri kaydediyoruz
        except PermissionError:
            pass
        return self.isfile
class PFSEARCH():
    def __init__(self,word):
        self.word=word # her fonksiyon için geçerli olan aranan kelimeyi alıyoruz
        self.drivers=[] # ve pc de kullanılan sürücü yollarını buluyoruz
        extensions="dabqwrtyuıopğüişlkjfszxvnmöçc/"
        for ex in extensions:
            try:
                os.listdir(str(ex)+":")
                self.drivers.append(str(ex)+":"+os.sep)
            except:
                pass
        ########### pc deki tüm klasörleri bulan fonksiyon ####################################
        self.isdir=[] # bu pc de ki tüm klasör lerin listesidir
        self.show=[] # bu ise sadece girilen
        for driving in self.drivers: # burda sınıf çağırıldıgında bulunan sürücüleri alıyoruz
            for i in Help(driving).Folder(): # ve her bulunan sürücüdeki klasörleri yardım sayesinde buraya alıyoruz
                self.isdir.append(i) # bulunan tüm klasör leri alıyorum
        for isd in self.isdir:# daha sonra sürekli genişleyecek olan isdir listesindeki klasörleri tekrar yardıma yollayıp pc deki
            for fo in Help(isd).Folder(): # tüm klasörleri buluyoruz:
                if fo not in self.isdir:
                    self.isdir.append(fo) # bulunan her klasörü genişlemesi için isdire ekliyoruz
        ###########################################################################
    def File(self): # aranan kelime ile işlesen dosya isimlerini bulur liste olarak verir
        show=[]
        for isd in self.isdir :
            for fo in Help().File(driv=isd):
                if self.word.lower() in os.path.split(fo)[1].lower():
                    show.append(fo)
        return show
    def Folder(self): # aranan kelime mile eşleşen dosyaları bulur ve liste olarak verir
        show=[]
        for isd in self.isdir:
            if self.word.lower() in os.path.split(isd)[1].lower():
                show.append(isd)
        return show
