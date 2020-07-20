import tkinter as tkr
from PIL import Image, ImageTk
import baza
import scrapper
import Scroll
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = tkr.Tk()

dane = scrapper.start()

def znajdz_ulubione():
    ulubione = []
    tab = baza.getulubione()
    for i in dane:
        for j in tab:
            if i[0] == j:
                ulubione.append([i[0],i[1],float(i[2]),i[3],i[4],i[5]])
    return ulubione

ulubione_tab = znajdz_ulubione()

def wyswietl_ulubione(dane):
    list = root.pack_slaves()
    for l in list:
        l.destroy()
    tabele = []

    top = tkr.Canvas(root, width=1200, height=100, bd=5, relief='sunken')
    top.pack()

    wszystkie = tkr.Button(top, text="Wszystkie", width=20, font=30, bd=8, fg="Blue", bg="white", relief="raised",command = lambda : sortuj_wg_nazwy(dane))
    wszystkie.place(relx=0.02, rely=0.1)

    ulubione = tkr.Button(top, text="Ulubione", width=20, font=30, bd=8, fg='Blue', bg="white", relief="raised")
    ulubione.place(relx=0.189, rely=0.1)

    nazwa = tkr.Button(top, text="Nazwa", width=20, font=30, bd=8, bg="white", relief="raised",
                       command=lambda: sortuj_wg_nazwy2(dane))
    nazwa.place(relx=0.02, rely=0.5)

    data = tkr.Button(top, text="Data", width=18, font=30, bd=8, bg="white", relief="raised",
                      command=lambda: sortuj_wg_daty(dane))
    data.place(relx=0.189, rely=0.5)

    kurs = tkr.Button(top, text="Kurs", width=18, font=30, bd=8, bg="white", relief="raised",
                      command=lambda: sortuj_wg_kurs(dane))
    kurs.place(relx=0.344, rely=0.5)

    zmiana = tkr.Button(top, text="Zmiana", width=18, font=30, bd=8, bg="white", relief="raised",
                        command=lambda: sortuj_wg_zmiana(dane))
    zmiana.place(relx=0.5, rely=0.5)

    wolumen = tkr.Button(top, text="Wolumen", width=18, font=30, bd=8, bg="white", relief="raised",
                         command=lambda: sortuj_wg_wolumen(dane))
    wolumen.place(relx=0.656, rely=0.5)

    obrot = tkr.Button(top, text="Obrot", width=18, font=30, bd=8, bg="white", relief="raised",
                       command=lambda: sortuj_wg_obrot(dane))
    obrot.place(relx=0.813, rely=0.5)

    frame = tkr.Canvas(root)
    frame.pack(side='left')
    scrollable_body = Scroll.Scrollable(frame, width=20)

    for i in ulubione_tab:
        tabele.append(Akcja(i[0], i[2], i[1], i[4], i[5],i[3], scrollable_body))
        tabele[-1].ulubione = True
    scrollable_body.update()


