import mysql.connector
from mysql.connector import Error
import random
from random import *


print ("hello")


def ConnectoToDB():
    try:
        conn = mysql.connector.connect(
            host="bhlxwvmh8s7krbir0jfv-mysql.services.clever-cloud.com",
            port="3306",
            user="ufhdlaicsbs8zt0n",
            password="X814lP52O4nBfgShnHeK",
            db="bhlxwvmh8s7krbir0jfv"
        )
    except Error as ex:
        print(ex)
    return conn

def CloseConnection(conn):
    if conn.is_connected():
        conn.close()
        # cursor.close()

conn = ConnectoToDB()
CloseConnection(conn)