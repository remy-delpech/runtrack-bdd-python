import mysql.connector

class EmployeeManager:
    def __init__(self, db_config):
        self.db_config = db_config

    def _connect(self):
        return mysql.connector.connect(**self.db_config)

    def get_employees_and_services(self):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT e.id, e.nom, e.prenom, e.salaire, s.nom as service
            FROM employes e
            JOIN services s ON e.id_service = s.id
        """)
        employees_and_services = cursor.fetchall()
        cursor.close()
        conn.close()
        return employees_and_services

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "Unknow!",
    "database": "nom_de_la_base_de_donnees"
}

employee_manager = EmployeeManager(db_config)

# Récupérer tous les employés et leur service respectif
employees_and_services = employee_manager.get_employees_and_services()

print("Employés et leur service respectif :")
for employee_and_service in employees_and_services:
    print(employee_and_service)

class EmployeeManager:
    # ...

    def create_employee(self, nom, prenom, salaire, id_service):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO employes (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)", (nom, prenom, salaire, id_service))
        conn.commit()
        cursor.close()
        conn.close()

    def get_employee(self, id):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM employes WHERE id = %s", (id,))
        employee = cursor.fetchone()
        cursor.close()
        conn.close()
        return employee

    def update_employee(self, id, nom=None, prenom=None, salaire=None, id_service=None):
        conn = self._connect()
        cursor = conn.cursor()

        updates = []
        params = []

        if nom is not None:
            updates.append("nom = %s")
            params.append(nom)
        if prenom is not None:
            updates.append("prenom = %s")
            params.append(prenom)
        if salaire is not None:
            updates.append("salaire = %s")
            params.append(salaire)
        if id_service is not None:
            updates.append("id_service = %s")
            params.append(id_service)

        updates_str = ', '.join(updates)
        params.append(id)

        cursor.execute(f"UPDATE employes SET {updates_str} WHERE id = %s", params)
        conn.commit()
        cursor.close()
        conn.close()

    def delete_employee(self, id):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM employes WHERE id = %s", (id,))
        conn.commit()
        cursor.close()
        conn.close()

    def list_employees(self):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM employes")
        employees = cursor.fetchall()
        cursor.close()
        conn.close()
        return employees
    
employee_manager = EmployeeManager(db_config)

# Créer un nouvel employé
employee_manager.create_employee("Doe", "John", 3200, 1)

# Récupérer un employé par ID
employee = employee_manager.get_employee(1)
print(employee)

# Mettre à jour un employé
employee_manager.update_employee(1, salaire=3500)

# Supprimer un employé
employee_manager.delete_employee(1)

# Lister tous les employés
employees = employee_manager.list_employees()
for employee in employees:
    print(employee)