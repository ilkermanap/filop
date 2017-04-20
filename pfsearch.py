import os
class PFSEARCH():
    def __init__(self,word):
        self.word=word # her fonksiyon için geçerli olan aranan kelimeyi alıyoruz
        self.drivers=[] # ve pc de kullanılan sürücü yollarını buluyoruz
        extensions="dabqwrtyuıopğüişlkjfszxvnmöçc/"
        for ex in extensions:
            try:
                os.listdir(str(ex)+":")
                self.drivers.append(str(ex)+":/")
            except:
                pass
    def Helpfolder(self,driv):# klasör lerin bulunmaısında yardımcı olur
        isdir=[] # bu bulunan klasör leri geçeci depoluyor
        try:
            for sea in os.listdir(driv):
                full_ex=os.path.join(driv,sea)
                if "windows" in full_ex.lower(): # burda amaç pc deki windows klasöründe arama yapmamasını sağlamak
                    pass
                else:
                    if os.path.isdir(full_ex) and full_ex not in isdir:
                        isdir.append(full_ex) # ve girilen driv deki sürücülerinde ki klasörleri kaydediyoruz
        except PermissionError:
            pass
        return isdir
    def Helpfile(self,driv): # girilen uzantının altındaki dosya ları bulup liste olarak verir
        isfile=[]
        try:
            for sea in os.listdir(driv):
                full_ex=os.path.join(driv,sea)
                if "windows" in full_ex.lower(): # burda amaç pc deki windows klasöründe arama yapmamasını sağlamak
                    pass
                else:
                    if os.path.isfile(full_ex) and full_ex not in isfile:
                        isfile.append(full_ex) # ve girilen driv deki sürücülerinde ki klasörleri kaydediyoruz
        except PermissionError:
            pass
        return isfile
    def Folder(self):
        isdir=[]
        show=[]
        for driving in self.drivers: # burda sınıf çağırıldıgında bulunan sürücüleri alıyoruz
            for i in PFSEARCH(self.word).Helpfolder(driv=driving): # ve her bulunan sürücüdeki klasörleri yardım sayesinde buraya alıyoruz
                isdir.append(i) # bulunan tüm klasör leri alıyorum
        for isd in isdir:# daha sonra sürekli genişleyecek olan isdir listesindeki klasörleri tekrar yardıma yollayıp pc deki
            for fo in PFSEARCH(self.word).Helpfolder(driv=isd): # tüm klasörleri buluyoruz:
                if fo not in isdir:
                    isdir.append(fo) # bulunan her klasörü genişlemesi için isdire ekliyoruz
                    if self.word.lower() in os.path.split(fo)[1].lower(): # ve eğer aranan kelime bulunan dosya isminde varsa çıkartıyoruz
                        show.append(fo)
        return show
    def File(self):
        show=[]
        isdir=PFSEARCH("").Folder() # tüm klasör leri alıyoruz
        for isd in isdir:
            for fo in PFSEARCH(self.word).Helpfile(driv=isd):
                if self.word.lower() in os.path.split(fo)[1].lower():
                    show.append(fo)
        return show