def sortuj_wg_nazwy(dane):
    list = root.pack_slaves()
    for l in list:
        l.destroy()
    tabele = []

    top = tkr.Canvas(root,width=1200,height=100,bd = 5,relief = 'sunken')
    top.pack()

    wszystkie = tkr.Button(top, text="Wszystkie", width=20, font=30, bd=8,fg = "Blue", bg="white", relief="raised")
    wszystkie.place(relx=0.02, rely=0.1)

    ulubione = tkr.Button(top, text="Ulubione", width=20, font=30, bd=8,fg='Blue', bg="white", relief="raised",command=lambda : wyswietl_ulubione(dane))
    ulubione.place(relx=0.189, rely=0.1)

    nazwa = tkr.Button(top, text="Nazwa", width=20, font=30, bd=8, bg="white", relief="raised",
                       command=lambda: sortuj_wg_nazwy2(dane))
    nazwa.place(relx=0.02,rely=0.5)

    data = tkr.Button(top, text="Data",width=18, font=30, bd=8, bg="white", relief="raised", command=lambda: sortuj_wg_daty(dane))
    data.place(relx=0.189,rely=0.5)

    kurs = tkr.Button(top, text="Kurs", width=18, font=30, bd=8, bg="white", relief="raised",
                      command=lambda: sortuj_wg_kurs(dane))
    kurs.place(relx=0.344,rely=0.5)

    zmiana = tkr.Button(top, text="Zmiana", width=18, font=30, bd=8, bg="white", relief="raised",
                        command=lambda: sortuj_wg_zmiana(dane))
    zmiana.place(relx=0.5,rely=0.5)

    wolumen = tkr.Button(top, text="Wolumen",width=18, font=30, bd=8, bg="white", relief="raised", command=lambda: sortuj_wg_wolumen(dane))
    wolumen.place(relx=0.656,rely=0.5)

    obrot = tkr.Button(top, text="Obrot",width=18, font=30, bd=8, bg="white", relief="raised", command=lambda: sortuj_wg_obrot(dane))
    obrot.place(relx=0.813,rely=0.5)

    frame = tkr.Canvas(root)
    frame.pack(side='left')
    scrollable_body = Scroll.Scrollable(frame, width=20)

    dane = sorted(dane, key=lambda dane_entry: dane_entry[0])

    for i in dane:
        tabele.append(Akcja(i[0], i[2], i[1], i[4], i[5],i[3],scrollable_body))

    scrollable_body.update()

def sortuj_wg_nazwy2(dane):
    list = root.pack_slaves()
    for l in list:
        l.destroy()
    tabele = []

    top = tkr.Canvas(root, width=1200, height=100, bd=5, relief='sunken')
    top.pack()

    wszystkie = tkr.Button(top, text="Wszystkie", width=20, font=30, bd=8, fg="Blue", bg="white", relief="raised")
    wszystkie.place(relx=0.02, rely=0.05)

    ulubione = tkr.Button(top, text="Ulubione", width=20, font=30, bd=8, fg='Blue', bg="white", relief="raised",
                          command=lambda: wyswietl_ulubione(dane))
    ulubione.place(relx=0.189, rely=0.1)

    nazwa = tkr.Button(top, text="Nazwa", width=20, font=30, bd=8, bg="white", relief="raised",
                       command=lambda: sortuj_wg_nazwy(dane))
    nazwa.place(relx=0.02,rely=0.5)

    data = tkr.Button(top, text="Data",width=18, font=30, bd=8, bg="white", relief="raised", command=lambda: sortuj_wg_daty(dane))
    data.place(relx=0.189,rely=0.5)

    kurs = tkr.Button(top, text="Kurs", width=18, font=30, bd=8, bg="white", relief="raised",
                      command=lambda: sortuj_wg_kurs(dane))
    kurs.place(relx=0.344,rely=0.5)

    zmiana = tkr.Button(top, text="Zmiana", width=18, font=30, bd=8, bg="white", relief="raised",
                        command=lambda: sortuj_wg_zmiana(dane))
    zmiana.place(relx=0.5,rely=0.5)

    wolumen = tkr.Button(top, text="Wolumen",width=18, font=30, bd=8, bg="white", relief="raised", command=lambda: sortuj_wg_wolumen(dane))
    wolumen.place(relx=0.656,rely=0.5)

    obrot = tkr.Button(top, text="Obrot",width=18, font=30, bd=8, bg="white", relief="raised", command=lambda: sortuj_wg_obrot(dane))
    obrot.place(relx=0.813,rely=0.5)

    frame = tkr.Canvas(root)
    frame.pack(side='left')
    scrollable_body = Scroll.Scrollable(frame, width=20)

    dane = sorted(dane, key=lambda dane_entry: dane_entry[0])
    dane.reverse()
    for i in dane:
        tabele.append(Akcja(i[0], i[2], i[1], i[4], i[5],i[3],scrollable_body))

    scrollable_body.update()


def sortuj_wg_daty(dane):
    pass

