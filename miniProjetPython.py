###### Initialisation des variables globales des elements du Jeu
  
# Jx et Jy la position initiale du joueur
Jx= 9
Jy= 9
  
# Bx et By la position initile de la bombe
Bx= 1
By= 1
Bombe= True

# Plateau de Jeu
Plateau= []

# Taille du Plateau de Jeu
Px = 20
Py = 20

# Liste des Mx,My la position des Mechants
Mechants= [[0,0],[19,0],[0,19],[19,19],[0,9],[9,0],[9,19],[19,9]]

# Fin Jeu 
playerisDead = False



####### 1 Fonction Principale du Jeu
def Start():
  print("Bienvenu dans le jeu GamePy.\nVous devez deplacer sur le plateau le hero representer par le symbole :@ \n")
  print("à l'aide des touche de direction ou les lettres\n Z: haut, S: Bas, Q: Gauche, D: Droite\n")
  print("faite attention au bandits represnter par le symbole:$")
  print("ravitailler vous en bombe dans l'espace representer par le symbole:o, lancer votre bombe avec la touche B\n")
  print("\n\n")
  
  createPlateau()  
  printPlateau()
  while not finJeu() :
    actionPlayer()
    actionOrdinateur()
    

#######2 Fonction d'initialisation du plateau de Jeu (liste bidimensionnelle de xLignes et yColonnes) 
def createPlateau():
  global Plateau
  
  i = 1
  while i <=Px:
    j = 1
    listeColonne = []
    while j <=Py: 
      listeColonne.append(' ')
      j = j +1
    Plateau.append(listeColonne)
    i = i + 1
  #position de l'emplacement de la bombe
  Plateau[Bx][By] = '0'  
  #position de mon joueur
  Plateau[Jx][Jy] = '@'
  #position des mechants
  i=0
  while i< len(Mechants):
    Plateau[Mechants[i][0]][Mechants[i][1]] = '$'
    i= i+1
    
  return Plateau

#######3 Fonction d'affichage graphique des elements du plateau de Jeu
def printPlateau():
  i = 0
  while i < len(Plateau):
    print(Plateau[i])
    i = i + 1

  print('\n\n')
  return 0
    

#######4 Fonction du deplacement du Héro 

def actionPlayer():
  global Plateau
  global Bombe
  global Jx
  global Jy
  global playerisDead
  
  
  while playerisDead == False :
       
      while True:
        print("A votre tour de jouer\n Z: haut, S: Bas, Q: Gauche, D: Droite, Et B: BOMBE \n")
        playerChoice = input().upper()
        if playerisDead == True :
          break
        if playerChoice in ['Z','S','Q','D','B']:
            break

      ####GAUCHE
      if playerChoice == "Q":
        # deplacement vers la Gauche, nous verifions que Joueur (Jx,Jy) n'est pas hors plateau
        if Jy - 1 < 0 :
          print("\n /!\ Deplacement Impossible !!! \n")
          break
        else :
          regleJeu(playerChoice)

      ####DROITE
      if playerChoice == "D":
        # deplacement vers la Droite, nous verifions que Joueur (Jx,Jy) n'est pas hors plateau
        if Jy + 1 >= Py :
          print("\n /!\ Deplacement Impossible !!! \n")
          break
        else :
          regleJeu(playerChoice)

      ####HAUT
      if playerChoice == "Z":
        # deplacement vers le Haut, nous verifions que Joueur (Jx,Jy) n'est pas hors plateau
        if Jx - 1 < 0 :
          print("\n /!\ Deplacement Impossible !!! \n")
          break
        else :
          regleJeu(playerChoice)

      ####BAS
      if playerChoice == "S":
        # deplacement vers le Haut, nous verifions que Joueur (Jx,Jy) n'est pas hors plateau
        if Jx + 1 >= Px :
          print("\n /!\ Deplacement Impossible !!! \n")
          break
        else :
          regleJeu(playerChoice)

      ####BOMBE
      if playerChoice == "B":
        if Bombe :
          # Si bombe disponbile alors lancer, Appliquer regle pour supprimer les mechants touchés
          printBombe(Jx,Jy)
        else :
          # Verifier si ravitaillement possible
          return 0
      
  
  return 0


#######5 Fonction d'affichage graphique des effets de la bombe sur plateau de Jeu
def printBombe(x,y):
  global Plateau
  global Mechants

  i = 0
  j = 0
  while i <Px :
    Plateau[i][Jy] = '#'
    i = i+1
  while j <Py : 
    Plateau[Jx][j] = '#'
    j = j +1
    
  #position de mon joueur
  Plateau[Jx][Jy] = '@'
  #position des mechants
  k = 0
  while k< len(Mechants):
    Plateau[Mechants[k][0]][Mechants[k][1]] = '$'
    k = k+1
  
  printPlateau()
  
  i = 0
  j = 0
  while i <Px :
    Plateau[i][Jy] = ' '
    i = i+1
  while j <Py : 
    Plateau[Jx][j] = ' '
    j = j +1
    
  #position de mon joueur
  Plateau[Jx][Jy] = '@'
  
  #position des mechants
  k = 0
  print(Mechants)
  while k< len(Mechants):
    Plateau[Mechants[k][0]][Mechants[k][1]] = '$'
    k = k+1
  
      

  print('\n\n')
  return 0

