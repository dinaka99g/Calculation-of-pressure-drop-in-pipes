import tkinter as tk
from matplotlib import pyplot as plt
import math
root=tk.Tk() 
root.title('Dina Karamuratović')
root.geometry('300x500')
#Deklaracija varijabli
protok=tk.DoubleVar()
precnik_cijevi=tk.DoubleVar()
brzina=tk.DoubleVar()
koef_trenja=tk.DoubleVar()
duzina_cjevovoda=tk.DoubleVar()
gustina=tk.DoubleVar()
gustina.set(1000)
ubrzanje=tk.DoubleVar()
ubrzanje.set(9.81)
bruto_pad=tk.DoubleVar()
v_instalacioni=tk.DoubleVar()
faktor_materijala=tk.DoubleVar()
formula_rejnolds=tk.DoubleVar()
lambdica=tk.DoubleVar()
hglin=tk.DoubleVar()
hglok=tk.DoubleVar()
hguk=tk.DoubleVar()
hef=tk.DoubleVar()
pad_pritiska=tk.DoubleVar()
proc=tk.DoubleVar()
#Varijablice
def protok_precnik():
    clearFrame()
    tk.Label(root,textvariable=staje_poznato).pack()
    tk.Label(text='Unesi protok u m3/s').pack()
    tk.Entry(textvariable=protok).pack()
    tk.Label(text='Unesi precnik u m').pack()
    tk.Entry(textvariable=precnik_cijevi).pack()
    tk.Label(text='Unesi koef trenja').pack()
    tk.Entry(textvariable=koef_trenja).pack()
    tk.Label(text='Unesi duzinu cjevovoda u m').pack()
    tk.Entry(textvariable=duzina_cjevovoda).pack()
    tk.Label(text='Unesi bruto pad u m').pack()
    tk.Entry(textvariable=bruto_pad).pack()
    tk.Label(text='Unesi faktor materijala').pack()
    tk.Entry(textvariable=faktor_materijala).pack()
    tk.Button(text='Izračunaj',command=proracun,bg='yellow').pack()
def protok_brzina():
    clearFrame()
    tk.Label(root,textvariable=staje_poznato).pack()
    tk.Label(text='Unesi protok').pack()
    tk.Entry(textvariable=protok).pack()
    tk.Label(text='Unesi brzinu').pack()
    tk.Entry(textvariable=brzina).pack()
    tk.Label(text='Unesi koef trenja').pack()
    tk.Entry(textvariable=koef_trenja).pack()
    tk.Label(text='Unesi duzinu cjevovoda').pack()
    tk.Entry(textvariable=duzina_cjevovoda).pack()
    tk.Label(text='Unesi bruto pad').pack()
    tk.Entry(textvariable=bruto_pad).pack()
    tk.Label(text='Unesi faktor materijala').pack()
    tk.Entry(textvariable=faktor_materijala).pack()
    tk.Button(text='Izračunaj',command=proracun,bg='yellow').pack()
def clearFrame():
   
    for widget in root.winfo_children():
       widget.destroy()
def racunanje_brzine():
    formulav_instalacioni=protok.get()*1.46
    v_instalacioni.set(formulav_instalacioni)
    formula_brzina=v_instalacioni.get()/((precnik_cijevi.get()**2)*3.14/4)
    brzina.set(formula_brzina)
def racunanje_precnika():
    v_instalacioni.set(1.46*protok.get())
    formula_precnik_cijevi=(4*v_instalacioni.get()/(3.14*brzina.get()))**0.5
    precnik_cijevi.set(formula_precnik_cijevi)

#poznato
staje_poznato=tk.StringVar()
staje_poznato.set('Šta je poznato?')
tk.Label(root,textvariable=staje_poznato).pack()
tk.Radiobutton(root, text="Protok-Prečnik", variable=staje_poznato, value='Proračun za poznat protok i prečnik', command=protok_precnik).pack()
tk.Radiobutton(root, text="Protok-Brzina", variable=staje_poznato, value='Proračun za poznat protok i brzinu',command=protok_brzina).pack()

#Tkinter
def proracun():
    root_novi=tk.Tk()
    root_novi.title('Proračun')
    root_novi.geometry('400x200')
    if brzina.get()==0:
        racunanje_brzine()
    if precnik_cijevi.get()==0:
        racunanje_precnika()
    #Re
    formula_rejnolds.set(gustina.get()*brzina.get()/koef_trenja.get())
    tk.Label(root_novi,text='Rejnoldsov broj je',bg='yellow').pack()
    tk.Label(root_novi,text=formula_rejnolds.get(),bg='yellow').pack()
    #Lambda
    c1=tk.DoubleVar()
    c2=tk.DoubleVar()
    c1.set((-2.456*math.log(((7/formula_rejnolds.get())**0.9+faktor_materijala.get()/(3.7*(precnik_cijevi.get())))))**16)
    c2.set((37530/formula_rejnolds.get())**16)
    formula_lambdica=tk.DoubleVar()
    formula_lambdica.set(8*((8/formula_rejnolds.get())**(1/12)+(c1.get()+c2.get())**(-3/2))**(1/12))
    tk.Label(root_novi,text='Lambda je:',bg='grey').pack()
    tk.Label(root_novi,text=formula_lambdica.get(),bg='grey').pack()
    #hglin
    hglin.set(formula_lambdica.get()*duzina_cjevovoda.get()*brzina.get()*brzina.get()/(precnik_cijevi.get()*2*ubrzanje.get()))
    #hglok
    hglok.set(0.05*bruto_pad.get())
    #hguk
    hguk.set(hglin.get()+hglok.get())
    #hef
    hef.set(bruto_pad.get()-hguk.get())
    #proc
    proc.set((hguk.get()/bruto_pad.get())*100)
    tk.Label(root_novi,text='Procentualni gubitak je:',bg='blue').pack()
    tk.Label(root_novi,text=proc.get(),bg='blue').pack()
    #Pad pritiska
    pad_pritiska.set(formula_lambdica.get()*gustina.get()*brzina.get()*brzina.get()*duzina_cjevovoda.get()/(2*precnik_cijevi.get()))
    tk.Label(root_novi,text='Pad pritiska je:',bg='pink').pack()
    tk.Label(root_novi,text=pad_pritiska.get(),bg='pink').pack()
    tk.Button(root_novi,text='Grafik efektivnog pada po dužini cijevi',command=prikaz).pack()
    
def prikaz():
    
    plt.title('Efektivni pad po dužini cijevi')
    x=[0,duzina_cjevovoda.get()]
    y=[bruto_pad.get(),hef.get()]
    lokalni_gubitci=[hglok.get(),hglok.get()]
    plt.plot(x,y)
    plt.plot(x,lokalni_gubitci)
    plt.legend(['Ukupni gubitci','Lokalni gubitci'])
    plt.show()

root.mainloop()