def sortuj_wg_wolumen2(dane):
    list = root.pack_slaves()
    for l in list:
        l.destroy()
    tabele = []

    top = tkr.Canvas(root, width=1200, height=100, bd=5, relief='sunken')
    top.pack()

    wszystkie = tkr.Button(top, text="Wszystkie", width=20, font=30, bd=8, fg="Blue", bg="white", relief="raised")
    wszystkie.place(relx=0.02, rely=0.05)

    ulubione = tkr.Button(top, text="Ulubione", width=20, font=30, bd=8, fg='Blue', bg="white", relief="raised",
                          command=lambda: wyswietl_ulubione(dane))
    ulubione.place(relx=0.189, rely=0.1)

    nazwa = tkr.Button(top, text="Nazwa", width=20, font=30, bd=8, bg="white", relief="raised",
                       command=lambda: sortuj_wg_nazwy(dane))
    nazwa.place(relx=0.02, rely=0.5)

    data = tkr.Button(top, text="Data", width=18, font=30, bd=8, bg="white", relief="raised",
                      command=lambda: sortuj_wg_daty(dane))
    data.place(relx=0.189, rely=0.5)

    kurs = tkr.Button(top, text="Kurs", width=18, font=30, bd=8, bg="white", relief="raised",
                      command=lambda: sortuj_wg_kurs(dane))
    kurs.place(relx=0.344, rely=0.5)

    zmiana = tkr.Button(top, text="Zmiana", width=18, font=30, bd=8, bg="white", relief="raised",
                        command=lambda: sortuj_wg_zmiana(dane))
    zmiana.place(relx=0.5, rely=0.5)

    wolumen = tkr.Button(top, text="Wolumen", width=18, font=30, bd=8, bg="white", relief="raised",
                         command=lambda: sortuj_wg_wolumen(dane))
    wolumen.place(relx=0.656, rely=0.5)

    obrot = tkr.Button(top, text="Obrot", width=18, font=30, bd=8, bg="white", relief="raised",
                       command=lambda: sortuj_wg_obrot(dane))
    obrot.place(relx=0.813, rely=0.5)

    frame = tkr.Canvas(root)
    frame.pack(side='left')
    scrollable_body = Scroll.Scrollable(frame, width=20)

    dane = sorted(dane, key=lambda dane_entry: dane_entry[4])
    dane.reverse()
    for i in dane:
        tabele.append(Akcja(i[0], i[2], i[1], i[4], i[5], i[3], scrollable_body))

    scrollable_body.update()

def sortuj_wg_wolumen(dane):
    list = root.pack_slaves()
    for l in list:
        l.destroy()
    tabele = []

    top = tkr.Canvas(root, width=1200, height=100, bd=5, relief='sunken')
    top.pack()

    wszystkie = tkr.Button(top, text="Wszystkie", width=20, font=30, bd=8, fg="Blue", bg="white", relief="raised")
    wszystkie.place(relx=0.02, rely=0.05)

    ulubione = tkr.Button(top, text="Ulubione", width=20, font=30, bd=8, fg='Blue', bg="white", relief="raised",
                          command=lambda: wyswietl_ulubione(dane))
    ulubione.place(relx=0.189, rely=0.1)

    nazwa = tkr.Button(top, text="Nazwa", width=20, font=30, bd=8, bg="white", relief="raised",
                       command=lambda: sortuj_wg_nazwy(dane))
    nazwa.place(relx=0.02, rely=0.5)

    data = tkr.Button(top, text="Data", width=18, font=30, bd=8, bg="white", relief="raised",
                      command=lambda: sortuj_wg_daty(dane))
    data.place(relx=0.189, rely=0.5)

    kurs = tkr.Button(top, text="Kurs", width=18, font=30, bd=8, bg="white", relief="raised",
                      command=lambda: sortuj_wg_kurs(dane))
    kurs.place(relx=0.344, rely=0.5)

    zmiana = tkr.Button(top, text="Zmiana", width=18, font=30, bd=8, bg="white", relief="raised",
                        command=lambda: sortuj_wg_zmiana(dane))
    zmiana.place(relx=0.5, rely=0.5)

    wolumen = tkr.Button(top, text="Wolumen", width=18, font=30, bd=8, bg="white", relief="raised",
                         command=lambda: sortuj_wg_wolumen2(dane))
    wolumen.place(relx=0.656, rely=0.5)

    obrot = tkr.Button(top, text="Obrot", width=18, font=30, bd=8, bg="white", relief="raised",
                       command=lambda: sortuj_wg_obrot(dane))
    obrot.place(relx=0.813, rely=0.5)

    frame = tkr.Canvas(root)
    frame.pack(side='left')
    scrollable_body = Scroll.Scrollable(frame, width=20)

    dane = sorted(dane, key=lambda dane_entry: dane_entry[4])

    for i in dane:
        tabele.append(Akcja(i[0], i[2], i[1], i[4], i[5],i[3],scrollable_body))

    scrollable_body.update()

