import mysql.connector

# Remplacez ces valeurs par les informations de connexion à votre base de données
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "Unknow!",
    "database": "LaPlateforme"
}

# Connexion à la base de données
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Exécution de la requête pour récupérer les noms et les capacités des salles
cursor.execute("SELECT nom, capacite FROM salles")

# Récupération des résultats et affichage en console
for nom, capacite in cursor:
    print(f"Nom: {nom}, Capacité: {capacite}")

# Fermeture de la connexion à la base de données
cursor.close()
conn.close()