from django.shortcuts import render
from app import models
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from datetime import datetime,date
from django.http import JsonResponse
import json
import random
import itertools

from app.models import Uyeler,Kategori,Grup,Soru,Ayarlar,Iletisim
# Create your views here.

def index(request):
    
    soru=models.Soru.objects.order_by("?").first()
    ayarlar=models.Ayarlar.objects.all().first()
    ayarlar.gunluk_ziyaretci += 1
    ayarlar.toplam_ziyaretci += 1
    ayarlar.save()
    if "log" in request.session.keys():
        if request.session["log"]:
            user=models.Uyeler.objects.filter(nick_name=request.session["kadi"],password=request.session["sifre"])
            return render(request,'index.html',
                context={
                "sorular":soru,
                "sid":soru.id,
                "user":user.first(),
                "ayarlar":models.Ayarlar.objects.all().first(),
                "toplan_kullanici":len(models.Uyeler.objects.all()),
                "title":"Ana Sayfa",
                "k":0,
                "desc":"Merhaba ben kimsenin bilmediği ama varlığını her zaman hissettirdiği yerdeyim. Sadece boş zamanlarımda kendime yeni bilgiler katmak için soruları cevaplıyorum. Her doğru cevapladığım soru için yardıma muhtaç insanlara 10 buğday tanesi göndermiş oluyorum. Seni de ekibe davet ediyorum. Hoşgeldin. 🤗",
                }, # num_visits appended
            )

    return render(request,'index.html',
        context={
        "sorular":soru,
        "sid":soru.id,
        "user":0,
        "ayarlar":models.Ayarlar.objects.all().first(),
        "toplan_kullanici":len(models.Uyeler.objects.all()),
        "title":"Ana Sayfa",
        "k":0,
        "desc":"Merhaba ben kimsenin bilmediği ama varlığını her zaman hissettirdiği yerdeyim. Sadece boş zamanlarımda kendime yeni bilgiler katmak için soruları cevaplıyorum. Her doğru cevapladığım soru için yardıma muhtaç insanlara 10 buğday tanesi göndermiş oluyorum. Seni de ekibe davet ediyorum. Hoşgeldin. 🤗",
        }, # num_visits appended
    )


def kategoriler_id(request,idd):
    return HttpResponseRedirect('/kategoriler/'+convertAscii(models.Kategori.objects.filter(id=int(idd)).first().isim).lower()+"/"+str(idd))

def kategoriler_id_isim(request,kisim,idd):
    k=idd
    if models.Soru.objects.filter(kategori=models.Kategori.objects.filter(id=int(idd)).first()).order_by("?").first():
        soru=models.Soru.objects.filter(kategori=models.Kategori.objects.filter(id=int(idd)).first()).order_by("?").first()
    else:
        soru=models.Soru.objects.order_by("?").first()
    ayarlar=models.Ayarlar.objects.all().first()
    ayarlar.gunluk_ziyaretci += 1
    ayarlar.toplam_ziyaretci += 1
    ayarlar.save()
    if "log" in request.session.keys():
        if request.session["log"]:
            user=models.Uyeler.objects.filter(nick_name=request.session["kadi"],password=request.session["sifre"])
            return render(request,'index.html',
                context={
                "sorular":soru,
                "sid":soru.id,
                "user":user.first(),
                "ayarlar":models.Ayarlar.objects.all().first(),
                "toplan_kullanici":len(models.Uyeler.objects.all()),
                "title":"Ana Sayfa",
                "k":idd,
                "desc":models.Kategori.objects.filter(id=int(k)).first().aciklama,
                }, # num_visits appended
            )

    return render(request,'index.html',
        context={
        "sorular":soru,
        "sid":soru.id,
        "user":0,
        "ayarlar":models.Ayarlar.objects.all().first(),
        "toplan_kullanici":len(models.Uyeler.objects.all()),
        "title":"Ana Sayfa",
        "k":idd,
        "desc":soru.kategori.aciklama,
        }, # num_visits appended
    )


