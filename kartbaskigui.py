from tkinter import *
from tkinter import ttk
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from tkinter import filedialog
import threading

def outputfoldercommand():
    global outputfolder
    outputfolder = filedialog.askdirectory()
    
img1 = "./data/itp.jpg"
img2 = "./data/2.sinif.jpg"
img3 = "./data/3.sinif.jpg"
img4 = "./data/4.sinif.jpg"
img5 = "./data/5.sinif.jpg"
img6 = "./data/6.sinif.jpg"
img7 = "./data/7.sinif.jpg"
img8 = "./data/8.sinif.jpg"
img9 = "./data/9.sinif.jpg"
img10 = "./data/hazsinif.jpg"
img11 = "./data/10.sinif.jpg"
img12 = "./data/11.sinif.jpg"
img13 = "./data/12.sinif.jpg"
siniflar = ["2. SINIF","3. SINIF","4. SINIF","5. SINIF","6. SINIF","7. SINIF","8. SINIF","HAZIRLIK SINIFI","9. SINIF","10. SINIF","11. SINIF","12. SINIF"]
donemler = ["2021 - 2022","2022 - 2023","2023 - 2024","2024 - 2025","2025 - 2026","2026 - 2027",]
okullar = ["BİLFEN KOLEJİ","BAHÇEŞEHİR KOLEJİ","TED KOLEJİ","İSTEK KOLEJİ","FMV IŞIK KOLEJİ","MAYA KOLEJİ","ENKA KOLEJİ","TAN KOLEJİ"]

def calistir():
    
    sinif = e1a.get()
    okul = e2a.get()
    baslangic = int(e3a.get())-1
    bitis = int(e4a.get())
    donem = e5a.get()
    fileName = outputfolder+"/"+str(sinif)+"_"+str(okul)+"_"+str(int(baslangic)+1)+"-"+str(bitis)+"_Satış Kartı.pdf"
    pdf = canvas.Canvas(fileName,pagesize=(420.6385, 595))
    
    while baslangic<bitis:
        baslangic+=1
        pdfmetrics.registerFont(TTFont('abcb', './data/calibrib.ttf'))
        pdfmetrics.registerFont(TTFont('abc', './data/calibri.ttf'))
        if var1.get() == 1:
            pdf.drawImage(img1, 0,0, width=420.6385,height=595,mask=None)
        ustbilgi = str(sinif)+" / "+str(okul)+" TOEFL SINAV GİRİŞ KARTI"
        pdf.setFont('abc', 14)
        pdf.drawString(40,512, "No: "+str(baslangic))
        pdf.drawString(40,208, "No: "+str(baslangic))
        if len(str(ustbilgi))<=50:
            pdf.setFont('abcb', 11)
            pdf.drawString(163,525, ustbilgi)
            pdf.drawString(163,225, ustbilgi)
        else:
            pdf.setFont('abcb', 9.5)
            pdf.drawString(163,525, ustbilgi)
            pdf.drawString(163,225, ustbilgi)
        pdf.setFont('abc', 9)
        pdf.drawString(165,132, "Bu kart sadece öğrencinin "+donem+" eğitim döneminde")
        pdf.drawString(165,122, "okulunda düzenlenecek olan TOEFL kurumsal testleri için")
        pdf.drawString(165,112, "kullanılabilir.")
        if sinif =="2. SINIF":
            pdf.drawImage(img2, 315,552, width=90,height=35,mask=None)
            pdf.drawImage(img2, 315,249, width=90,height=35,mask=None)
        if sinif =="3. SINIF":
            pdf.drawImage(img3, 315,552, width=90,height=35,mask=None)
            pdf.drawImage(img3, 315,249, width=90,height=35,mask=None)
        if sinif =="4. SINIF":
            pdf.drawImage(img4, 315,552, width=90,height=35,mask=None)
            pdf.drawImage(img4, 315,249, width=90,height=35,mask=None)
        if sinif =="5. SINIF":
            pdf.drawImage(img5, 315,552, width=90,height=35,mask=None)
            pdf.drawImage(img5, 315,249, width=90,height=35,mask=None)
        if sinif =="6. SINIF":
            pdf.drawImage(img6, 315,552, width=90,height=35,mask=None)
            pdf.drawImage(img6, 315,249, width=90,height=35,mask=None)
        if sinif =="7. SINIF":
            pdf.drawImage(img7, 315,552, width=90,height=35,mask=None)
            pdf.drawImage(img7, 315,249, width=90,height=35,mask=None)
        if sinif =="8. SINIF":
            pdf.drawImage(img8, 315,552, width=90,height=35,mask=None)
            pdf.drawImage(img8, 315,249, width=90,height=35,mask=None)
        if sinif =="9. SINIF":
            pdf.drawImage(img9, 315,552, width=90,height=35,mask=None)
            pdf.drawImage(img9, 315,249, width=90,height=35,mask=None)
        if sinif =="HAZIRLIK SINIFI" or sinif == "HAZIRLIK" or sinif == "HAZ. SINIFI":
            pdf.drawImage(img10, 315,552, width=90,height=35,mask=None)
            pdf.drawImage(img10, 315,249, width=90,height=35,mask=None)
        if sinif =="10. SINIF":
            pdf.drawImage(img11, 315,552, width=90,height=35,mask=None)
            pdf.drawImage(img11, 315,249, width=90,height=35,mask=None)
        if sinif =="11. SINIF":
            pdf.drawImage(img12, 315,552, width=90,height=35,mask=None)
            pdf.drawImage(img12, 315,249, width=90,height=35,mask=None)
        if sinif =="12. SINIF":
            pdf.drawImage(img13, 315,552, width=90,height=35,mask=None)
            pdf.drawImage(img13, 315,249, width=90,height=35,mask=None)
        
        pdf.showPage()
    pdf.save()

