from typing import List, Dict
import mysql.connector
import json
import time
import sys


# Connects to the database and inserts the disease
def add_disease(ID, name1, provenance, critical_level, recomandation, recovery_days):
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'heart_diseases_db'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    sql = "insert into heart_diseases values (%s, %s, %s, %s, %s, %s)"
    val = (str(ID), name1, provenance, str(critical_level), recomandation, str(recovery_days))
    cursor.execute(sql, val)
    connection.commit()

    # Print the new database
    cursor.execute('SELECT * from heart_diseases')
    for x in cursor:
        print(x)

    cursor.close()
    connection.close()

# Connects to the database and deletes the disease
def remove_heart_desease(ID):
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'heart_disease_db'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    sql = "DELETE FROM heart_diseases WHERE ID = %s"
    to_delete = (ID, )  
    cursor.execute(sql, to_delete)
    connection.commit()

    # Print the new database
    cursor.execute('SELECT * from heart_diseases')
    for x in cursor:
        print(x)

    cursor.close()
    connection.close()  


if __name__ == '__main__':
    while True:
        print("Type START to begin")
        command = sys.stdin.readline().strip('\n')
        if command == "START":
            break

    while True:
        print("1.Add disease\n2.Delete desease\n")
        option = sys.stdin.readline().strip('\n')
        if option == "1":
            print("desease ID:")
            ID = int(sys.stdin.readline().strip('\n'))
            print("Insert name:")
            name1 = sys.stdin.readline().strip('\n')
            print("Provenance (eg. 'East Asia':")
            provenance = sys.stdin.readline().strip('\n')
            print("Critical level (eg. 1 for high severity, 4 for low severity):")
            critical_level = int(sys.stdin.readline().strip('\n'))
            print("Insert short recomandation:")
            recomandation = sys.stdin.readline().strip('\n')
            print("Number of days for fully recover:")
            recovery_days = int(sys.stdin.readline().strip('\n'))

            add_disease(ID, name1, provenance, critical_level, recomandation, recovery_days)
        elif option == "2":
            print("Remove disease:")
            ID = sys.stdin.readline().strip('\n')
            remove_disase(ID)
        else:
            print("Invalid option!!!")
