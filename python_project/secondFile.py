import tkinter as tk
import uskudar
import kadikoy
import umraniye
import kecioren
import cankaya
import mamak
import bornova
import cesme
import buca

def fiyati_hesapla():
    il_text = infoIl.get()
    ilce_text = infoIlce.get()
    oda_text = infoOda.get()
    alan_text = infoAlan.get()

    try:
        if (ilce_text == ""):
            info_label.config(text="İlçe Seçiniz", foreground="red")
            info_label.place(x=360, y=160)

        elif (il_text == "İstanbul" and ilce_text == "Üsküdar" and alan_text == "50-100" and oda_text == "2+1"):
            ortalama = uskudar.birinci_durum()

        elif (il_text == "İstanbul" and ilce_text == "Üsküdar" and alan_text == "100-150" and oda_text == "2+1"):
            ortalama = uskudar.ikinci_durum()

        elif (il_text == "İstanbul" and ilce_text == "Üsküdar" and alan_text == "150-200" and oda_text == "2+1"):
            ortalama = uskudar.ucuncu_durum()

        elif (il_text == "İstanbul" and ilce_text == "Üsküdar" and alan_text == "50-100" and oda_text == "3+1"):
            ortalama = uskudar.dorduncu_durum()

        elif (il_text == "İstanbul" and ilce_text == "Üsküdar" and alan_text == "100-150" and oda_text == "3+1"):
            ortalama = uskudar.besinci_durum()

        elif (il_text == "İstanbul" and ilce_text == "Üsküdar" and alan_text == "150-200" and oda_text == "3+1"):
            ortalama = uskudar.altinci_durum()

        elif (il_text == "İstanbul" and ilce_text == "Kadıköy" and alan_text == "50-100" and oda_text == "2+1"):
            ortalama = kadikoy.birinci_durum()
        elif (il_text == "İstanbul" and ilce_text == "Kadıköy" and alan_text == "100-150" and oda_text == "2+1"):
            ortalama = kadikoy.ikinci_durum()

        elif (il_text == "İstanbul" and ilce_text == "Kadıköy" and alan_text == "150-200" and oda_text == "2+1"):
            ortalama = kadikoy.ucuncu_durum()

        elif (il_text == "İstanbul" and ilce_text == "Kadıköy" and alan_text == "50-100" and oda_text == "3+1"):
            ortalama = kadikoy.dorduncu_durum()

        elif (il_text == "İstanbul" and ilce_text == "Kadıköy" and alan_text == "100-150" and oda_text == "3+1"):
            ortalama = kadikoy.besinci_durum()

        elif (il_text == "İstanbul" and ilce_text == "Kadıköy" and alan_text == "150-200" and oda_text == "3+1"):
            ortalama = kadikoy.altinci_durum()

        elif (il_text == "İstanbul" and ilce_text == "Ümraniye" and alan_text == "50-100" and oda_text == "2+1"):
            ortalama = umraniye.birinci_durum()

        elif (il_text == "İstanbul" and ilce_text == "Ümraniye" and alan_text == "100-150" and oda_text == "2+1"):
            ortalama = umraniye.ikinci_durum()

        elif (il_text == "İstanbul" and ilce_text == "Ümraniye" and alan_text == "150-200" and oda_text == "2+1"):
            ortalama = umraniye.ucuncu_durum()

        elif (il_text == "İstanbul" and ilce_text == "Ümraniye" and alan_text == "50-100" and oda_text == "3+1"):
            ortalama = umraniye.dorduncu_durum()

        elif (il_text == "İstanbul" and ilce_text == "Ümraniye" and alan_text == "100-150" and oda_text == "3+1"):
            ortalama = umraniye.besinci_durum()

        elif (il_text == "İstanbul" and ilce_text == "Ümraniye" and alan_text == "150-200" and oda_text == "3+1"):
            ortalama = umraniye.altinci_durum()

        elif (il_text == "Ankara" and ilce_text == "Keçiören" and alan_text == "50-100" and oda_text == "2+1"):
            ortalama = kecioren.birinci_durum()

        elif (il_text == "Ankara" and ilce_text == "Keçiören" and alan_text == "100-150" and oda_text == "2+1"):
            ortalama = kecioren.ikinci_durum()

        elif (il_text == "Ankara" and ilce_text == "Keçiören" and alan_text == "150-200" and oda_text == "2+1"):
            ortalama = kecioren.ucuncu_durum()

        elif (il_text == "Ankara" and ilce_text == "Keçiören" and alan_text == "50-100" and oda_text == "3+1"):
            ortalama = kecioren.dorduncu_durum()

        elif (il_text == "Ankara" and ilce_text == "Keçiören" and alan_text == "100-150" and oda_text == "3+1"):
            ortalama = kecioren.besinci_durum()

        elif (il_text == "Ankara" and ilce_text == "Keçiören" and alan_text == "150-200" and oda_text == "3+1"):
            ortalama = kecioren.altinci_durum()

        elif (il_text == "Ankara" and ilce_text == "Çankaya" and alan_text == "50-100" and oda_text == "2+1"):
            ortalama = cankaya.birinci_durum()

        elif (il_text == "Ankara" and ilce_text == "Çankaya" and alan_text == "100-150" and oda_text == "2+1"):
            ortalama = cankaya.ikinci_durum()

        elif (il_text == "Ankara" and ilce_text == "Çankaya" and alan_text == "150-200" and oda_text == "2+1"):
            ortalama = cankaya.ucuncu_durum()

        elif (il_text == "Ankara" and ilce_text == "Çankaya" and alan_text == "50-100" and oda_text == "3+1"):
            ortalama = cankaya.dorduncu_durum()

        elif (il_text == "Ankara" and ilce_text == "Çankaya" and alan_text == "100-150" and oda_text == "3+1"):
            ortalama = cankaya.besinci_durum()

        elif (il_text == "Ankara" and ilce_text == "Çankaya" and alan_text == "150-200" and oda_text == "3+1"):
            ortalama = cankaya.altinci_durum()

        elif (il_text == "Ankara" and ilce_text == "Mamak" and alan_text == "50-100" and oda_text == "2+1"):
            ortalama = mamak.birinci_durum()

        elif (il_text == "Ankara" and ilce_text == "Mamak" and alan_text == "100-150" and oda_text == "2+1"):
            ortalama = mamak.ikinci_durum()

        elif (il_text == "Ankara" and ilce_text == "Mamak" and alan_text == "150-200" and oda_text == "2+1"):
            ortalama = mamak.ucuncu_durum()

        elif (il_text == "Ankara" and ilce_text == "Mamak" and alan_text == "50-100" and oda_text == "3+1"):
            ortalama = mamak.dorduncu_durum()

        elif (il_text == "Ankara" and ilce_text == "Mamak" and alan_text == "100-150" and oda_text == "3+1"):
            ortalama = mamak.besinci_durum()

        elif (il_text == "Ankara" and ilce_text == "Mamak" and alan_text == "150-200" and oda_text == "3+1"):
            ortalama = mamak.altinci_durum()

        elif (il_text == "İzmir" and ilce_text == "Bornova" and alan_text == "50-100" and oda_text == "2+1"):
            ortalama = bornova.birinci_durum()

        elif (il_text == "İzmir" and ilce_text == "Bornova" and alan_text == "100-150" and oda_text == "2+1"):
            ortalama = bornova.ikinci_durum()

        elif (il_text == "İzmir" and ilce_text == "Bornova" and alan_text == "150-200" and oda_text == "2+1"):
            ortalama = bornova.ucuncu_durum()

        elif (il_text == "İzmir" and ilce_text == "Bornova" and alan_text == "50-100" and oda_text == "3+1"):
            ortalama = bornova.dorduncu_durum()

        elif (il_text == "İzmir" and ilce_text == "Bornova" and alan_text == "100-150" and oda_text == "3+1"):
            ortalama = bornova.besinci_durum()

        elif (il_text == "İzmir" and ilce_text == "Bornova" and alan_text == "150-200" and oda_text == "3+1"):
            ortalama = bornova.altinci_durum()

        elif (il_text == "İzmir" and ilce_text == "Çeşme" and alan_text == "50-100" and oda_text == "2+1"):
            ortalama = cesme.birinci_durum()

        elif (il_text == "İzmir" and ilce_text == "Çeşme" and alan_text == "100-150" and oda_text == "2+1"):
            ortalama = cesme.ikinci_durum()

        elif (il_text == "İzmir" and ilce_text == "Çeşme" and alan_text == "150-200" and oda_text == "2+1"):
            ortalama = cesme.ucuncu_durum()

        elif (il_text == "İzmir" and ilce_text == "Çeşme" and alan_text == "50-100" and oda_text == "3+1"):
            ortalama = cesme.dorduncu_durum()

        elif (il_text == "İzmir" and ilce_text == "Çeşme" and alan_text == "100-150" and oda_text == "3+1"):
            ortalama = cesme.besinci_durum()

        elif (il_text == "İzmir" and ilce_text == "Çeşme" and alan_text == "150-200" and oda_text == "3+1"):
            ortalama = cesme.altinci_durum()

        elif (il_text == "İzmir" and ilce_text == "Buca" and alan_text == "50-100" and oda_text == "2+1"):
            ortalama = buca.birinci_durum()

        elif (il_text == "İzmir" and ilce_text == "Buca" and alan_text == "100-150" and oda_text == "2+1"):
            ortalama = buca.ikinci_durum()

        elif (il_text == "İzmir" and ilce_text == "Buca" and alan_text == "150-200" and oda_text == "2+1"):
            ortalama = buca.ucuncu_durum()

        elif (il_text == "İzmir" and ilce_text == "Buca" and alan_text == "50-100" and oda_text == "3+1"):
            ortalama = buca.dorduncu_durum()

        elif (il_text == "İzmir" and ilce_text == "Buca" and alan_text == "100-150" and oda_text == "3+1"):
            ortalama = buca.besinci_durum()

        elif (il_text == "İzmir" and ilce_text == "Buca" and alan_text == "150-200" and oda_text == "3+1"):
            ortalama = buca.altinci_durum()

        fiyat_label = tk.Label(root,text=str(ortalama) +" ₺",font=('Times',20,'bold')).place(x=620,y=250)

    except:
        pass

