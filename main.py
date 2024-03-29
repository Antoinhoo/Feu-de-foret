#Importation des modules 
import pandas as pd
import mysql.connector
from mysql.connector import Error

#Chargement des données

    #localisation du fichier à charger dans la base de données
Raisin = pd.read_excel(r'C:\Users\LAB-MND\Desktop\TP_Antoine\TP\Feu_de_Foret.xlsx') 
print(Raisin.columns) #présentation du résultat



# Chargement du dataframe dans MYSQL

        #connexion à la base de données MySQL
try:
    connexion = mysql.connector.connect(host='localhost',  #Le serveur qui est local
                                       database='feu_de_foret',  #le nom de la base de données 
                                       user='root',   #le nom d'utilisateur 
                                       password='') #le mot de passe pour se connecter au serveur. Ici, le mot de passe est vide
  
  #verification de la connexion à la base de données pour son utilisation 
    if connexion.is_connected():
        print('Connexion à MySQL réussie')
 # Code à exécuter si une exception se produit
except Error as e:
    print(f"Erreur lors de la connexion à MySQL: {e}") #présentation du résultat de la connexion

#si la connexion est bien établi, les lignes suivantes seront éexécutées pour charger les données dans la base de données mySQL
try:
    cursor = connexion.cursor() #cette ligne permet de créer un curseur pour interagir avec une base de données

    for i,row in Raisin.iterrows(): #pour i lignes dans la base de données Raisin, ajouter les éléments suivants dans la table raisin_gains.
        sql = """INSERT INTO données(X, Y, Mois, Jour, FFMC, DMC, DC, ISI, Temp, RH, Vent, Pluie, Zone) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        #print(sql)
        cursor.execute(sql, tuple(row)) #cette ligne de code permet d'exécuter la requête SQL précédente à l’aide d’un curseur dans une base de données. Le curseur est un objet qui permet d’exécuter la commandes SQL et de récupérer les résultats.
#execute(sql, tuple(row)): Cette méthode exécute la requête SQL stockée dans la variable sql en utilisant les valeurs contenues dans le tuple row. Le tuple row doit contenir les valeurs appropriées pour les paramètres de la requête

    connexion.commit() #cette ligne permet de valider les modifications ou ajouts apportées à une base de données après la transaction
    connexion.close() #cette ligne permet de fermer la connexion à la base de données. Cela libère les ressources et met fin à la session de travail avec la base de données.
    print("DataFrame chargé dans MySQL avec succès!")
   
    # Code à exécuter si une exception se produit
except Exception as e: #Lorsqu'une exception (erreur) se produit, le code sur cette ligne except est s'exécute pour gérer cette exception
    print(f"Erreur lors du chargement du DataFrame dans MySQL: {e}")