def sortuj_wg_obrot(dane):
    list = root.pack_slaves()
    for l in list:
        l.destroy()
    tabele = []

    top = tkr.Canvas(root, width=1200, height=100, bd=5, relief='sunken')
    top.pack()

    wszystkie = tkr.Button(top, text="Wszystkie", width=20, font=30, bd=8, fg="Blue", bg="white", relief="raised")
    wszystkie.place(relx=0.02, rely=0.05)

    ulubione = tkr.Button(top, text="Ulubione", width=20, font=30, bd=8, fg='Blue', bg="white", relief="raised",
                          command=lambda: wyswietl_ulubione(dane))
    ulubione.place(relx=0.189, rely=0.1)

    nazwa = tkr.Button(top, text="Nazwa", width=20, font=30, bd=8, bg="white", relief="raised",
                       command=lambda: sortuj_wg_nazwy(dane))
    nazwa.place(relx=0.02, rely=0.5)

    data = tkr.Button(top, text="Data", width=18, font=30, bd=8, bg="white", relief="raised",
                      command=lambda: sortuj_wg_daty(dane))
    data.place(relx=0.189, rely=0.5)

    kurs = tkr.Button(top, text="Kurs", width=18, font=30, bd=8, bg="white", relief="raised",
                      command=lambda: sortuj_wg_kurs(dane))
    kurs.place(relx=0.344, rely=0.5)

    zmiana = tkr.Button(top, text="Zmiana", width=18, font=30, bd=8, bg="white", relief="raised",
                        command=lambda: sortuj_wg_zmiana(dane))
    zmiana.place(relx=0.5, rely=0.5)

    wolumen = tkr.Button(top, text="Wolumen", width=18, font=30, bd=8, bg="white", relief="raised",
                         command=lambda: sortuj_wg_wolumen(dane))
    wolumen.place(relx=0.656, rely=0.5)

    obrot = tkr.Button(top, text="Obrot", width=18, font=30, bd=8, bg="white", relief="raised",
                       command=lambda: sortuj_wg_obrot2(dane))
    obrot.place(relx=0.813, rely=0.5)

    frame = tkr.Canvas(root)
    frame.pack(side='left')
    scrollable_body = Scroll.Scrollable(frame, width=20)

    dane = sorted(dane, key=lambda dane_entry: dane_entry[5])

    for i in dane:
        tabele.append(Akcja(i[0], i[2], i[1], i[4], i[5],i[3],scrollable_body))

    scrollable_body.update()

