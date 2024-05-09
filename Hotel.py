#----------------------------------------------------------------------ADATOK--------------------------------------------------------------------------------

# Név:        Tamási Miklós
# Neptkód:    O070E2
# Szak:       Mérnökinfo

#----------------------------------------------------------------------ADATBAZIS_FELEPITESE------------------------------------------------------------------

#         0                 1          2            3           4           5             6           7               8
#   Szálloda_neve   Egyágyas_szoba   1Ára    Kétágyas_szoba   2Ára       Check_in     Check_out   Szobaszáma      Egyágyas?
#     ASD Hotel             10       5000           8         7500      2024.05.04   2024.05.05       5              True

#----------------------------------------------------------------------Konyvtarak----------------------------------------------------------------------------

from abc import ABC, abstractmethod
from tkinter import *
from tkinter import messagebox
from datetime import datetime

#----------------------------------------------------------------------Globalis valtozok---------------------------------------------------------------------

hatter = "#5CFCFF"
gombHatter = "teal"
udv = "Üdvözlünk a Szobafoglaló applikációnkban!"
kiiras ="Itt lehetőség van a szobátfoglalni, törölni, \nvalamint a foglalások átnézésére a különböző hotelek között.\n\n\nKérlék válasz az alábbi lehetőségek közül:"
szovegSzin = "black"
terkoz = 40
ablakMeret = "800x900"
eleres = ""
ADATBAZIS = []

# Teszteléshez:
def Teszt():
    pass

#----------------------------------------------------------------------Osztalyok-----------------------------------------------------------------------------
#----Adatszerkezet

class Szoba(ABC):
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar
    
    @abstractmethod
    def tipus(self):
        pass

    #GETTERS:
    def GetSzobaSzam(self):     return self.szobaszam
    def GetSzobaAr(self):       return self.ar
    #SETTERS:
    def SetSzobaSzam(self, szobaszam):  self.szobaszam = szobaszam
    def SetSzobaAr(self, ar):           self.ar = ar

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam, ar):
        super().__init__(szobaszam, ar)
    
    def tipus(self):
        return "Egyágyas"

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam, ar):
        super().__init__(szobaszam, ar)  
    
    def tipus(self):
        return "Kétágyas"

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
    
    def uj_szoba(self, szoba):
        self.szobak.append(szoba)
    
    def szabad_szobak(self):
        return [szoba for szoba in self.szobak if not szoba.foglalt]

class Foglalas:
    def __init__(self, szoba, checkIn, checkOut):
        self.szoba = szoba
        self.checkIn = checkIn
        self.checkOut = checkOut
        szoba.foglalt = True

#----Különböző műveletek
class Muveletek:
    def Beolvasas():
        pass
        # beolvas = []
        # try:
        #     file = open(eleres + "DATABASE.txt", "r", encoding="utf-8")
            
        #     for sor in file:
        #         beolvas.clear()
        #         beolvas = sor.split(";")
        #         foglal = Foglalas(beolvas[0], beolvas[1], beolvas[2], beolvas[3], beolvas[4], beolvas[5], beolvas[6], beolvas[7], beolvas[8])
        #         ADATBAZIS.append(foglal)

        #     file.close()
        # except :
        #     messagebox.showinfo(title="Adatbázis hiba!", message="Az adatbázis betöltése során hiba lépett fel!\n")

    def Kiiratas():
        messagebox.showinfo("Foglalás sikeres", "A szoba foglalása sikeres volt!")
        

