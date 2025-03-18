import pypyodbc as odbc
from PyQt5 import Qt

DRIVER_NAME = "SQL SERVER"
# Tutaj niech Pani wklei nazwę Servera
SERVER_NAME = "DESKTOP-28TJH0V\SQLEXPRESS01"
DATABASE_NAME = "TimeForge"


def get_tasks_for_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        print("Executing SQL query with user_id:", user_id)
        cursor.execute("""
            SELECT z.zadanie_id, z.nazwa_zadania, z.opis_zadania, z.data_zadania, z.czas_rozpoczecia, z.czas_zakonczenia,
                   k.kategoria, s.czy_zrobione
            FROM Zadania z
            JOIN kategoria_zadania_status_mapowanie m ON z.zadanie_id = m.zadanie_id
            JOIN kategorie_zadan k ON m.kategoria_id = k.kategoria_id
            JOIN Statusy_Zadania s ON m.status_id = s.status_id
            WHERE z.uzytkownik_id = ?;
        """, (user_id,))

        tasks_by_date = {}  # Dictionary to hold tasks grouped by dates

        for row in cursor.fetchall():
            print("Fetched row:", row)
            task = {
                'task_name': row[1],
                'task_description': row[2],
                'date': row[3],
                'start_time': row[4],
                'end_time': row[5],
                'category_name': row[6],
                'status': row[7]
            }

            # Group tasks by date
            date = row[3]  # Assuming the date is in the 4th column
            if date not in tasks_by_date:
                tasks_by_date[date] = []
            tasks_by_date[date].append(task)

        return tasks_by_date
    except Exception as e:
        print("Error fetching tasks:", e)
        return {}
    finally:
        cursor.close()
        conn.close()
def get_user_theme(user_id):

    conn = get_connection()  # Assuming you have a function to get the database connection
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT motyw FROM Uzytkownicy WHERE uzytkownik_id = ?", (user_id,))
        result = cursor.fetchone()
        if result:
            return result[0]  # Return the user's name
        else:
            return None  # User not found
    except Exception as e:
        print("Error fetching user's name:", e)
        return None
    finally:
        cursor.close()
        conn.close()
def save_new_theme(user_id, theme):
    conn = get_connection()  # Assuming you have a function to get the database connection
    cursor = conn.cursor()

    try:
        cursor.execute("UPDATE Uzytkownicy SET motyw = ? WHERE uzytkownik_id = ?", (theme, user_id))
        conn.commit()  # Commit the transaction to save the changes to the database
        return True  # Return True indicating successful update
    except Exception as e:
        print("Error updating user's first name:", e)
        conn.rollback()  # Rollback the transaction in case of error
        return False  # Return False indicating failure
    finally:
        cursor.close()
        conn.close()
def default_theme(user_id, theme):
    conn = get_connection()  # Assuming you have a function to get the database connection
    cursor = conn.cursor()

    try:
        cursor.execute("UPDATE Uzytkownicy SET motyw = ? WHERE uzytkownik_id = ?", (theme, user_id))
        conn.commit()  # Commit the transaction to save the changes to the database
        return True  # Return True indicating successful update
    except Exception as e:
        print("Error updating user's theme:", e)
        conn.rollback()  # Rollback the transaction in case of error
        return False  # Return False indicating failure
    finally:
        cursor.close()
        conn.close()

def save_new_password(user_id, new_password):
    conn = get_connection()  # Assuming you have a function to get the database connection
    cursor = conn.cursor()

    try:
        cursor.execute("UPDATE Uzytkownicy SET haslo_uzytkownika = ? WHERE uzytkownik_id = ?", (new_password, user_id))
        conn.commit()  # Commit the transaction to save the changes to the database
        return True  # Return True indicating successful update
    except Exception as e:
        print("Error updating user's first name:", e)
        conn.rollback()  # Rollback the transaction in case of error
        return False  # Return False indicating failure
    finally:
        cursor.close()
        conn.close()