def kontrol(request):

    bt_value=request.GET["bt_value"]
    soruid=request.GET["soruid"]
    kid=request.GET["kid"]
    ayarlar=models.Ayarlar.objects.all().first()

    if kid == "0":
        yeni_soru=models.Soru.objects.order_by("?").first()
    else:
        if models.Soru.objects.filter(kategori=models.Kategori.objects.filter(id=int(kid)).first()):
            yeni_soru=models.Soru.objects.filter(kategori=models.Kategori.objects.filter(id=int(kid)).first()).order_by("?").first()
        else:
            yeni_soru=models.Soru.objects.order_by("?").first()

    soru=models.Soru.objects.filter(id=int(soruid)).first()
    
    listA = [0, 1, 2, 3]
    perm = itertools.permutations(listA) 
    siklar=list(perm)[random.randint(0,23)]
    yeni_soru_cevir=yeni_soru
    cevaplar = [yeni_soru.sik_1,yeni_soru.sik_2,yeni_soru.sik_3,yeni_soru.sik_4]
    yeni_soru_cevir.sik_1=cevaplar[siklar[0]]
    yeni_soru_cevir.sik_2=cevaplar[siklar[1]]
    yeni_soru_cevir.sik_3=cevaplar[siklar[2]]
    yeni_soru_cevir.sik_4=cevaplar[siklar[3]]
    ayarlar.cozulen_soru +=1
    ayarlar.gunluk_cozulen_soru +=1
    ayarlar.save()
    if soru.sik_1 == str(bt_value):
        ayarlar.gunluk += 10
        ayarlar.aylik += 10
        ayarlar.toplam += 10
        ayarlar.gunluk_toplam += 10
        ayarlar.save()
        if "log" in request.session.keys():
            if request.session["log"]:
                user=models.Uyeler.objects.filter(nick_name=request.session["kadi"],password=request.session["sifre"]).first()
                user.bugday += 10
                user.cozulen_soru +=1
                user.save()
                
        return JsonResponse({"sonuc":"1","cevap":soru.sik_1,"gunluk":ayarlar.gunluk,"aylik":ayarlar.aylik,"toplam":ayarlar.toplam,"yeni_soru_id":yeni_soru.id,"yeni_soru":yeni_soru_cevir.soru,"a":yeni_soru_cevir.sik_1,"b":yeni_soru_cevir.sik_2,"c":yeni_soru_cevir.sik_3,"d":yeni_soru_cevir.sik_4})
    else:
        return JsonResponse({"sonuc":"0","cevap":soru.sik_1,"gunluk":ayarlar.gunluk,"aylik":ayarlar.aylik,"toplam":ayarlar.toplam,"yeni_soru_id":yeni_soru.id,"yeni_soru":yeni_soru_cevir.soru,"a":yeni_soru_cevir.sik_1,"b":yeni_soru_cevir.sik_2,"c":yeni_soru_cevir.sik_3,"d":yeni_soru_cevir.sik_4})

#return HttpResponse("deneme deneme deneme")


def giris(request):

    return render(request,'giris.html',
        context={
        "title":"Giris",
        "desc":"Bugdaybagisla.com sitemize üye girişi yaparak ne kadar katkı sağladığınızı görebilirsiniz. Sıralamanızı takip edebilirsiniz.",
        }, # num_visits appended
    )


def giris_form(request):

    ok=0
    user=models.Uyeler.objects.filter(nick_name=request.POST["kadi"],password=request.POST["sifre"])
    if user:
        request.session["log"]=1
        request.session["kadi"]=request.POST["kadi"]
        request.session["sifre"]=request.POST["sifre"]
        return HttpResponseRedirect('/')
    else:
        ok=1
        return render(request,'giris.html',
            context={
            "ok":ok,
            "title":"Giris",
            }, # num_visits appended
        )

    

