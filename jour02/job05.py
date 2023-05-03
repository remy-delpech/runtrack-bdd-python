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

# Exécution de la requête pour calculer la superficie totale des étages
cursor.execute("SELECT SUM(superficie) FROM etage")

# Récupération du résultat
total_superficie = cursor.fetchone()[0]

# Affichage du résultat en console
print(f"La superficie de La Plateforme est de {total_superficie} m2")

# Fermeture de la connexion à la base de données
cursor.close()
conn.close()