def ilce_goster():
    il = infoIl.get()
    info_label.destroy()

    if(il=="İstanbul"):
        ilce_spinbox = tk.Spinbox(root, width=15, values=("Kadıköy","Üsküdar","Ümraniye"), textvariable=infoIlce, font=10).place(x=320, y=130)

    if (il == "Ankara"):
        ilce_spinbox = tk.Spinbox(root, width=15, values=("Keçiören", "Çankaya", "Mamak"),textvariable=infoIlce, font=10).place(x=320, y=130)

    if (il == "İzmir"):
        ilce_spinbox = tk.Spinbox(root, width=15, values=("Bornova", "Çeşme", "Buca"),textvariable=infoIlce, font=10).place(x=320, y=130)

root = tk.Tk()
root.geometry("850x550")
root.title("Konut Fiyatı Hesaplama")

infoIl = tk.StringVar()
infoIlce = tk.StringVar()
infoOda = tk.StringVar()
infoBalkon = tk.StringVar()
infoEsya = tk.StringVar()
infoAlan = tk.StringVar()

il_label = tk.Label(root,text="İl",font=('Times',13,'bold')).place(x=160,y=100)
il_spinbox = tk.Spinbox(root,width=15,values=("İstanbul","Ankara","İzmir"),textvariable=infoIl,font=10).place(x=100,y=130)
ilce_label = tk.Label(root, text="İlçe", font=('Times', 13, 'bold')).place(x=380, y=100)
ilce_spinbox = tk.Spinbox(root, width=15, values=(""),textvariable=infoIlce, font=10).place(x=320, y=130)
ilce_button = tk.Button(root,width=3,text="->",command=ilce_goster).place(x=285,y=127)
oda_label = tk.Label(root, text="Oda sayısı", font=('Times', 13, 'bold')).place(x=130, y=200)
oda_spinbox = tk.Spinbox(root, width=15, values=("2+1","3+1"),textvariable=infoOda, font=10).place(x=100, y=230)
balkon_label = tk.Label(root, text="Balkon", font=('Times', 13, 'bold')).place(x=370, y=200)
balkon_spinbox = tk.Spinbox(root, width=15, values=("Var","Yok"),textvariable=infoBalkon, font=10).place(x=320, y=230)
esya_label = tk.Label(root, text="Eşya", font=('Times', 13, 'bold')).place(x=150, y=300)
esya_spinbox = tk.Spinbox(root, width=15, values=("Eşyalı","Eşyasız"),textvariable=infoEsya, font=10).place(x=100, y=330)
alan_label = tk.Label(root, text="m² (Net)", font=('Times', 13, 'bold')).place(x=360, y=300)
alan_spinbox = tk.Spinbox(root, width=15, values=("50-100","100-150","150-200"),textvariable=infoAlan, font=10).place(x=320, y=330)
fiyat_hesapla = tk.Button(root,width=10,text="HESAPLA",font=('Times', 20, 'bold'),command=fiyati_hesapla).place(x=600,y=130)
info_label = tk.Label(root)
info_label.place(x=360,y=160)
ogrenci_label = tk.Label(root,text="Yasin Rümel 171420007\nKamil Kır 171420011\nBilgisayar Programlama 2 Projesi",font=('Times', 13, 'bold')).place(x=20,y=450)

root.mainloop()