def uye_ol(request):
    
    return render(request,'uye_ol.html',
        context={
        "title":"Uye Ol",
        "desc":"Bugdaybagisla.com sitemize üye olabileceğiniz sayfamızıdr. Buradan üye olarak tüm ilerlemenizi takip edebilir, ne kadar katkı sağladığınızı görebilirsiniz.",

        }, # num_visits appended
    )

def uye_ol_form(request):
    
    kadi=request.POST["kadi"]
    mail=request.POST["mail"]
    sifre1=request.POST["sifre1"]
    sifre2=request.POST["sifre2"]
    gsm=request.POST["gsm"]
    ok=0;
    hata="";
    if models.Uyeler.objects.filter(nick_name=kadi):
        hata="Bu kullanıcı adı daha önce alınmıştır."
    else:
        if  models.Uyeler.objects.filter(e_mail=mail):
            hata="Bu mail adresi ile daha önce üye olunmuştur."
        else:
            if sifre1 == sifre2:
                ok=1
                new=Uyeler(
                                        nick_name=kadi,
                                        e_mail=mail,
                                        password=sifre1,
                                        gsm=gsm
                                        )
                new.save()
            else:
                hata="Girmiş olduğunuz şifreler birbiri ile uyuşmamaktadır."


    
    return render(request,'uye_ol.html',
        context={
        "hata":hata,
        "ok":ok,
        "title":"Uye Ol",
        }, # num_visits appended
    )

def cikis(request):

    session_del(request)
    return HttpResponseRedirect('/')

def hakkimizda(request):

    return render(request,'hakkimizda.html',
        context={
        "title":"Hakkımızda",
        "desc":"Bu güne kadar sayısız yardım projesine öncülük etmiş Türkiye Cumhuriyeti toprakları dışında bir çok öncü gelen markanın spons...",
        }, # num_visits appended
    )