def calistirbutton():
    tr1 = threading.Thread(target=calistir)
    tr1.start()
    
root = Tk()
root.title('Kart Baskısı')

panel1 = Frame(root, bd=1, relief="raised", bg="#545454")
panel1.pack(fill=BOTH,expand=1)
label1 = Label(panel1, text="Sınıf:",bg="#545454",fg="#ffffff",font=("Calibri", 10)).grid(row=0,column=0,padx=10,pady=5, sticky=W)
e1a= StringVar()
e1a.set("2. SINIF")
e1a= ttk.Combobox(panel1, width=17, value=siniflar)
e1a.current(0)
e1a.grid(row=0,column=1,padx=10,pady=5)
label2 = Label(panel1, text="Okul:",bg="#545454",fg="#ffffff",font=("Calibri", 10)).grid(row=1,column=0,padx=10,pady=5, sticky=W)
e2a= StringVar()
e2a.set("BİLFEN KOLEJİ")
e2a= ttk.Combobox(panel1, width=17, value=okullar)
e2a.current(0)
e2a.grid(row=1,column=1,padx=10,pady=5)
label3 = Label(panel1, text="Başlangıç:",bg="#545454",fg="#ffffff",font=("Calibri", 10)).grid(row=2,column=0,padx=10,pady=5, sticky=W)
e3a= StringVar()
e3b = Entry(panel1, width=20, textvariable=e3a).grid(row=2,column=1)
label4 = Label(panel1, text="Bitiş:",bg="#545454",fg="#ffffff",font=("Calibri", 10)).grid(row=3,column=0,padx=10,pady=5, sticky=W)
e4a= StringVar()
e4b = Entry(panel1, width=20, textvariable=e4a).grid(row=3,column=1)
label5 = Label(panel1, text="Dönem:",bg="#545454",fg="#ffffff",font=("Calibri", 10)).grid(row=4,column=0,padx=10,pady=5, sticky=W)
e5a= StringVar()
e5a.set("2021 - 2022")
e5a= ttk.Combobox(panel1, width=17, value=donemler)
e5a.current(0)
e5a.grid(row=4,column=1,padx=10,pady=5)
var1 = IntVar()
c1 = Checkbutton(panel1, text='ITP Arkaplan Deneme',bg="#545454",fg="#ffffff",font=("Calibri", 10), activebackground='#545454',selectcolor="#545454",activeforeground='black',variable=var1, onvalue=1, offvalue=0).grid(row=5,column=0,padx=10,pady=5, sticky=W)
button3 = Button(panel1,width=20,text='Çıktı Klasörü',bg="#545454",fg="#ffffff", command=outputfoldercommand).grid(row=5,column=1,padx=10,pady=5)
button4 = Button(panel1,width=20,text='Çalıştır',bg="#545454",fg="#ffffff", command=calistirbutton).grid(row=6,column=0,padx=10,pady=10)
button5 = Button(panel1,width=20,text='Kapat',bg="#545454",fg="#ffffff", command=root.destroy).grid(row=6,column=1,padx=10,pady=10)




style = ttk.Style()
style.theme_create('Cloud', parent="classic", settings={
    ".": {
        "configure": {
            "background": '#545454', # All colors except for active tab-button
        }
    },
    "TNotebook": {
        "configure": {
            "background":"#545454", # color behind the notebook
            "tabmargins": [3, 3, 0, 0], # [left margin, upper margin, right margin, margin beetwen tab and frames]
        }
    },
    "TNotebook.Tab": {
        "configure": {
            "background": '#797979', # Color of non selected tab-button
            "padding": [10, 4], # [space beetwen text and horizontal tab-button border, space between text and vertical tab_button border]
        },
        "map": {
            "background": [("selected", '#545454')], # Color of active tab
            "expand": [("selected", [1, 1, 1, 0])], # [expanse of text]
            "foreground": [("selected", "#ffffff"),("!disabled", "#000000")] 
        }
    }
})
style.theme_use('Cloud')


root.config(background="#545454")
root.mainloop()