class AblakSzulo(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.geometry(ablakMeret)
        self.config(background=hatter)
        self. transient(master)
        self.grab_set()
        self.resizable(width=False, height=False)

    def destroy(self):
        super().destroy()
        self.master.grab_release()

class GombEvent():
    def Foglalas():
        global fogablak, felhasznaloEntri, szallodamegjelen, agyak, checkIn, checkOut
        fogablak = AblakSzulo()
        
        fogudv = "Szoba foglalás"
        szovegSzin="black"
        cimke = Label(fogablak,
                       text=fogudv, 
                       background=hatter, 
                       font=('Arial', 25, 'bold'), 
                       fg=szovegSzin,
                       pady=10 
                       )
        
        felhasznaloNeve = Label(fogablak,
                       text="Foglaló neve: ", 
                       background=hatter, 
                       font=('Arial', 15, 'bold'), 
                       fg=szovegSzin,
                       pady=10 )
        
        szallodaKivalasztas = Label(fogablak,
                       text="Szálloda kiválasztása: ", 
                       background=hatter, 
                       font=('Arial', 15, 'bold'), 
                       fg=szovegSzin,
                       pady=10 )

        agyKivalasztasa = Label(fogablak,
                       text="Hány ágyas szobát szeretne: ", 
                       background=hatter, 
                       font=('Arial', 15, 'bold'), 
                       fg=szovegSzin,
                       pady=10 )
        
        erkezesiIdo = Label(fogablak,
                       text="Érkezés időpontja(ÉÉÉÉ-HH-NN):", 
                       background=hatter, 
                       font=('Arial', 15, 'bold'), 
                       fg=szovegSzin,
                       pady=10 )

        tavozasiIdo = Label(fogablak,
                       text="Távozás időpontja(ÉÉÉÉ-HH-NN):", 
                       background=hatter, 
                       font=('Arial', 15, 'bold'), 
                       fg=szovegSzin,
                       pady=10
                       )

        felhasznaloEntri = Entry(fogablak, width=30)

        elemek = ["Első", "Második", "Harmadik", "Negyedik"]

        szallodamegjelen = Listbox(fogablak, selectmode=SINGLE)
        for elem in elemek:
             szallodamegjelen.insert(END, elem)
        szallodamegjelen.selection_set(0)

        agyak = StringVar(value="egy")
        egy = Radiobutton(fogablak, text="Egy ágyas szoba", variable=agyak, value="egy", background=hatter)
        ketto = Radiobutton(fogablak, text="Két ágyas szoba", variable=agyak, value="ketto", background=hatter)

        checkIn = Entry(fogablak, width=20)
        checkOut = Entry(fogablak, width=20)

        checkIn.insert(0, "ÉÉÉÉ-HH-NN")
        checkOut.insert(0, "ÉÉÉÉ-HH-NN")

        ujszalloda = Button(fogablak,
                      text="Új szálloda felvétele",
                      command=GombEvent.UjSzalloda,
                      font=("Consolas", 10, "bold"),
                      fg=szovegSzin,
                      bg=gombHatter,
                      activeforeground=szovegSzin,
                      activebackground="blue",
                      justify=CENTER,
                      width=22,
                      bd=5,
                      padx=5
                      )

        cimke.pack()
        felhasznaloNeve.pack()
        felhasznaloEntri.pack()
        szallodaKivalasztas.pack()
        szallodamegjelen.pack()
        ujszalloda.pack()
        agyKivalasztasa.pack()
        egy.pack()
        ketto.pack()
        erkezesiIdo.pack()
        checkIn.pack()
        tavozasiIdo.pack()
        checkOut.pack()

        foglalasMentese = Button(fogablak,
                      text="Foglalás mentése",
                      command=GombEvent.FoglalasAlEsemeny,
                      font=("Consolas", 15, "bold"),
                      fg=szovegSzin,
                      bg=gombHatter,
                      activeforeground=szovegSzin,
                      activebackground="blue",
                      justify=CENTER,
                      width=22,
                      bd=5,
                      padx=5
                      )
        
        torles = Button(fogablak,
                      text="Adatok törlése",
                      command=GombEvent.TorlesAlEsemeny,
                      font=("Consolas", 15, "bold"),
                      fg=szovegSzin,
                      bg=gombHatter,
                      activeforeground=szovegSzin,
                      activebackground="blue",
                      justify=CENTER,
                      width=22,
                      bd=5,
                      padx=5
                      )

        vissza = Button(fogablak ,
                      text="Vissza a főmenübe",
                      command=fogablak.destroy,
                      font=("Consolas", 15, "bold"),
                      fg=szovegSzin,
                      bg=gombHatter,
                      activeforeground=szovegSzin,
                      activebackground="blue",
                      justify=CENTER,
                      width=22,
                      bd=5,
                      padx=5
                      )

        foglalasMentese.pack(side=LEFT)
        torles.pack(side=LEFT)
        vissza.pack(side=LEFT)

        checkIn.bind("<Button-1>", checkIn.delete(0, END))
        checkOut.bind("<Button-1>", checkOut.delete(0, END))

    def Lemondas():
        global lemondablak, foglalasiNevEntri, LemondoLista
        lemondablak = AblakSzulo()
        
        udvozloAblakon = Label(lemondablak, 
                       text="Szoba foglalásának lemondása", 
                       background=hatter, 
                       font=('Arial', 25, 'bold'),
                       pady=10
                       )
        nevMegAdasa = Label(lemondablak, 
                      text="Foglalási név:", 
                      background=hatter,
                      font=('Arial', 15), 
                      pady=10
                      )

        foglalasiNevEntri = Entry(lemondablak, width=50)

        foglalasiNevButton = Button(lemondablak,
                      text="Keresés",
                      command="kereso_gomb",
                      font=("Consolas", 10, "bold"),
                      fg=szovegSzin,
                      bg=gombHatter,
                      activeforeground=szovegSzin,
                      activebackground="blue",
                      justify=CENTER,
                      width=22,
                      bd=5,
                      padx=5
                      )
        
        lemondasi = ["Kérlek adja meg a foglalási nevet!", "", ""]
        lemondoLista = Listbox(lemondablak, selectmode=SINGLE, width=120, height=40)
        for lemond in lemondasi:
             lemondoLista.insert(END, lemond)
        
        keresGomb = Button(
                      lemondablak,
                      text="Lemondás",
                      command=GombEvent.LemondasAlEsemeny,
                      font=("Consolas", 15, "bold"),
                      fg=szovegSzin,
                      bg=gombHatter,
                      activeforeground=szovegSzin,
                      activebackground="blue",
                      justify=CENTER,
                      width=22,
                      bd=5,
                      padx=5
                      )

        torles = Button(lemondablak,
                        text="Keresés törlése",
                        command=GombEvent.LemondasTorles,
                        font=("Consolas", 15, "bold"),
                        fg=szovegSzin,
                        bg=gombHatter,
                        activeforeground=szovegSzin,
                        activebackground="blue",
                        justify=CENTER,
                        width=22,
                        bd=5,
                        padx=5
                        )

        visszaGomb = Button(lemondablak,
                      text="Vissza a főmenübe",
                      command=lemondablak.destroy,
                      font=("Consolas", 15, "bold"),
                      fg=szovegSzin,
                      bg=gombHatter,
                      activeforeground=szovegSzin,
                      activebackground="blue",
                      justify=CENTER,
                      width=22,
                      bd=5,
                      padx=5
                      )

        udvozloAblakon.pack()
        nevMegAdasa.pack()
        foglalasiNevEntri.pack()
        foglalasiNevButton.pack()
        lemondoLista.pack()

        keresGomb.pack(side=LEFT)
        torles.pack(side=LEFT)
        visszaGomb.pack(side=LEFT)

    def LemondasAlEsemeny():
        pass

    def Listazas():
        global listazasablak
        listazasablak = AblakSzulo()

        udvozloAblakon = Label(listazasablak, 
                       text="Szállodák és foglalások listája:", 
                       background=hatter, 
                       font=('Arial', 25, 'bold'),
                       pady=10
                       )
        
        visszaGomb = Button(listazasablak,
                      text="Vissza a főmenübe",
                      command=listazasablak.destroy,
                      font=("Consolas", 15, "bold"),
                      fg=szovegSzin,
                      bg=gombHatter,
                      activeforeground=szovegSzin,
                      activebackground="blue",
                      justify=CENTER,
                      width=22,
                      bd=5,
                      padx=5
                      )

        lista = ["Szállodás és a foglalások láthatók!", "", ""]
        foglalasiLista = Listbox(listazasablak, selectmode=SINGLE, width=120, height=45)
        for l in lista:
             foglalasiLista.insert(END, l)

        udvozloAblakon.pack()
        foglalasiLista.pack(pady=10)
        visszaGomb.pack()

    def UjSzalloda():
        fogablak.destroy()

        global ujszallodaablak, szallodaNeveEntri, szallodaEgyArEntri, szallodaKetArLabel
        ujszallodaablak = AblakSzulo()

        udvozloAblakon = Label(ujszallodaablak, 
                       text="Új szálloda hozzáadása", 
                       background=hatter, 
                       font=('Arial', 25, 'bold'),
                       pady=10
                       )
        szallodaNeveLabel = Label(ujszallodaablak, 
                      text="Szálloda neve:", 
                      background=hatter,
                      font=('Arial', 15), 
                      pady=10
                      )
        
        szallodaNeveEntri = Entry(ujszallodaablak, width=30)

        szallodaEgyArLabel = Label(ujszallodaablak, 
                      text="Egy ágyas szoba ára:", 
                      background=hatter,
                      font=('Arial', 15), 
                      pady=10
                      )
        
        szallodaEgyArEntri = Entry(ujszallodaablak, width=30)

        szallodaKetArLabel = Label(ujszallodaablak, 
                      text="Két ágyas szoba ára:", 
                      background=hatter,
                      font=('Arial', 15), 
                      pady=10
                      )
        
        szallodaKetArEntri = Entry(ujszallodaablak, width=30)

        foglalasMentese = Button(ujszallodaablak,
                      text="Foglalás mentése",
                      command=GombEvent.UjSzalloAlEsemeny,
                      font=("Consolas", 15, "bold"),
                      fg=szovegSzin,
                      bg=gombHatter,
                      activeforeground=szovegSzin,
                      activebackground="blue",
                      justify=CENTER,
                      width=22,
                      bd=5,
                      padx=5
                      )
        
        torles = Button(ujszallodaablak,
                      text="Adatok törlése",
                      command=GombEvent.SzallodaTorles,
                      font=("Consolas", 15, "bold"),
                      fg=szovegSzin,
                      bg=gombHatter,
                      activeforeground=szovegSzin,
                      activebackground="blue",
                      justify=CENTER,
                      width=22,
                      bd=5,
                      padx=5
                      )

        vissza = Button(ujszallodaablak,
                      text="Vissza a főmenübe",
                      command=ujszallodaablak.destroy,
                      font=("Consolas", 15, "bold"),
                      fg=szovegSzin,
                      bg=gombHatter,
                      activeforeground=szovegSzin,
                      activebackground="blue",
                      justify=CENTER,
                      width=22,
                      bd=5,
                      padx=5
                      )

        udvozloAblakon.pack()
        szallodaNeveLabel.pack()
        szallodaNeveEntri.pack()
        szallodaEgyArLabel.pack()
        szallodaEgyArEntri.pack()
        szallodaKetArLabel.pack()
        szallodaKetArEntri.pack()

        foglalasMentese.pack(side=LEFT)
        torles.pack(side=LEFT)
        vissza.pack(side=LEFT)

    def UjSzalloAlEsemeny():
        messagebox.showinfo("Új szálloda", "Az új szállodát rögzítettük az adatbázisban!")
        ujszallodaablak.destroy()

    def FoglalasAlEsemeny():
        messagebox.showinfo("Foglalás", "A Foglalást sikeresen rögzítettük!")
        fogablak.destroy()

    def TorlesAlEsemeny():
        checkIn.insert(0, "ÉÉÉÉ-HH-NN")
        checkOut.insert(0, "ÉÉÉÉ-HH-NN")
        szallodamegjelen.selection_set(0)
        felhasznaloEntri.delete(0, END)
        checkIn.bind("<Button-1>", checkIn.delete(0, END))
        checkOut.bind("<Button-1>", checkOut.delete(0, END))

    def SzallodaTorles():
        szallodaNeveEntri.delete(0, END)
        szallodaEgyArEntri.delete(0, END)
        szallodaKetArLabel.delete(0, END)

    def LemondasTorles():
        foglalasiNevEntri.delete(0, END)
        LemondoLista.delete(0, END)
        lemondasi = ["Kérlek adja meg a foglalási nevet!", "", ""]
        lemondoLista = Listbox(lemondablak, selectmode=SINGLE, width=120, height=40)
        for lemond in lemondasi:
             lemondoLista.insert(END, lemond)

#----------------------------------------------------------------------MAIN----------------------------------------------------------------------------------

def Main():
    kezdoAblak = Tk()

    kezdoAblak.geometry(ablakMeret)
    kezdoAblak.title("Hotel Foglalás")
    kezdoAblak.config(background=hatter)
    kezdoAblak.resizable(width=False, height=False)

    #ikon = PhotoImage(file= eleres + "icon.png")
    #kezdoAblak.iconphoto(True, ikon)

    listazasGomb = Button(
        kezdoAblak,
        text="Foglalások litázása",
        command=GombEvent.Listazas,
                      font=("Consolas", 15, "bold"),
                      fg=szovegSzin,
                      bg=gombHatter,
                      activeforeground=szovegSzin,
                      activebackground="blue",
                      justify=CENTER,
                      width=22,
                      bd=5,
                      padx=5
                      )

    lemondasGomb = Button(kezdoAblak,
                      text="Szoba lemondás",
                      command=GombEvent.Lemondas,
                      font=("Consolas", 15, "bold"),
                      fg=szovegSzin,
                      bg=gombHatter,
                      activeforeground=szovegSzin,
                      activebackground="blue",
                      justify=CENTER,
                      width=22,
                      bd=5,
                      padx=5
                      )

    foglalasGomb = Button(kezdoAblak,
                      text="Szoba foglalás",
                      command=GombEvent.Foglalas,
                      font=("Consolas", 15, "bold"),
                      fg=szovegSzin,
                      bg=gombHatter,
                      activeforeground=szovegSzin,
                      activebackground="blue",
                      justify=CENTER,
                      width=22,
                      bd=5,
                      padx=5
                      )

    udvozloAblakon = Label(kezdoAblak, 
                       text=udv, 
                       background=hatter, 
                       font=('Arial', 25, 'bold'), 
                       fg=szovegSzin,
                       pady=10
                       )

    szovegAblakon = Label(kezdoAblak, 
                      text=kiiras, 
                      background=hatter,
                      font=('Arial', 15), 
                      pady=300
                      )

    udvozloAblakon.pack()
    szovegAblakon.pack()

    foglalasGomb.pack(side=LEFT)
    lemondasGomb.pack(side=LEFT)
    listazasGomb.pack(side=LEFT)

    kezdoAblak.mainloop()

#----------------------------------------------------------------------START---------------------------------------------------------------------------------

Main()

