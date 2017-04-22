" filop --> file operaions --> dosya işlemleri"
import os


class Help():
    """Bu yardım sınıfı SEARCH sınıfına yardım etmesi için yazıldı ve
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
class PSA():
    " This class is PYTHON SEARCH ALGORİTHMA "
    def __init__(self,word,word_list):
        self.word=word.lower()
        self.result=[]
        self.word_list=[]
        for wor in word_list:
            self.word_list.append(wor.lower())
    def Match(self):
        for word_l in self.word_list: # bu tam eşleşme olanları alıyor önce
            if self.word==os.path.split(word_l)[1] and word_l not in self.result:
                self.result.append(word_l)
        for word_l in self.word_list:
            # bura da tam eşitlik olmasada girilen kelime nın harf sayısından yarısı ile eşlesirse
            number=0
            while True:
                try:
                    if os.path.split(word_l)[1][number]==self.word[number] and word_l not in self.result:
                        number+=1
                    else:
                        if number>int(len(self.word)/2) and word_l not in self.result:
                            self.result.append(word_l)
                        break
                except IndexError:
                    break
        for word_l in self.word_list:
            if self.word in os.path.split(word_l)[1] and word_l not in self.result:
                self.result.append(word_l)
        return self.result
class FILOP():
    """ python dosya işlemleri, ana sınıf bu """
    def __init__(self):
        self.drivers=[] # ve pc de kullanılan sürücü yollarını buluyoruz
        extensions="dabqwrtyuıopğüişlkjfszxvnmöçc/"
        for ex in extensions:
            try:
                os.listdir(str(ex)+":")
                self.drivers.append(str(ex)+":"+os.sep)
            except:
                pass
        ####################### pc deki tüm klasörleri bulan fonksiyon #############
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
    def SearchFile(self,word): # aranan kelime ile işlesen dosya isimlerini bulur liste olarak verir
        show=[]
        for isd in self.isdir :
            for add in PSA(word,Help(driv=isd).File()).Match():
                show.append(add)
        return show
    def SearchFolder(self,word): # aranan kelime mile eşleşen dosyaları bulur ve liste olarak verir
        show=[]
        for isd in self.isdir:
            for add in PSA(word,Help(driv=isd).Folder()).Match():
                    show.append(add)
        return show
    def OpenExtension(self,path): # list or str girilen yoldaki dosya yı açar liste veya str olarak girilebilir
        liste=[]
        if type(liste)==type(path):
            for pat in path:
                os.startfile(pat)
        else:
            os.startfile(path)