#######6 Fonction d'application des regles du Jeu 

def regleJeu(action):  
  global Plateau
  global Mechants
  global Bombe
  global Jx
  global Jy
  global playerisDead
  
  # Regle de deplacement vers la GAUCHE
  if action == "Q":
    # Verifier si zone de ravitaillement en bombe
    if Jy - 1 == By and Jx == Bx :
      if not Bombe :
        while True:
          print('/!\ Zone de ravitaillment de bombe')
          print('Appuyez B pour recupperer, C pour annuler')
          bombeChoice = input().upper()
          
          if bombeChoice in ['B','C']:
            break
          if bombeChoice == 'B' :
            Bombe = True
            print('Vous avez une Bombe \o/')

    # Verifier si zone occupé par un mechant
    else :
      i = 0
      while i < len(Mechants) :
        if Mechants[i][0] == Jx and Mechants[i][1] == Jy -1 :
          print(' Your are Dead !!!')
          # effacer lancien position du Joueur
          Plateau[Jx][Jy] = ' '  
          playerisDead = True
          return playerisDead
        else :
          i = i+1
      
      if playerisDead == False :
        #effacer lancien position du Joueur
        Plateau[Jx][Jy] = ' '
        # repositionner le jouer
        Jy = Jy - 1 
        Plateau[Jx][Jy] = '@'
        
        printPlateau()
      
  # Regle de deplacement vers la DROITE
  if action == "D":
    # Verifier si zone de ravitaillement en bombe
    if Jy + 1 == By and Jx == Bx :
      if not Bombe :
        while True:
          print('/!\ Zone de ravitaillment de bombe')
          print('Appuyez B pour recupperer, C pour annuler')
          bombeChoice = input().upper()
          if bombeChoice in ['B','C']:
            break
        if bombeChoice == 'B' :
          Bombe = True
          print('Vous avez une Bombe \o/')
    # Verifier si zone occupé par un mechant
    else :
      i = 0
      while i < len(Mechants) :
        if Mechants[i][0] == Jx and Mechants[i][1] == Jy +1 :
          print(' Your are Dead !!!')
          # effacer lancien position du Joueur
          Plateau[Jx][Jy] = ' '  
          playerisDead = True
          return playerisDead
        else :
          i = i+1
    
    if playerisDead == False :
      # effacer lancien position du Joueur
          Plateau[Jx][Jy] = ' '
          # repositionner le jouer
          Jy= Jy + 1
          Plateau[Jx][Jy] = '@'
          printPlateau()
      
# Regle de deplacement vers le HAUT
  if action == "Z":
    # Verifier si zone de ravitaillement en bombe
    if Jy == By and Jx - 1 == Bx :
      if not Bombe :
        while True:
          print('/!\ Zone de ravitaillment de bombe')
          print('Appuyez B pour recupperer, C pour annuler')
          bombeChoice = input().upper()
          if bombeChoice in ['B','C']:
            break
        if bombeChoice == 'B' :
          Bombe = True
          print('Vous avez une Bombe \o/')
    # Verifier si zone occupé par un mechant
    else :
      i = 0
      while i < len(Mechants) :
        if Mechants[i][0] == Jx - 1 and Mechants[i][1] == Jy :
          print(' Your are Dead !!!')
          # effacer lancien position du Joueur
          Plateau[Jx][Jy] = ' '  
          playerisDead = True
          return playerisDead
        else :
          i = i+1
    
    if playerisDead == False :
      # effacer lancien position du Joueur
          Plateau[Jx][Jy] = ' '
          # repositionner le jouer
          Jx = Jx - 1
          Plateau[Jx][Jy] = '@'
          printPlateau()
      
# Regle de deplacement vers le BAS
  if action == "S":
    # Verifier si zone de ravitaillement en bombe
    if Jy == By and Jx + 1 == Bx :
      if not Bombe :
        while True:
          print('/!\ Zone de ravitaillment de bombe')
          print('Appuyez B pour recupperer, C pour annuler')
          bombeChoice = input().upper()
          if bombeChoice in ['B','C']:
            break
        if bombeChoice == 'B' :
          Bombe = True
          print('Vous avez une Bombe \o/')
    # Verifier si zone occupé par un mechant
    else :
      i = 0
      while i < len(Mechants) :
        if Mechants[i][0] == Jx + 1 and Mechants[i][1] == Jy :
          print(' Your are Dead !!!')
          # effacer lancien position du Joueur
          Plateau[Jx][Jy] = ' '  
          playerisDead = True
          return playerisDead
        else :
          i = i+1
    
    if playerisDead == False :
      # effacer lancien position du Joueur
          Plateau[Jx][Jy] = ' '
          # repositionner le joueur
          Jx= Jx + 1
          Plateau[Jx][Jy] = '@'
          printPlateau()
      
      
  return playerisDead


#######7 Fonction de strategie de Jeu Ordinateur 
def actionOrdinateur():

  return 0

#
def finJeu():
  global playerisDead
  return playerisDead

#######6 Fonction d'effet de bombe
#---------------------------------------------------------------------------------------------------------------------------
#Lancer le programme
Start()