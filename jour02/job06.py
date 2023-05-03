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

# Exécution de la requête pour calculer la somme des capacités des salles
cursor.execute("SELECT SUM(capacite) FROM salles")

# Récupération du résultat
total_capacite = cursor.fetchone()[0]

# Affichage du résultat en console
print(f"La capacité totale des salles est de {total_capacite}")

# Fermeture de la connexion à la base de données
cursor.close()
conn.close()