import tkinter as tk

racine= tk.Tk()
racine.title('racine')

texte=""
solution=" "

def defilGest(L):
    op, deCombien = L[0], L[1]

    if op == 'scroll':
        units = L[2]
        saisi.xview_scroll(deCombien, units)
    elif op == 'moveto':
        saisi.xview_moveto(deCombien)


def Met1():
    """permet de décoder le texte 1, qui est un code de césar dont la clé est 1"""
    global texte, resultat
    resultat.delete(0)
    rep = ""
    clé = 1
    texte= entree_texte.get()
    for i in range(len(texte)):
        if not ord(texte[i])>96 or not ord(texte[i])<123:
            resultat.insert(i,texte[i])
        else:    
            num_lettre= (ord(texte[i])%26)-97
            nvl_lettre= chr((num_lettre+clé)%26+97)
            resultat.insert(i,nvl_lettre)

def decrypt2(i):
    """permet de décoder la lettre"""
    res= ""
    if i == 'a':
        res += 'z'
    elif i == "c" :
        res += 'd'
    elif i == "d" :
        res += 'n'
    elif i == "f" :
        res += 'm'
    elif i == "g" :
        res += 'l'
    elif i == "i" :
        res += 's'
    elif i == "k" :
        res += 'i'
    elif i == "l" :
        res += 'h'
    elif i == "m" :
        res += 'g'
    elif i == "n" :
        res += 'a'
    elif i == "o" :
        res += 'r'
    elif i == "q" :
        res += 'p'
    elif i == "s" :
        res += 'o'
    elif i == "u" :
        res += 't'
    elif i == "v" :
        res += 'c'
    elif i == "w" :
        res += 'f'
    elif i == "x" :
        res += 'e'
    elif i == "y" :
        res += 'u'
    return res


def Met2():
    """permet de décoder le texte2"""
    resultat.delete(0)
    rep=""
    texte=entree_texte.get()
    for i in range(len(texte)):
        if not ord(texte[i])>96 or not ord(texte[i])<123:
            resultat.insert(i,texte[i])
        else:
            nvl_lettre= decrypt2(texte[i])
            resultat.insert(i,nvl_lettre)


def Met3():
    """permet dedécoder le texte3"""
    
    pass


def Met4():
    """inch"""
    pass



entree_texte = tk.Entry(racine, width = 50, font = ("helvetica", "20"))
entree_texte.grid(row = 0, column = 0, columnspan=3)

butt1 = tk.Button(racine, text='Texte 1', font = ("helvetica", "20"), command=Met1)
butt1.grid(row=1, column=0)

butt2 =tk.Button(racine, text='Texte 2', font = ("helvetica", "20"), command=Met2)
butt2.grid(row=1, column=1)

butt3=tk.Button(racine, text='Texte 3', font = ("helvetica", "20"), command=Met3)
butt3.grid(row=1, column=2)

butt4=tk.Button(racine, text='Texte 4', font = ("helvetica", "20"), command=Met4)
butt4.grid(row=1, column=3)

label_texte = tk.Label(racine,font = ("helvetica", "20"), text = "Entrer le message ici.")
label_texte.grid(row = 0, column = 4)


label_dech = tk.Label(racine,font = ("helvetica", "20"), text = "Déchiffre ici")
label_dech.grid(row = 3, column = 4)


resultat=tk.Entry(racine,width = 50, font = ("helvetica", "20"), text=solution)
resultat.grid(row=3,column=0, columnspan=3, sticky='nsew')

resultatDefil = tk.Scrollbar(racine, orient='horizontal', command= defilGest)
resultatDefil.grid(row=4, column=0, columnspan=3, sticky='nsew')
resultat['xscrollcommand']= resultatDefil.set


racine.mainloop()