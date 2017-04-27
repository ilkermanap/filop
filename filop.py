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
    def Size(self,totaly=False):# normal çıktı verir liste veya dict değildir
     # totaly false şu demek eğer bir klasörün içindeki dosyaların boyutlarını bayt çinsinden hesaplamış
     # ve bunun kaç mb/gb oldugunu öğrenmek istiyorsan totaly=bulunan bayt miktarı girilmesi gerek yapmalısın
        size_int=os.stat(self.driv).st_size # her dosyanın boyutunu alıyoruz
        size_str=str(size_int) # bir int bir de str kopya cıkartıyoruz
        if totaly!=False:
            size_int=totaly
            size_str=str(size_int)
        try:
            point=size_str[:size_str.index(".")] # burda nokta varmı diye bakıyoruz varsa konumunu aldık
        except:
            point=len(size_str) # yoksa toplam uzunlugunu aldık
        if size_int<1024:
            size=size_str[:point]+"/Bayt"
        elif size_int>1024 and size_int<1048576:
            size=str(size_int/1024)[:point]+"/KB"
        elif size_int>1048576 and size_int<1073741824:
            size=str(size_int/1048576)[:point]+"/MB"
        elif size_int<1073741824 and size_int<1099511627776:
            size=str(size_int/1073741824)[:point]+"/GB"
        elif size_int>1099511627776:
            size=str(size_int/1099511627776)[:point]+"/TB"
        return size,self.driv
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
    def __init__(self,dont_us_search=True):
        # dont_us_search eğer False ise arama fonskiyonlarını kullanamaz ve diğer işlemleri daha hızlı yapar
        self.drivers=[] # ve pc de kullanılan sürücü yollarını buluyoruz
        extensions="dabqwrtyuıopğüişlkjfszxvnmöçc/"
        for ex in extensions:
            try:
                os.listdir(str(ex)+":")
                self.drivers.append(str(ex)+":"+os.sep)
            except:
                pass
        ####################### pc deki tüm klasörleri bulan fonksiyon #############
        if dont_us_search==True:
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
    def Size(self,path):
        if type(list(path))==type(path): # liste olarak girilmiş ise
            show=[]
            for pat in path:
                if os.path.isdir(pat): # klasör ise
                    total_size=0
                    for f in Help(driv=pat).File():
                        total_size+=os.stat(f).st_size
                    for fo in Help(driv=pat).Folder(): # altındaki tüm klasörleri buluyoruz
                        for f in Help(driv=fo).File():
                            total_size+=os.stat(f).st_size
                    show.append(Help(driv=pat).Size(totaly=total_size))
                else: # dosya ise
                    for pat in path:
                        try:
                            show.append(Help(driv=pat).Size())
                        except:
                            pass
            return show
        elif type(str(path))==type(path): # sadece bir tane str olarak girilmiş ise
            if os.path.isfile(path): # dosya ise
                return Help(driv=path).Size()
            else: # klasör ise
                total_size=0
                show=[]
                for f in Help(driv=path).File():
                    total_size+=os.stat(f).st_size
                for fo in Help(driv=pat).Folder(): # altındaki tüm klasörleri buluyoruz
                    for f in Help(driv=fo).File():
                        total_size+=os.stat(f).st_size
                show.append(Help(driv=pat).Size(totaly=total_size))
                return show
        else:
            return "You should only use list or str" # buraya düzgün bir hata olayı yap
x=FILOP()
y=x.SearchFile("resim")
for o in x.Size(y):
    print(o)