def sortuj_wg_zmiana(dane):
    list = root.pack_slaves()
    for l in list:
        l.destroy()
    tabele = []

    top = tkr.Canvas(root, width=1200, height=100, bd=5, relief='sunken')
    top.pack()

    wszystkie = tkr.Button(top, text="Wszystkie", width=20, font=30, bd=8, fg="Blue", bg="white", relief="raised")
    wszystkie.place(relx=0.02, rely=0.05)

    ulubione = tkr.Button(top, text="Ulubione", width=20, font=30, bd=8, fg='Blue', bg="white", relief="raised",
                          command=lambda: wyswietl_ulubione(dane))
    ulubione.place(relx=0.189, rely=0.1)

    nazwa = tkr.Button(top, text="Nazwa", width=20, font=30, bd=8, bg="white", relief="raised",
                       command=lambda: sortuj_wg_nazwy(dane))
    nazwa.place(relx=0.02, rely=0.5)

    data = tkr.Button(top, text="Data", width=18, font=30, bd=8, bg="white", relief="raised",
                      command=lambda: sortuj_wg_daty(dane))
    data.place(relx=0.189, rely=0.5)

    kurs = tkr.Button(top, text="Kurs", width=18, font=30, bd=8, bg="white", relief="raised",
                      command=lambda: sortuj_wg_kurs(dane))
    kurs.place(relx=0.344, rely=0.5)

    zmiana = tkr.Button(top, text="Zmiana", width=18, font=30, bd=8, bg="white", relief="raised",
                        command=lambda: sortuj_wg_zmiana2(dane))
    zmiana.place(relx=0.5, rely=0.5)

    wolumen = tkr.Button(top, text="Wolumen", width=18, font=30, bd=8, bg="white", relief="raised",
                         command=lambda: sortuj_wg_wolumen(dane))
    wolumen.place(relx=0.656, rely=0.5)

    obrot = tkr.Button(top, text="Obrot", width=18, font=30, bd=8, bg="white", relief="raised",
                       command=lambda: sortuj_wg_obrot(dane))
    obrot.place(relx=0.813, rely=0.5)

    frame = tkr.Canvas(root)
    frame.pack(side='left')
    scrollable_body = Scroll.Scrollable(frame, width=20)

    dane = sorted(dane, key=lambda dane_entry: float(dane_entry[3]))
    dane.reverse()
    for i in dane:
        tabele.append(Akcja(i[0], i[2], i[1], i[4], i[5],i[3],scrollable_body))

    scrollable_body.update()

def sortuj_wg_zmiana2(dane):
    list = root.pack_slaves()
    for l in list:
        l.destroy()
    tabele = []

    top = tkr.Canvas(root, width=1200, height=100, bd=5, relief='sunken')
    top.pack()

    wszystkie = tkr.Button(top, text="Wszystkie", width=20, font=30, bd=8, fg="Blue", bg="white", relief="raised")
    wszystkie.place(relx=0.02, rely=0.05)

    ulubione = tkr.Button(top, text="Ulubione", width=20, font=30, bd=8, fg='Blue', bg="white", relief="raised",
                          command=lambda: wyswietl_ulubione(dane))
    ulubione.place(relx=0.189, rely=0.1)

    nazwa = tkr.Button(top, text="Nazwa", width=20, font=30, bd=8, bg="white", relief="raised",
                       command=lambda: sortuj_wg_nazwy(dane))
    nazwa.place(relx=0.02, rely=0.5)

    data = tkr.Button(top, text="Data", width=18, font=30, bd=8, bg="white", relief="raised",
                      command=lambda: sortuj_wg_daty(dane))
    data.place(relx=0.189, rely=0.5)

    kurs = tkr.Button(top, text="Kurs", width=18, font=30, bd=8, bg="white", relief="raised",
                      command=lambda: sortuj_wg_kurs(dane))
    kurs.place(relx=0.344, rely=0.5)

    zmiana = tkr.Button(top, text="Zmiana", width=18, font=30, bd=8, bg="white", relief="raised",
                        command=lambda: sortuj_wg_zmiana(dane))
    zmiana.place(relx=0.5, rely=0.5)

    wolumen = tkr.Button(top, text="Wolumen", width=18, font=30, bd=8, bg="white", relief="raised",
                         command=lambda: sortuj_wg_wolumen(dane))
    wolumen.place(relx=0.656, rely=0.5)

    obrot = tkr.Button(top, text="Obrot", width=18, font=30, bd=8, bg="white", relief="raised",
                       command=lambda: sortuj_wg_obrot(dane))
    obrot.place(relx=0.813, rely=0.5)

    frame = tkr.Canvas(root)
    frame.pack(side='left')
    scrollable_body = Scroll.Scrollable(frame, width=20)

    dane = sorted(dane, key=lambda dane_entry: float(dane_entry[3]))

    for i in dane:
        tabele.append(Akcja(i[0], i[2], i[1], i[4], i[5],i[3],scrollable_body))

    scrollable_body.update()


