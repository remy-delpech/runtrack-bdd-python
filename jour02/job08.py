import mysql.connector
from datetime import datetime

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "Unknow!",
    "database": "zoo"
}

conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

def ajouter_cage(superficie, capacite_max):
    cursor.execute("INSERT INTO cage (superficie, capacite_max) VALUES (%s, %s)", (superficie, capacite_max))
    conn.commit()

def supprimer_cage(id):
    cursor.execute("DELETE FROM cage WHERE id = %s", (id,))
    conn.commit()

def modifier_cage(id, superficie=None, capacite_max=None):
    updates = []
    params = []

    if superficie is not None:
        updates.append("superficie = %s")
        params.append(superficie)
    if capacite_max is not None:
        updates.append("capacite_max = %s")
        params.append(capacite_max)

    updates_str = ', '.join(updates)
    params.append(id)

    cursor.execute(f"UPDATE cage SET {updates_str} WHERE id = %s", params)
    conn.commit()

def ajouter_animal(nom, race, id_cage, date_naissance, pays_origine):
    cursor.execute("INSERT INTO animal (nom, race, id_cage, date_naissance, pays_origine) VALUES (%s, %s, %s, %s, %s)", (nom, race, id_cage, date_naissance, pays_origine))
    conn.commit()

def supprimer_animal(id):
    cursor.execute("DELETE FROM animal WHERE id = %s", (id,))
    conn.commit()

def modifier_animal(id, nom=None, race=None, id_cage=None, date_naissance=None, pays_origine=None):
    updates = []
    params = []

    if nom is not None:
        updates.append("nom = %s")
        params.append(nom)
    if race is not None:
        updates.append("race = %s")
        params.append(race)
    if id_cage is not None:
        updates.append("id_cage = %s")
        params.append(id_cage)
    if date_naissance is not None:
        updates.append("date_naissance = %s")
        params.append(date_naissance)
    if pays_origine is not None:
        updates.append("pays_origine = %s")
        params.append(pays_origine)

    updates_str = ', '.join(updates)
    params.append(id)

    cursor.execute(f"UPDATE animal SET {updates_str} WHERE id = %s", params)
    conn.commit()

def afficher_animaux():
    cursor.execute("SELECT * FROM animal")
    animaux = cursor.fetchall()
    print("Animaux dans le zoo:")
    for animal in animaux:
        print(animal)

def afficher_animaux_par_cage():
    cursor.execute("""
    SELECT cage.id, animal.id, animal.nom, animal.race
    FROM cage
    LEFT JOIN animal ON cage.id = animal.id_cage
    ORDER BY cage.id
    """)
    animaux_par_cage = cursor.fetchall()
    print("Animaux par cage:")
    for animal in animaux_par_cage:
        print(animal)

def calculer_superficie_totale_cages():
    cursor.execute("SELECT SUM(superficie) FROM cage")
    superficie_totale = cursor.fetchone()[0]
    print(f"La superficie totale de toutes les cages est de {superficie_totale} m2")

# Exemple d'utilisation des fonctions
ajouter_cage(100, 5)
ajouter_animal("Lion", "Panthera leo", 1, datetime(2010, 6, 15), "Afrique")
afficher_animaux()
afficher_animaux_par_cage()
calculer_superficie_totale_cages()

# N'oubliez pas de fermer la connexion à la base de données
cursor.close()
conn.close()