def hakkimizda_sayfa(request,sayfa):
    baslik=""
    icerik=""
    desc=""
    etiketler=["Buğday Bağışla","yardım", "bilgi", "bilgi yarışması", "yardımlaşma", "ortadoğu", "oyun", "göçmen", "mülteci", "hak", "insan hakları","insan güvenliği", "politika", "kriz", "dünya", "ekip", "yardım", "oyuncu", "buğday", "bağış", "bağışçı","bağış yap", "ekonomi", "su kuyusu", "ilaç yardımı", "eğitim yardımı", "doğu afrika", "fidan bağışı", "umut ol", "insani yardım", "insani destek","genel kultur sorulari", "soru bankası", "tarih soruları", "edebiyat soruları", "sorular", "yarışma", "soru çöz", "yardımlaşmak", "destek ol", "katkıda bulun", "eğitim"]
    if sayfa == "biz-kimiz":
        baslik="Biz Kimiz ?"
        icerik="""Bu güne kadar sayısız yardım projesine öncülük etmiş Türkiye Cumhuriyeti toprakları dışında bir çok öncü gelen markanın sponsorluğuyla Mali, Etiyopya, Kenya, Gana, Nijerya gibi insani yardımın ulaşamadığı ülkelere el uzatmış bir çok su kuyusu, ilaç tedariği, sağlık alanında hizmet etmiş kimsenin bilmediği ama varlığını her zaman hissettirdiği bir sosyal yardımlaşma ekibiyiz. """
        desc="Bu güne kadar sayısız yardım projesine öncülük etmiş Türkiye Cumhuriyeti toprakları dışında bir çok öncü gelen markanın spons..."
    elif sayfa == "ne-yapiyoruz":
        baslik="Ne Yapıyoruz ?"
        icerik="""Dünya’da 700 milyondan fazla insan su ihtiyacını karşılayamıyor, kirli su kullanımı yüzünden tifo,ishal ve kolera gibi hastalıklar günlük 1000 çocuğun ölmesine sebeb oluyor, yıllık 2 milyondan fazla kişi susuzluk, hastalık, kuraklık gibi nedenlerden ötürü hayatını kaybediyor.Sadece ulusal verilere göre Afrika’da 20 milyondan fazla kişi ilaç yardımı için el uzatmanızı bekliyor ve en kötüsüde bizlerin belki umursamadığı hastalıklar yüzünden milyonlarca insan tedavi göremediği için hayatını kaybediyor.Biz sadece sizlerin boş zamanınızı değerlendirmek ve boş zamanınızda aslında insanlık için yapılabilecek en büyük hizmet için aracılık ediyoruz.Zevkle eğlenceğiz zaman geçireceğiniz vaktinizi, yardımlara dönüştürüp sizler için insanlık için katkılarınızı el uzatan kişilere iletiyoruz.Kimsenin bilmediği ama varlığını hissettirdiği bir ekibiz en güzelide kimse sizleri bilmeyip uzattığınız elleri, varlığınızı hissedecek. Sizde ne yapıyorlar demeyip içinizden artık bende bunu yapıyorum diyebileceksiniz."""
        desc="Dünya’da 700 milyondan fazla insan su ihtiyacını karşılayamıyor, kirli su kullanımı yüzünden tifo,ishal ve kolera gibi hastal..."
    elif sayfa == "nemi-yapacagiz":
        baslik="Nemi Yapacağız ?"
        icerik="""Merak etmeyin EKİPTESİNİZ artık. Ekipteki her çalışma arkadaşımız rahatlıkla kullanabilmesi ve ihtiyaç sahiplerine el uzatabilmesi için rahat ve kullanılabilir bir platform oluşturduk.Çünkü her ekip üyemizin boş vakti yardım bekleyen her bireyin en güzel vakti haline geldi.Artık tek yapmamız gereken karşımıza çıkan soruları cevaplamak.Karşımıza her çıkacak soruya doğru cevap verdiğimiz taktirde 10 buğday tanesi bedelinde bir yardım miktarı bizler için ekipteki diğer gönüllüler tarafınca yardım bekleyen insanlara ulaşmaktadır.cŞimdi sırtımızı yaslayıp soruları cevaplayıp hem boş vaktimizi faydalı bilgilerle doldurup hemde el uzatanlara el uzatmak olacaktır. Unutmayın kimse sizleri bilmez ama varlığınız herkes tarafından hissedilir. """
        desc="Merak etmeyin EKİPTESİNİZ artık. Ekipteki her çalışma arkadaşımız rahatlıkla kullanabilmesi ve ihtiyaç sahiplerine el uzatabi..."
    elif sayfa == "bugdaylarin-bedeli-kim-tarafindan-karsilanmaktadir":
        baslik="Buğdayların bedeli kim tarafından karşılanmaktadır ?"
        icerik="""Her çalışma arkadaşımızın merak ettiği ve korktuğu o soru. Merak etmeyin hiç kimseden bir finans talebinde bulunmuyoruz ve birer ekip üyesi olarak adımıza toplanmaya çalışılan yabancı kuruluşların kampanyalarından kesinlikle sorumlu değiliz. Sponsorlarımız ve tüzel finansörlerimiz sayesinde tüm bedellerimiz karşılanmaktadır.Onlarda sizler gibi kimsenin bilmediği ama şuan varlığını hissettiğimiz kişilerdir."""
        desc="Her çalışma arkadaşımızın merak ettiği ve korktuğu o soru. Merak etmeyin hiç kimseden bir finans talebinde bulunmuyoruz ve bi..."
    elif sayfa == "peki-finansorler-ve-tuzel-kisiler-neden-bugday-bedelini-karsiliyor":
        baslik="Peki Finansörler ve Tüzel Kişiler Neden Buğday Bedelini Karşılıyor ?"
        icerik="""Finansörler ve tüzel kişilerde aslında bazı gayeler sonucunda bu bedelleri karşılamaktadırlar. Oluşturdukları reklamların görüntülenmesi finansörlerimiz ve tüzel sponsorlarımız tarafıından en önemli noktalardan birisidir.Çünkü markalarını ve ürünlerini tanıtmak için en ideal nokta olmaktadır ekibimiz.Bizlerden yani ekipteki arkadaşlarımızdan tek talep ettikleri soruları cevaplarken karşımıza çıkacak reklamları görüntülemek olacaktır.Hem bilgi haznemizin genişlemesi hemde ihtiyaç sahiplerine uzatılacak bir el için umut ışığı olmuşlardır. Her görüntülediğimiz reklam belki bir kuyu, belki bir ilaç, belki bir tedavi bedeli olabileceğini lütfen unutmayalım.En önemlisi ise kimse bizleri bilmeyecek ama herkes tarafından varlığımız hissedilir olacak."""
        desc="Finansörler ve tüzel kişilerde aslında bazı gayeler sonucunda bu bedelleri karşılamaktadırlar. Oluşturdukları reklamların gör..."
    elif sayfa == "sorulari-yanlis-cevaplarsam":
        baslik="Soruları Yanlış Cevaplarsam ?"
        icerik="""Sakin olabilirsiniz her şey ekip üyelerimizin rahatlığı ve kolaylığı için yapıldı. Sorular karşınıza random olarak çıkmamaktadır.Yapay zeka tekniğiyle başta sizleri sorularla tanıyıp, sorarken öğretip, doğru cevap vermenizi sağlamaktadır.Yanlış cevaplarda dahi biriktirdiğimiz buğday miktarı yerinde kalmaktadır el uzatanlara el uzatabilmemiz için elimizden geleni yapmalıyız ideolojisiyle çıktığımız bu yolda yanlışların doğrularımızı götürmemesi gerektiğine inaniyoruz ve bu şekilde ilerliyoruz."""
        desc="Sakin olabilirsiniz her şey ekip üyelerimizin rahatlığı ve kolaylığı için yapıldı. Sorular karşınıza random olarak çıkmamakta..."
    elif sayfa == "insani-yardimda-ulkemiz":
        baslik="İnsani Yardımda Ülkemiz"
        icerik="""Türk milleti Osmanlıdan günümüze gelen insani yardım faktörünü bırakmaksızın tarihinden kultüründen güçlü bir geleneğe sahip bir toplumdur. Bu nedenlerden dolayı güzel ülkemiz doğal afetler olsun toplumsal çatışmalar olsun bir çok zor durumda kalan ülkeye ellerini uzatarak geleneğini devam ettirmektedir.Her hangi bir suretle din,dil,ırk, cinsiyet gözetmeksizin imkanların elverdiği ölçüde insani yardım için tüm imkanlarını seferber etmektedir.Başta Kızılay olmak üzere birçok sivil toplum örgütümüz insani yardım alanında büyük adımlar atmışlardır.2008 yılında Dünya’nın en büyük donör ülkesi olmayı devem ettirmiştir ülkemiz. Toplamda 8.4 milyar dolar tutarında yardım yaptığı Küresel İnsan Raporuna göre açıklanmıştır.Ayrıca milli gelirinin %0,79 unu insani yardım için ayırarak DÜNYA’NIN EN CÖMERT ÜLKESİ unvanını almıştır.Şili deki depremler, Pakistan daki sel felaketi, bunun gibi bir çok ülkenin yardım operasyonlarında büyük rol almıştır.Bu sebeplerden ötürü Dünya nın en büyük insani yardım zirvesi ülkemizde gerçekleşmiştir.Yaklaşık 180 üyenin hazır bulunduğu zirvede 55 den fazla başkan, 60dan fazla bakan, 40 tan fazla genel sekreter düzeyinde yetkili katılım sağlamıştır.BM lerin gerçekleştirtirdiği bu insani yardım zirvesinde açıklanan rakamlara göre 9 binden fazla katılımcının olduğu rapor edilmiştir.Bu tür büyük zirvelerin ülkemizde yapılması gurur verici olmaktan artık öteye geçmiştir.Osmanlıdan günümüze gelen bu geleneğin onurunu yaşamak her türk bireyi için gurur verici bi hale burunmuş olup gögüs kabartmaktadır. Kendimize borç bildiğimiz bu geleneği devam ettirmek adına ekipçe artık daha güçlü olduğumuzu verilerle görmekteyiz."""
        desc="Türk milleti Osmanlıdan günümüze gelen insani yardım faktörünü bırakmaksızın tarihinden kultüründen güçlü bir geleneğe sahip ..."
    elif sayfa == "dogu-afrika":
        baslik="Doğu Afrika"
        icerik="""Son yıllarda Doğu Afrika’da yaşanan insani kriz çok kötü bir durum haline gelmektedir.Sağlık hizmeti gibi gıda hizmeti gibi bir çok alanda yaşanan zorluklar milyonlarca insanın canını tehdit emekle beraber hayatı yaşanmaz kılmaktadır.Özellikle küçük yaştaki çocukların gıda yetersizliğinden ötürü su kaynaklarının olmamasından dolayı her gün hayata göz yummalarına sebeb olmaktadır.Etiyopya, Kenya, Yemen, Ruanda gibi birçok Doğu Afrika ülkesinde sadece belirttiğimiz yetersizliklerden ötürü mali sıkıntıların olduğu sürekli gün yüzüne gelmektedir.Bu tür mali sıkıntıları aşamayan Doğu Afrika ülkelerine insani yardım kuruluşları ellerini uzatmış bulunmaktadırlar.Milyonlarca insanın hayat mücadelesi verdiği bu tür bölgelerde insani yardım kuruluşları tüm desteklerini sarfetmelerine rağmen yetersiz geldiği için bizlerden destek belirtmektedirler. """
        desc="Son yıllarda Doğu Afrika’da yaşanan insani kriz çok kötü bir durum haline gelmektedir.Sağlık hizmeti gibi gıda hizmeti gibi b..."
    elif sayfa == "guney-asya":
        baslik="Güney Asya"
        icerik="""Bangladeş, Nijerya gibi ülkelere sahip olan güney asyanın muson yağmurlarından meydana gelen selin bir çok insanı zor duruma düşürmesıyle geçtiğimiz günlerde gündeme gelip bir çok enkazzede hayatını kaybetmiştir.Milyonlarca insanın evsiz kaldığı bu üzücü durumda ülkemizden ve ekibimizden o an elverdiği şekilde tüm destekler sunulmuştur. Hala Güney Asya için yardımlar devam etmektedir. Milyonlarca insanı umut ışığı olmak adına düzenlenen kampayalar destek olmak için sadece sitemizde kısa bir vakit ayırmanız yeterli olacaktır."""
        desc="Bangladeş, Nijerya gibi ülkelere sahip olan güney asyanın muson yağmurlarından meydana gelen selin bir çok insanı zor duruma ..."

    return render(request,'alt-sayfa.html',
        context={
        "baslik":baslik,
        "icerik":icerik,
        "etiketler":etiketler,
        "title":baslik,
        "desc":desc,
        }, # num_visits appended
    )