def sortuj_wg_obrot2(dane):
    list = root.pack_slaves()
    for l in list:
        l.destroy()
    tabele = []

    top = tkr.Canvas(root, width=1200, height=100, bd=5, relief='sunken')
    top.pack()

    wszystkie = tkr.Button(top, text="Wszystkie", width=20, font=30, bd=8, fg="Blue", bg="white", relief="raised")
    wszystkie.place(relx=0.02, rely=0.05)

    ulubione = tkr.Button(top, text="Ulubione", width=20, font=30, bd=8, fg='Blue', bg="white", relief="raised",
                          command=lambda: wyswietl_ulubione(dane))
    ulubione.place(relx=0.189, rely=0.1)

    nazwa = tkr.Button(top, text="Nazwa", width=20, font=30, bd=8, bg="white", relief="raised",
                       command=lambda: sortuj_wg_nazwy(dane))
    nazwa.place(relx=0.02, rely=0.5)

    data = tkr.Button(top, text="Data", width=18, font=30, bd=8, bg="white", relief="raised",
                      command=lambda: sortuj_wg_daty(dane))
    data.place(relx=0.189, rely=0.5)

    kurs = tkr.Button(top, text="Kurs", width=18, font=30, bd=8, bg="white", relief="raised",
                      command=lambda: sortuj_wg_kurs(dane))
    kurs.place(relx=0.344, rely=0.5)

    zmiana = tkr.Button(top, text="Zmiana", width=18, font=30, bd=8, bg="white", relief="raised",
                        command=lambda: sortuj_wg_zmiana(dane))
    zmiana.place(relx=0.5, rely=0.5)

    wolumen = tkr.Button(top, text="Wolumen", width=18, font=30, bd=8, bg="white", relief="raised",
                         command=lambda: sortuj_wg_wolumen(dane))
    wolumen.place(relx=0.656, rely=0.5)

    obrot = tkr.Button(top, text="Obrot", width=18, font=30, bd=8, bg="white", relief="raised",
                       command=lambda: sortuj_wg_obrot(dane))
    obrot.place(relx=0.813, rely=0.5)

    frame = tkr.Canvas(root)
    frame.pack(side='left')
    scrollable_body = Scroll.Scrollable(frame, width=20)

    dane = sorted(dane, key=lambda dane_entry: dane_entry[5])
    dane.reverse()
    for i in dane:
        tabele.append(Akcja(i[0], i[2], i[1], i[4], i[5],i[3],scrollable_body))

    scrollable_body.update()


def sortuj_wg_kurs(dane):
    list = root.pack_slaves()
    for l in list:
        l.destroy()
    tabele = []

    top = tkr.Canvas(root, width=1200, height=100, bd=5, relief='sunken')
    top.pack()

    wszystkie = tkr.Button(top, text="Wszystkie", width=20, font=30, bd=8, fg="Blue", bg="white", relief="raised")
    wszystkie.place(relx=0.02, rely=0.05)

    ulubione = tkr.Button(top, text="Ulubione", width=20, font=30, bd=8, fg='Blue', bg="white", relief="raised",
                          command=lambda: wyswietl_ulubione(dane))
    ulubione.place(relx=0.189, rely=0.1)

    nazwa = tkr.Button(top, text="Nazwa", width=20, font=30, bd=8, bg="white", relief="raised",
                       command=lambda: sortuj_wg_nazwy(dane))
    nazwa.place(relx=0.02, rely=0.5)

    data = tkr.Button(top, text="Data", width=18, font=30, bd=8, bg="white", relief="raised",
                      command=lambda: sortuj_wg_daty(dane))
    data.place(relx=0.189, rely=0.5)

    kurs = tkr.Button(top, text="Kurs", width=18, font=30, bd=8, bg="white", relief="raised",
                      command=lambda: sortuj_wg_kurs2(dane))
    kurs.place(relx=0.344, rely=0.5)

    zmiana = tkr.Button(top, text="Zmiana", width=18, font=30, bd=8, bg="white", relief="raised",
                        command=lambda: sortuj_wg_zmiana(dane))
    zmiana.place(relx=0.5, rely=0.5)

    wolumen = tkr.Button(top, text="Wolumen", width=18, font=30, bd=8, bg="white", relief="raised",
                         command=lambda: sortuj_wg_wolumen(dane))
    wolumen.place(relx=0.656, rely=0.5)

    obrot = tkr.Button(top, text="Obrot", width=18, font=30, bd=8, bg="white", relief="raised",
                       command=lambda: sortuj_wg_obrot(dane))
    obrot.place(relx=0.813, rely=0.5)

    frame = tkr.Canvas(root)
    frame.pack(side='left')
    scrollable_body = Scroll.Scrollable(frame, width=20)

    dane = sorted(dane, key=lambda dane_entry: dane_entry[2])

    for i in dane:
        tabele.append(Akcja(i[0], i[2], i[1], i[4], i[5],i[3],scrollable_body))

    scrollable_body.update()