def delete_user_from_db(uzytkownik_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        # Delete the task from the Zadania table
        cursor.execute("DELETE FROM Uzytkownicy WHERE uzytkownik_id = ?", (uzytkownik_id,))
        conn.commit()
        print(f"Uzytkownik with ID {uzytkownik_id} deleted successfully!")
    except Exception as e:
        print(f"Error deleting task with ID {uzytkownik_id}: {e}")
        raise
    finally:
        cursor.close()
        conn.close()
def save_new_last_name(user_id, new_first_name):
    conn = get_connection()  # Assuming you have a function to get the database connection
    cursor = conn.cursor()

    try:
        cursor.execute("UPDATE Uzytkownicy SET nazwisko_uzytkownika = ? WHERE uzytkownik_id = ?", (new_first_name, user_id))
        conn.commit()  # Commit the transaction to save the changes to the database
        return True  # Return True indicating successful update
    except Exception as e:
        print("Error updating user's first name:", e)
        conn.rollback()  # Rollback the transaction in case of error
        return False  # Return False indicating failure
    finally:
        cursor.close()
        conn.close()
def save_new_first_name(user_id, new_first_name):
    conn = get_connection()  # Assuming you have a function to get the database connection
    cursor = conn.cursor()

    try:
        cursor.execute("UPDATE Uzytkownicy SET imie_uzytkownika = ? WHERE uzytkownik_id = ?", (new_first_name, user_id))
        conn.commit()  # Commit the transaction to save the changes to the database
        return True  # Return True indicating successful update
    except Exception as e:
        print("Error updating user's first name:", e)
        conn.rollback()  # Rollback the transaction in case of error
        return False  # Return False indicating failure
    finally:
        cursor.close()
        conn.close()
def get_user_info_by_id(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT  login_uzytkownika, imie_uzytkownika, nazwisko_uzytkownika, haslo_uzytkownika, motyw FROM Uzytkownicy WHERE uzytkownik_id = ?
        """, (user_id,))
        user_info = cursor.fetchone()
        if user_info:
            login, first_name, last_name, password, theme = user_info
            return {'login': login, 'first_name': first_name, 'last_name': last_name, 'password': password, 'theme': theme}
        else:
            return None
    except Exception as e:
        print(f"Error getting user info: {e}")
        raise
    finally:
        cursor.close()
        conn.close()
def delete_task_from_db(task_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        # Delete the task from the Zadania table
        cursor.execute("DELETE FROM Zadania WHERE zadanie_id = ?", (task_id,))
        conn.commit()
        print(f"Task with ID {task_id} deleted successfully!")
    except Exception as e:
        print(f"Error deleting task with ID {task_id}: {e}")
        raise
    finally:
        cursor.close()
        conn.close()
def get_user_name(user_id):

    conn = get_connection()  # Assuming you have a function to get the database connection
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT imie_uzytkownika FROM Uzytkownicy WHERE uzytkownik_id = ?", (user_id,))
        result = cursor.fetchone()
        if result:
            return result[0]  # Return the user's name
        else:
            return None  # User not found
    except Exception as e:
        print("Error fetching user's name:", e)
        return None
    finally:
        cursor.close()
        conn.close()


def get_tasks_for_date(user_id, date):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        print("Executing SQL query with user_id:", user_id, "and date:", date)
        cursor.execute("""
            SELECT z.zadanie_id, z.nazwa_zadania, z.opis_zadania, z.data_zadania, z.czas_rozpoczecia, z.czas_zakonczenia,
                   k.kategoria, s.czy_zrobione
            FROM Zadania z
            JOIN kategoria_zadania_status_mapowanie m ON z.zadanie_id = m.zadanie_id
            JOIN kategorie_zadan k ON m.kategoria_id = k.kategoria_id
            JOIN Statusy_Zadania s ON m.status_id = s.status_id
            WHERE z.uzytkownik_id = ? AND CAST(z.data_zadania AS DATE) = ?;
        """, (user_id, date))
        tasks = []
        for row in cursor.fetchall():
            print("Fetched row:", row)
            task = {
                'task_name': row[1],
                'task_description': row[2],
                'date': row[3],
                'start_time': row[4],
                'end_time': row[5],
                'category_name': row[6],
                'status': row[7],
                'task_id': row[0],  # Changed index to 0 for task_id
            }
            tasks.append(task)
        return tasks
    except Exception as e:
        print("Error fetching tasks:", e)
        raise  # Raise the exception to propagate it
    finally:
        cursor.close()
        conn.close()
def get_connection():
    connection_string = f"""
        DRIVER={{{DRIVER_NAME}}};
        SERVER={SERVER_NAME};
        DATABASE={DATABASE_NAME};
        Trust_Connection=yes;
    """
    return odbc.connect(connection_string)

# User operations
def register_user(imie, login, haslo, theme):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        # Check if the login already exists in the database
        cursor.execute("SELECT * FROM Uzytkownicy WHERE login_uzytkownika = ?", (login,))
        existing_user = cursor.fetchone()
        if existing_user:
            print("User with this login already exists.")
            return False

        # If the login is unique, proceed with registration
        cursor.execute("""
            INSERT INTO Uzytkownicy (imie_uzytkownika, login_uzytkownika, haslo_uzytkownika, motyw)
            VALUES (?, ?, ?,?)
        """, (imie, login, haslo, theme))
        conn.commit()
    except Exception as e:
        print(f"Error registering user: {e}")
        raise
    finally:
        cursor.close()
        conn.close()
    return True


def validate_user(login, haslo):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        # Check if the login and password exist in the database
        cursor.execute("""
            SELECT COUNT(*)
            FROM Uzytkownicy
            WHERE login_uzytkownika = ? AND haslo_uzytkownika = ?
        """, (login, haslo))
        count = cursor.fetchone()[0]
        if count > 0:
            return True  # User is validated
        else:
            return False  # User is not validated
    except Exception as e:
        print(f"Error validating user: {e}")
        return False
    finally:
        cursor.close()
        conn.close()

def get_user_info(login):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT uzytkownik_id, login_uzytkownika, imie_uzytkownika, nazwisko_uzytkownika, haslo_uzytkownika FROM Uzytkownicy WHERE login_uzytkownika = ?
        """, (login,))
        user_info = cursor.fetchone()
        if user_info:
            user_id, login, first_name, last_name, password_hash = user_info
            return {'user_id': user_id, 'first_name': first_name, 'last_name': last_name, 'login':login, 'password_hash': password_hash}
        else:
            return None
    except Exception as e:
        print(f"Error getting user info: {e}")
        raise
    finally:
        cursor.close()
        conn.close()

def insert_task(user_id, task_name, task_description, date, start_time, end_time):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        print(f"Inserting task: {task_name}, {task_description}, {date}, {start_time}, {end_time}")
        cursor.execute("""
            INSERT INTO Zadania (uzytkownik_id, nazwa_zadania, opis_zadania, data_zadania, czas_rozpoczecia, czas_zakonczenia)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (user_id, task_name, task_description, date, start_time.toString("HH:mm:ss"), end_time.toString("HH:mm:ss")))
        conn.commit()
        print("Task inserted successfully!")
    except Exception as e:
        print(f"Error inserting task: {e}")
        raise
    finally:
        cursor.close()
        conn.close()


def get_category_id(category_name):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        query = "SELECT kategoria_id FROM kategorie_zadan WHERE kategoria = ?"
        cursor.execute(query, (category_name,))
        result = cursor.fetchone()
        cursor.close()
        if result:
            return result[0]
        else:
            return None
    except Exception as e:
        print(f"Error fetching category ID: {e}")
        return None

def get_status_id(status_name):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        query = "SELECT status_id FROM Statusy_Zadania WHERE czy_zrobione = ?"
        cursor.execute(query, (status_name,))
        result = cursor.fetchone()
        cursor.close()
        if result:
            return result[0]
        else:
            return None
    except Exception as e:
        print(f"Error fetching status ID: {e}")
        return None

def insert_task_category_status(task_id, category_id, status_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO kategoria_zadania_status_mapowanie (zadanie_id, kategoria_id, status_id)
            VALUES (?, ?, ?)
        """, (task_id, category_id, status_id))
        conn.commit()
    except Exception as e:
        print(f"Error inserting task-category-status mapping: {e}")
        raise
    finally:
        cursor.close()
        conn.close()