def kategoriler(request):

    kategoriler=models.Kategori.objects.all()
    soru_sayisi=[]
    for i in kategoriler:
        soru_sayisi.append(len(models.Soru.objects.filter(kategori=i)))
    return render(request,'kategoriler.html',
        context={
        "kategoriler":zip(kategoriler,soru_sayisi),
        "title":"Kategoriler",
        "desc":"Hoşgeldiniz buradan istediğiniz kategoriyi seçip sadece o kategoriye ailt soruları çözebilirsiniz. Size minnettarız...",
        }, # num_visits appended
    )


def lider_tablosu(request):

    tablo=models.Uyeler.objects.order_by("-bugday")[:10]
    return render(request,'lider-tablosu.html',
        context={
        "tablo":tablo,
        "title":"Lider Tablosu",
        "desc":"Buğday Bağışla ekibinin en aktif kullanıcıları. Hepiniz hoşgelsiniz. İnsanlara el uzatıp onalrı unutmadığınız için teşekkür ederiz...",
        }, # num_visits appended
    )

def iletisim(request):

    return render(request,'iletisim.html',
        context={
        "ok":0,
        "title":"İletişim",
        "desc":"Bizimle ilgili tüm merak etiiklerinizi buradan bize sorabilirsiniz. Elimizden geldiğince herkese cevap vermeyi borç biliriz.",
        }, # num_visits appended
    )