def sortuj_wg_kurs2(dane):
    list = root.pack_slaves()
    for l in list:
        l.destroy()
    tabele = []

    top = tkr.Canvas(root, width=1200, height=100, bd=5, relief='sunken')
    top.pack()

    wszystkie = tkr.Button(top, text="Wszystkie", width=20, font=30, bd=8, fg="Blue", bg="white", relief="raised")
    wszystkie.place(relx=0.02, rely=0.05)

    ulubione = tkr.Button(top, text="Ulubione", width=20, font=30, bd=8, fg='Blue', bg="white", relief="raised",
                          command=lambda: wyswietl_ulubione(dane))
    ulubione.place(relx=0.189, rely=0.1)

    nazwa = tkr.Button(top, text="Nazwa", width=20, font=30, bd=8, bg="white", relief="raised",
                       command=lambda: sortuj_wg_nazwy(dane))
    nazwa.place(relx=0.02, rely=0.5)

    data = tkr.Button(top, text="Data", width=18, font=30, bd=8, bg="white", relief="raised",
                      command=lambda: sortuj_wg_daty(dane))
    data.place(relx=0.189, rely=0.5)

    kurs = tkr.Button(top, text="Kurs", width=18, font=30, bd=8, bg="white", relief="raised",
                      command=lambda: sortuj_wg_kurs(dane))
    kurs.place(relx=0.344, rely=0.5)

    zmiana = tkr.Button(top, text="Zmiana", width=18, font=30, bd=8, bg="white", relief="raised",
                        command=lambda: sortuj_wg_zmiana(dane))
    zmiana.place(relx=0.5, rely=0.5)

    wolumen = tkr.Button(top, text="Wolumen", width=18, font=30, bd=8, bg="white", relief="raised",
                         command=lambda: sortuj_wg_wolumen(dane))
    wolumen.place(relx=0.656, rely=0.5)

    obrot = tkr.Button(top, text="Obrot", width=18, font=30, bd=8, bg="white", relief="raised",
                       command=lambda: sortuj_wg_obrot(dane))
    obrot.place(relx=0.813, rely=0.5)

    frame = tkr.Canvas(root)
    frame.pack(side='left')
    scrollable_body = Scroll.Scrollable(frame, width=20)

    dane = sorted(dane, key=lambda dane_entry: float(dane_entry[2]))
    dane.reverse()
    for i in dane:
        tabele.append(Akcja(i[0], i[2], i[1], i[4], i[5],i[3],scrollable_body))

    scrollable_body.update()

