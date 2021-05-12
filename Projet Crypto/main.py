import tkinter as tk
from tkinter import Button, filedialog
from tkinter import simpledialog    


racine= tk.Tk()
racine.title('racine')

texte=""
solution=" "


def Met1():
    """permet de décoder le texte 1, qui est un code de césar dont la clé est 1"""
    global texte, resultat
    resultat.delete(0)
    clé = 1
    texte= entree_texte.get()
    for i in range(len(texte)):
        if not ord(texte[i])>96 or not ord(texte[i])<123:
            resultat.insert(i,texte[i])
        else:    
            num_lettre= ord(texte[i])-97
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


def quitter(x):
    x.destroy()


def affiche(texte):
    """affiche le résultat de Met4"""
    root=tk.Tk()
    root.title('Met4')

    reponsem4 = tk.Label(root, text= texte)
    reponsem4.grid(row=0, column=0)

    boutton_quitt= tk.Button(root, text='Quitter', command=lambda: quitter(root))
    boutton_quitt.grid(row=0, column=1)


def decryptV(lettre, x, cle):
    """permet de décrypter un code de vigenere, avec une lettre, 
    et la place de la lettre décodante dans la clé et la clé."""
    num_lettre = ord(lettre)-97
    lcode= ord(cle[x])-97
    nvl_lettre= chr((num_lettre-lcode)%26+ 97)
    return nvl_lettre



def Met3():
    """permet dedécoder le texte3"""
    resultat= ""
    rep=""
    cle= 'clez'
    texte= entree_texte.get()
    cpt= 0
    for i in range(len(texte)):
        if not ord(texte[i])>96 or not ord(texte[i])<123:
            resultat += texte[i]
        else:
            nvl_lettre= decryptV(texte[i],(cpt%len(cle)) ,cle)
            resultat += nvl_lettre
        cpt+= 1
    affiche(resultat)


def Met4():
    """Set a décoder le texte 4"""
    resultat.delete(0)
    lines = open("Texte 4.txt", "r")
    key = "bravez"
    newText = ""
    dclcle= [1, 0, 0, 2, 4, 5, 0, 3, 4, 5, 0, 4, 5, 0, 4, 5, 1, 5, 0]
    for line in lines:
        comptel=0
        line = line[::-1]
        newLine = ""
        cpt = 0
        for letter in line:
            if not ord(letter) > 96 or not ord(letter) < 123:
                newLine += letter
            else:
                newLine += decryptV(letter, cpt % len(key), key)
            cpt += 1
        key = key[len(key) - int(dclcle[comptel])] + key[:(len(key) -int(dclcle[comptel]))]
        newText += newLine + "\n" 
        comptel +=1
    affiche(newText)


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
resultat.grid(row=3,column=0, columnspan=3)


boutquitterracine= tk.Button(racine, text= "Quitter", command=lambda :quitter(racine))
boutquitterracine.grid(row=4, column= 2)

racine.mainloop()