import mysql.connector

# Remplacez les valeurs ci-dessous par les informations de connexion de votre base de données
config = {
  'user': 'root',
  'password': 'Unknow',
  'host': 'localhost',
  'database': 'LaPlateforme',
  'raise_on_warnings': True
}

# Se connecter à la base de données
cnx = mysql.connector.connect(**config)

# Créer un curseur pour exécuter des requêtes SQL
cursor = cnx.cursor()

# Exécuter la requête SQL pour récupérer tous les étudiants
query = "SELECT * FROM etudiants;"
cursor.execute(query)

# Afficher le résultat de la requête en console
print("Liste des étudiants :")
for (id, nom, prenom, age, email) in cursor:
    print(f"{id}: {prenom} {nom} - {age} ans - {email}")

# Fermer le curseur et la connexion
cursor.close()
cnx.close()