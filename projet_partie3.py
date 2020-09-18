"""ANZID Ayoub, DUPIOT Louise - Groupe AFRIQUE"""
from os import system
import os
import copy
from json import dumps, loads
def indice_valide(plateau,indice):
    if indice <= (plateau['n']-1) and indice >= 0: #vérifie que l'indice est compris entre 0 et n la longeur max du tableau
        return True
    return False

def case_valide (plateau, i, j):
    if indice_valide(plateau,i) and indice_valide(plateau,j):  #vérifie que l'indice i et j sont compris entre 0 et n la longeur max du tableau
        return True
    return False

def get_case(plateau,i,j):
    assert case_valide(plateau,i,j) #si la case est valide
    return plateau ['cases'] [plateau['n']*i+j] #retourne la valeur de la case

def set_case(plateau,i,j,val):
    assert case_valide(plateau,i,j) and 0 <= val and val <= 2 # si la case est valide et que la valeur est compris entre 0 et 2
    plateau["cases"][plateau["n"]*i+j]=val #change la valeur de la case en la valeur mit en paramètre
    return plateau

def creer_plateau(n):
    assert n==4 or n==6 or n==8 #n doit être égale a 4 et 6 et 8
    tab=[]
    i=0
    while i<n*n:
        tab.append(0) # on remplit le tableau de 0
        i=i+1
    plateau={"n":n,"cases":tab}
    set_case(plateau,n//2-1,n//2-1,2)# les coordonnées des pions centraux
    set_case(plateau,n//2-1,n//2,1)
    set_case(plateau,n//2,n//2-1,1)
    set_case(plateau,n//2,n//2,2)
    return plateau
print(creer_plateau(4))


def afficher_plateau1(plateau):
    i=0
    while i<plateau["n"]: #on fait sa n fois ( pour chaque ligne )
        a=""
        j=0
        while j<plateau["n"]: #on fait sa n fois ( pour chaque colonne )
            a=a+str(get_case(plateau,i,j))+" " # on sauvagarde la valeur d'avant et on rajoute la valeur suivant
            j=j+1
        i=i+1
        print(a) #a égale a la ligne i, l'objectif est de print ligne par ligne le plateau


def afficher_plateau2(plateau):
    taille = len(plateau)
    indice = 0
    a = 0
    tab2 = []                       #forme un tableau vide
    while a < taille:
        if cases[a] == 1:             #si la valeur de la case est 1
            tab2.append("N")        #on ajoute la lettre N au tableau vide (tab2)
        elif cases[a] == 2:
            tab2.append("B")
        elif plateau[a] == 0:           #si la valeur de la case est 0
            tab2.append(" ")        #on ajoute un espace au tab2
        a += 1
        plateau={"n":n,"cases":tab}
    nbetoiles = (8*n)+1             #nombre d'étoiles sur les grandes lignes du tableau
    nblignes = (4*n)+1              #nombre d'étoiles sur les lignes verticales du tableau
    i = 0
    while i < nblignes:
        if i%4 == 0:                #quand i est un multiple de 4
            j = 0
            while j < nbetoiles:
                print("*",end = "") #affiche les grandes lignes du tableau
                j += 1
            print(" ")
        elif i%4 == 2:              #désigne la 2e ligne en-dessous de la grande ligne
            k = 0
            while k < n:
                print("*  ",plateau["cases"],"  ",end = "")  #affiche la ligne contenant les valeurs du tableau
                indice += 1         #incrémentation des indices de tab2
                k += 1
            print("*")              #rajoute l'étoile manquante sur les lignes contenant les valeurs et fait un retour à la ligne
        else:
            l = 0
            while l < n:
                print("*       ",end = "") #affiche les lignes pour dessiner les cases du tableau
                l += 1
            print("*")               #rajoute l'étoile manquante sur les lignes entre les grandes lignes et fait un retour à la ligne
        i += 1

n=4
p=creer_plateau(n)
afficher_plateau1(p)









def afficher_plateau(plateau):

    #Variables
    cpt_lig=0                   #Compteur de petites lignes
    plat=copy.deepcopy(plateau)
    n=plat["n"]
    etoiles_sep_lignes=n*8+1
    nb_lignes=4*n
    indice=0

    a=0
    while a<len(plat["cases"]):
        if plat["cases"][a]==1:
            plat["cases"][a]=("N")    #Remplace 1 par "N"
        if plat["cases"][a]==2:
            plat["cases"][a]=("B")    #Remplace 2 par "B"
        if plat["cases"][a]==0:
            plat["cases"][a]=(" ")    #Remplace 0 par " " (vide)
        a+=1

    while cpt_lig<nb_lignes+1:

        if cpt_lig%4==0:
            etoile=0
            while etoile<etoiles_sep_lignes:
                print("*",end="")
                etoile+=1
            print("")

        elif cpt_lig%4==2:
            cpt=0
            while cpt<n:
                print("*  ",plat["cases"][indice],"  ",end="")
                cpt+=1
                indice+=1
            print("*")

        else:
           cpt=0
           while cpt<n:
                print("*       ",end="")
                cpt+=1
           print("*")

        cpt_lig+=1







def pion_adverse(joueur):
    if(joueur == 1):
        return 2
    elif(joueur == 2):
        return 1
    assert not pion_adverse(3), "erreur"




def prise_possible_direction(p, i, j, vertical, horizontal, joueur):    #toutes directions possibles à l'horizontale et à la verticale par rapport à i et j entre -1 et 1
    if not(case_valide(p,i+vertical,j+horizontal)):                     #si case non  valide : faux
        return False
    if get_case(p,i+vertical,j+horizontal)==0 or not(get_case(p,i+vertical,j+horizontal)==pion_adverse(joueur)):   #si case vide ou case ne contient pas le pion adverse : faux
        return False
    v=vertical
    h=horizontal
    while case_valide(p,i+vertical+v,j+horizontal+h):          #vérifie toutes les cases valides
        if get_case(p,i+vertical+v,j+horizontal+h)==joueur:    #vérifie la case du joueur
            return True
        elif get_case(p,i+vertical+v,j+horizontal+h)==0:
            return False
        else:
            vertical=vertical+v
            horizontal=horizontal+h
    return False

def test_prise_possible_direction(p):
        if p["n"] == 4:
            assert not (prise_possible_direction(p,1,3,0,-1,1)),"erreur"
            assert (prise_possible_direction(p,1,3,0,-1,2))
            assert not (prise_possible_direction(p,1,3,-1,-1,2)),"erreur"


p = creer_plateau(4)

test_prise_possible_direction(p)
print(prise_possible_direction(p,1,3,0,-1,2)) #True
print(prise_possible_direction(p,1,3,0,-1,1))  #retourne False
print(prise_possible_direction(p,1,3,-1,-1,2)) #retourne False
print(prise_possible_direction(p,1,0,0,1,1))   #True

def mouvement_valide(plateau, i, j, joueur):
    if get_case(plateau,i,j)==0:              #si case vide : vérifie tous les mouvements possibles
        v=-1
        while v<=1:
            h=-1
            while h<=1:
                if prise_possible_direction(plateau,i,j,v,h,joueur):   #vérifie si il y a une prise possible
                    return True
                h=h+1
            v=v+1
    return False

p = creer_plateau(4)

def test_mouvement_valide():
    assert not (mouvement_valide(p,0,0,1)), "erreur"
    assert (mouvement_valide(p,1,3,2))


test_mouvement_valide()
print(mouvement_valide(p,1,3,2)) # retourne True
print(mouvement_valide(p,0,0,1)) # retourne False

def mouvement_direction(plateau, i, j, vertical, horizontal, joueur):
    if (prise_possible_direction(plateau, i, j, vertical, horizontal, joueur)):
        v = vertical + i
        h = horizontal + j
        while get_case(plateau,v,h) == pion_adverse(joueur):
            set_case(plateau,i+vertical,j+horizontal,joueur)
            v += vertical
            h += horizontal
        return plateau


def test_mouvement_direction():
    assert (p["cases"] == p["cases"])
    mouvement_direction(p,1,3,0,-1,2)
    assert (p["cases"][n*1+(3-1)] == 2)
"""
p = creer_plateau(4)
test_mouvement_direction()
mouvement_direction(p,0,3,-1,1,2) # ne modifie rien
mouvement_direction(p,1,3,0,-1,2) # met la valeur 2 dans la case (1,2)
afficher_plateau1(p)"""

def mouvement(plateau, i, j, joueur):
    if (mouvement_valide(plateau, i, j, joueur)):   #vérifie si mouvement valide
        set_case(plateau,i,j,joueur)                #met le pion du joueur en (i,j)
        v = -1
        while v <= 1:
            h = -1
            while h <= 1:
                mouvement_direction(plateau,i,j,v,h,joueur)  #met la valeur dans la case (i+v,j+h)
                h += 1
            v += 1
    return plateau
"""
p = creer_plateau(4)
mouvement(p,0,3,2) # ne modifie rien
mouvement(p,1,3,2) # met la valeur 2 dans les cases (1,2) et (1,3)
afficher_plateau1(p)"""

def joueur_peut_jouer(plateau, joueur):
    i = 0
    while i < plateau["n"]:
        j = 0
        while j < plateau["n"]:
            if mouvement_valide(plateau,i,j,joueur):
                return True
            j += 1
        i +=1
    return False


def test_joueur_peut_jouer():
    assert joueur_peut_jouer(p,1)
"""
p = creer_plateau(4)
print(joueur_peut_jouer(p,1)) # retourne True
# On remplace les pions du joueur 2 par des pions du joueur 1
set_case(p,1,1,1)
set_case(p,2,2,1)
afficher_plateau1(p)
print(joueur_peut_jouer(p,1)) # retourne False"""

def fin_de_partie(plateau):
    if (joueur_peut_jouer(plateau,1) == False and joueur_peut_jouer(plateau,2) == False):
        return True
    else:
        return False
"""
p = creer_plateau(4)
print(fin_de_partie(p)) # retourne False
# On remplace les pions du joueur 2 par des pions du joueur 1
set_case(p,1,1,1)
set_case(p,2,2,1)
afficher_plateau1(p)
print(fin_de_partie(p)) # retourne True"""

def gagnant(plateau):
    a = 0
    b = 0
    i = 0
    while i < plateau["n"] :
        j = 0
        while j < plateau ["n"]:
            if get_case(plateau,i,j) == 1:
                a += 1
            elif get_case(plateau,i,j) == 2:
                b += 1
            j += 1
        i += 1
    if a > b:
        return 1
    elif a < b:
        return 2
    else:
        return 0

"""p = creer_plateau(4) # On remplace les pions du joueur 2 par des pions du joueur 1
set_case(p,1,1,2)
set_case(p,2,2,2)
set_case(p,2,2,1)
afficher_plateau1(p)
gagnant(p) # retourne 1"""

##### PARTIE 3 #####

def creer_partie(n): #crée un dictionnaire avec le numéro du joueur et le plateau de jeu 

    partie ={ "joueur" : 1,"plateau": creer_plateau(n)}
    return partie
"""print(creer_partie(4))"""

def test_creer_partie(n):
    assert creer_partie(4)
    assert not creer_partie(3)
    assert  creer_partie(6)
    assert not creer_partie(7)
    assert  creer_partie(8)

def saisie_valide(partie, s): #vérifie si la saisie du joueur est valide grâce à la fonction mouvement valide et retourne True si saisie valide ou si le joueur veut accéder au menu
    if( s =="M"):
        return True
    car = "abcdefgh"
    nb ="12345678"
    i=0
    while(i < n):
        j=0
        while(j< n):

            if(car[i] == s[0] and nb[j] == s[1] and mouvement_valide(partie["plateau"],i,j,partie["joueur"])):
                return True
            j+=1
        i+=1
    return False

def test_saisie_valide(partie, s):
    partie = creer_partie
    assert saisie_valide(partie,"a1")
    assert not saisie_valide(partie,"A1")
    assert not saisie_valide(partie,"H8")

"""p = creer_partie(4)
print(saisie_valide(p,"b4")) # retourne True"""

def effacer_terminal():
        """Efface le terminal."""
        #system('clear') #pour linux
        system('cls') #pour Windows


def tour_jeu(partie): #affiche plateau de jeu, vérifie si le joueur peut jouer  
    effacer_terminal()
    afficher_plateau(partie["plateau"])
    if(joueur_peut_jouer(partie["plateau"],partie["joueur"]) == True): #si joueur_peut_jouer est vrai 
        print("Faire un mouvement") #demande au joueur de  saisir un mouvement 
        s =""
        s = str(input())
        car = "abcdefgh"
        nb ="12345678"
        while(saisie_valide(partie,s) == False): #demande une saisie valide au joueur 
            s = str(input())
        if(s == "M" and saisie_valide(partie,s) == True): # retourne False si le joueur veut accéder au menu 
             return False 
        i = 0
        while(i < n):
            j=0
            while(j < n):
                if(car[i] == s[0] and nb[j]==s[1]): 
                    mouvement(partie["plateau"],i,j,partie["joueur"]) #effectue le mouvement saisit par le joueur et return True 
                    return True 
                j+=1
            i+=1
    elif(joueur_peut_jouer(partie["plateau"],partie["joueur"]) == False): 
        return False #retourne False si le joueur ne peut pas jouer 

def test_tour_jeu(n):
    partie = creer_partie(n)
    a = saisir_action(partie)
    assert (a == 5) #6
    assert (a == 4 )
"""
p = creer_partie(4)
print(tour_jeu(p))
afficher_plateau(p["plateau"])"""

def saisir_action(partie): #menu du jeu
    print("0 : terminer partie ; 1:commencer une nouvelle partie ; 2:pour charger une partie ;3:sauvegarder partie ; 4 pour reprendre la partie")  
    n=int(input()) #demande une option au joueur
    while(n<0 or n>4):
        n=int(input())
    return n

"""n = saisir_action(None)
print(n)"""



def jouer(partie) :

     while(tour_jeu(partie) != False and fin_de_partie(partie["plateau"]) == False): 
            if(joueur_peut_jouer(partie["plateau"],partie["joueur"]) == True) : #tant que le joueur peut jouer et que la partie n'est pas finie 
                partie["joueur"] = pion_adverse(partie["joueur"])  #change le joueur courant



     if(tour_jeu(partie) == False):
        fin_de_partie(partie["plateau"])
        g = gagnant(partie["plateau"])
        print("test2")
        if(g == 1 or g == 2):
            print("le joueur",g,"a gagner")
        elif(g == 0) :
            print("il y a egalité")






def test_jouer():
    p = creer_partie(4)
    assert jouer(p)





"""p = creer_partie(4)
res = jouer(p)
print(res)"""

def saisir_taille_plateau(): 
    print("saisir une taille 4 , 6 ,8")
    n=int(input())
    return n


"""n = saisir_taille_plateau()
print(n)"""
def test_saisir_taille_plateau():
    assert  saisir_taille_plateau() == 4 or saisir_taille_plateau() == 6 or saisir_taille_plateau()== 8

def sauvegarder_partie(partie):
    part = str(partie)
    f = open("sauvegarde_partie.json", "w")
    f.write(part)
    f.close()

def test_sauvegarder_partie() :
    assert sauvegarder_partie(p)
"""p = creer_partie(4)
sauvegarder_partie(p)"""



def charger_partie():
    if os.path.exists("sauvegarde_partie.json"):
        print("Le fichier sauvegarde_partie.json existe.")
        f = open("sauvegarde_partie.json", "r")
        chaine = f.read()
        f.close()
        charge = dumps(chaine)
        char = loads(charge)
        print(char)

    else:
        print("Le fichier sauvegarde_partie.json n'existe pas.")

def test_charger_partie():
    assert charger_partie(),"True"


"""p = charger_partie()"""



def othello(): #commence par le menu et demande une option au joueur 
    a = 6
    while(a !=0):
        a = saisir_action(None)
        if( a == 1):
            """nouvelle partie"""
            n = saisir_taille_plateau()
            p=creer_partie(n)
            if(jouer(p) == True):
                p = none
        elif(a == 2):
            """charger une partie"""
            p=charger_partie()
        elif(a == 3):
            sauvegarder_partie(p)
        elif(a == 0):
            """quitter la partie"""
            return False

""" print("je suis la")
    a = saisir_action(None)
    if( a == 1):

        n = saisir_taille_plateau()
        p=creer_partie(n)
    elif(a == 2):

        p=charger_partie()
    elif(a == 0):

        return False

    while(a!=0):

        if(jouer(p) == False):
            a = saisir_action(p)
            if( a == 1):

                n = saisir_taille_plateau()
                p=creer_partie(n)
            elif(a == 2):

                p=charger_partie()
            elif(a == 3):
                sauvegarder_partie(p)
            elif(a == 0):
                return ("rien")
        elif(jouer(p) == True):
            if(tour_jeu(p) == False):
                a = saisir_action(none)
                if( a == 1):

                    n = saisir_taille_plateau()
                    p=creer_partie(n)
                elif(a == 2):

                    p=charger_partie()
                elif(a == 0):

                    return False """



othello()