def iletisim_form(request):

    new=Iletisim(
        kadi=request.POST["kadi"],
        kbasi=request.POST["kbasi"],
        kicerik=request.POST["kicerik"]
        )
    new.save()

    return render(request,'iletisim.html',
        context={
        "ok":1,
        "title":"İletişim",
        "desc":"Bizimle ilgili tüm merak etiiklerinizi buradan bize sorabilirsiniz. Elimizden geldiğince herkese cevap vermeyi borç biliriz.",
        }, # num_visits appended
    )

def gizlilik(request):

    return render(request,'gizlilik.html',
        context={
        "title":"Gizlilik Sözleşmesi",
        "desc":"Üyelerimizin gizliliğini göz önünde bulundurmak her zaman boynumuzun borcudur. Merak etmeyin tüm bilgilerimiz sözleşme ile koruma altındadır.",
        }, # num_visits appended
    )

def uyelik(request):

    return render(request,'uyelik.html',
        context={
        "title":"Üyelik Sözleşmesi",
        "desc":"Üyelerimizin üye olurken hakları çift taraflı olarak bu sözleşmede bulunmaktadır. Hepimiz güvendeyiz ...",
        }, # num_visits appended
    )


def soru_cevap(request,soru):
    soru1=models.Soru.objects.filter(id=soru).first()
    cat=convertAscii(soru1.kategori.isim).lower()
    qu=convertAscii(soru1.soru).lower()
    return HttpResponseRedirect('/soru-cevap/'+cat+"/"+qu+"/"+str(soru1.id))