class Akcja:
    def __init__(self,nazwa,kurs,data,wolumen,obrot,zmiana,scrollable_body):
        self.nazwa = nazwa
        self.kurs = float(kurs)
        self.zmiana = zmiana
        self.wolumen = wolumen
        self.obrot = obrot
        self.data = data
        self.canvas = tkr.Canvas(scrollable_body)
        self.canvas.pack()
        self.wykres = 0
        self.temp = 0
        self.line2 = 0
        self.space = 0
        self.space2 = 0
        self.dane_wykres = []
        self.but_ulub = 0
        self.ulubione = False
        self.info()


    def info(self):
        data = tkr.Label(self.canvas,text=self.data, width=20,height=2, font=30, bd=3, bg="white",relief='raised')
        data.grid(row=0,column = 1)

        kurs = tkr.Label(self.canvas, text=self.kurs,
                          width=20,height=2, font=30, bd=3, bg="white",relief='raised')
        kurs.grid(row=0, column=2)

        zmiana = tkr.Label(self.canvas, text=self.zmiana,
                         width=20, height=2, font=30, bd=3, bg="white", relief='raised')
        zmiana.grid(row=0, column=3)

        if self.zmiana[0] == '+':
            zmiana.configure(fg='green')
        elif self.zmiana[0] == '-':
            zmiana.configure(fg='red')

        wolumen = tkr.Label(self.canvas, text= self.wolumen,
                          width=20,height=2, font=30, bd=3, bg="white",relief='raised')
        wolumen.grid(row=0, column=4)

        obrot = tkr.Label(self.canvas, text=self.obrot,
                          width=20,height=2, font=30, bd=3, bg="white",relief='raised')
        obrot.grid(row=0, column=5)

        button = tkr.Button(self.canvas,text=self.nazwa, width=20, font=30, bd=8, bg="white", relief="raised",command = self.wyswietl)
        button.grid(row = 0,column = 0)

    def wyswietl(self):
        if self.temp == 0:

            name = self.nazwa.split(" (")
            self.dane_wykres = scrapper.image_download(name[0])
            data2 = {'Dni': [365,180,90, 31, 7, 1, 0],
                     'Kurs': [self.kurs-self.dane_wykres[0]-self.dane_wykres[1]-self.dane_wykres[2]-self.dane_wykres[3]-self.dane_wykres[4]-self.dane_wykres[5],self.kurs-self.dane_wykres[0]-self.dane_wykres[1]-self.dane_wykres[2]-self.dane_wykres[3]-self.dane_wykres[4],self.kurs-self.dane_wykres[0]-self.dane_wykres[1]-self.dane_wykres[2]-self.dane_wykres[3],self.kurs-self.dane_wykres[0]-self.dane_wykres[1]-self.dane_wykres[2],self.kurs-self.dane_wykres[0]-self.dane_wykres[1],self.kurs-self.dane_wykres[0],self.kurs]
                     }
            df2 = DataFrame(data2, columns=['Dni', 'Kurs'])
            figure = plt.Figure(figsize=(5, 4), dpi=100)
            ax2 = figure.add_subplot(111)
            figure.gca().invert_xaxis()
            self.line2 = FigureCanvasTkAgg(figure, self.canvas)
            self.line2.get_tk_widget().grid(row = 2,columnspan = 3)
            df2 = df2[['Dni', 'Kurs']].groupby('Dni').sum()
            df2.plot(kind='line', legend=True, ax=ax2, color='r', marker='o', fontsize=10)

            self.space = tkr.Label(self.canvas, text="", height=1)
            self.space.grid(row=1)

            self.space2 = tkr.Label(self.canvas, text="", height=1)
            self.space2.grid(row=4)


            if self.ulubione == False:
                self.but_ulub = tkr.Button(self.canvas, text="Dodaj do ulubionych", width=30, font=30, bd=8, bg="white",
                                  relief="raised", command= self.dodaj_do_ulub)
                self.but_ulub.grid(row=2, column = 3,columnspan=2)
            else:
                self.but_ulub = tkr.Button(self.canvas, text="Usun z ulubionych", width=30, font=30, bd=8, bg="white",
                                           relief="raised", command=self.usun_z_ulub)
                self.but_ulub.grid(row=1, column=3, columnspan=2)
            self.temp = 1
        else:
            self.line2.get_tk_widget().destroy()
            self.but_ulub.destroy()
            self.space.destroy()
            self.space2.destroy()
            self.temp = 0

    def dodaj_do_ulub(self):
        if ulubione_tab.count([self.nazwa,self.data,self.kurs,self.zmiana,self.wolumen,self.obrot]) == 0:
            ulubione_tab.append([self.nazwa,self.data,self.kurs,self.zmiana,self.wolumen,self.obrot])
            baza.insert(self.nazwa)
    def usun_z_ulub(self):
        if ulubione_tab.count([self.nazwa, self.data, self.kurs, self.zmiana, self.wolumen, self.obrot]) >= 1:
            ulubione_tab.remove([self.nazwa,self.data,self.kurs,self.zmiana,self.wolumen,self.obrot])
            baza.usun(self.nazwa)

        wyswietl_ulubione(dane)


sortuj_wg_nazwy(dane)


root.mainloop()