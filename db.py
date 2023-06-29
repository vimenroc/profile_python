import mysql.connector
from mysql.connector import Error
import random
from random import *


def connectoToDB():
    try:
        conn = mysql.connector.connect(
            host="bhlxwvmh8s7krbir0jfv-mysql.services.clever-cloud.com",
            port="3306",
            user="ufhdlaicsbs8zt0n",
            password="X814lP52O4nBfgShnHeK",
            db="bhlxwvmh8s7krbir0jfv"
        )

        users = ["Richar","Eilyn","Edú","Pollo","Víctor"]
        option = randint(1,5)
        
        cursor = conn.cursor()
        currentUser = users[randint(0,len(users)-1)]
        # Rvisar que la persona no haya tenido una linea asignada en los últimos 5 minutos
        query = "SELECT * FROM lanes where user = '" + currentUser + "' AND TIMEDIFF(CURRENT_TIMESTAMP(),time_called) < '00:05:00' "
        # query = "SELECT * FROM lanes where user = 'Pollo' AND TIMEDIFF(CURRENT_TIMESTAMP(),time_called) < '00:05:00'"
        cursor.execute(query)
        records = cursor.fetchall()

        if records:
            # print ("Sí results")
            row = records[0]
            print (row[2] + " es " + row[1] + "!")
        else:
            # print ("No results")
            query = "SELECT * FROM lanes where TIMEDIFF(CURRENT_TIMESTAMP(),time_called) > '00:05:00'"
            cursor.execute(query)
            records = cursor.fetchall()
            # print (records)
            # print (len(records))
            index = len(records) - 1
            option = randint(0,index)
            row = records[option]
            query = "UPDATE lanes set time_called = CURRENT_TIMESTAMP(), user = '" + currentUser + "' where id = '" + str(row[0]) + "';"
            cursor.execute(query)
            print (currentUser + " es " + row[1] + "!")
            conn.commit()
        # query = "SELECT * FROM lanes where id = " + str(option)
        # print (option)


    except Error as ex:
        print(ex)

    finally:
        if conn.is_connected():
            conn.close()
            cursor.close()

connectoToDB()