def soru_cevap_metin(request,kategori,metin,soru):

    soru1=models.Soru.objects.filter(id=soru).first()
    desc=soru1.soru + " Doğru cevap: "+soru1.sik_1+" - Diğer şıklar: " + soru1.sik_2+  " - "+soru1.sik_3+" - "+soru1.sik_4
    return render(request,'soru-cevap.html',
        context={
        "title":soru1.soru,
        "soru":soru1,
        "desc":desc,
        }, # num_visits appended
    )

def sitemap(request):

    return render(request,'sitemap.xml',
        context={
        }, # num_visits appended
    )

def sitemap_sira(request,sira):

    return render(request,'sitemap_'+str(sira)+'.xml',
        context={
        }, # num_visits appended
    )

def robot_txt(request):
    return render(request,'robot.txt',
        context={
        }, # num_visits appended
    )


def random_soru(request):

    soru=models.Soru.objects.order_by("?").first()
    return HttpResponseRedirect('/soru-cevap/'+str(soru.id))







def rastgele():
    listA = [1, 2, 3, 4]
    perm = itertools.permutations(listA)
    for i in list(perm): 
        print(i)

def session_del(request):
    for i in list(request.session.keys()):
        del request.session[i]

def convertAscii(metin):
    liste = {
        "  ":" ",
        "İ":"i",
        "ı": "i",
         "Ç": "c",
         "ç":"c",
         " ": "-",
         "ş": "s",
         "Ş":"s",
         "ğ":"g",
         "Ğ":"g",
         "\'":"",
         "\"":"",
         "ö":"o",
         "Ö":"o",
         ".":"",
         "ü":"u",
         "Ü":"u",
         "?":"",
         "!":"",
         "´":"",
         }

    for karakter in liste:
        metin = metin.replace(karakter, liste[karakter])
    return metin