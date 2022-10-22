import sqlite3 as sql
import os #este modulo me permite usar el comando para verificar si un archovo existe
#import random

def createDB():
    conn=sql.connect("THE_QUEST/Base_datos/ranking.db")
    conn.commit()
    conn.close()

def createTable():
    conn=sql.connect("THE_QUEST/Base_datos/ranking.db")
    cursor=conn.cursor()#nos permitira selecionar la posision del dato
    cursor.execute(
        """CREATE TABLE ranking(
            name text,
            score integer
        )"""
    )
    conn.commit()
    conn.close()


def insertRow(nombre,score):
    conn=sql.connect("THE_QUEST/Base_datos/ranking.db")
    cursor = conn.cursor()
    instruccion=f"INSERT INTO ranking VALUES ('{nombre}',{score})"  #f"" es una instruccion para un formato string
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def readOrder(field):
    conn=sql.connect("THE_QUEST/Base_datos/ranking.db")
    instruccion=f"SELECT * FROM ranking order by {field} DESC"
    cursor=conn.cursor()
    cursor.execute(instruccion)
    datos=cursor.fetchall()
    conn.commit()
    conn.close()
    return datos
#insertRow("Cam",random.randint(100,700) )
"""
datos= readOrder("score")
for i in range(len(datos)):
    print(datos[i][0])
    print(datos[i][1])
"""    


#estas dos instrucciones crearan el archivo de ranking.db
while not os.path.exists("THE_QUEST/Base_datos/ranking.db"):
    print("Empezo")
    if not os.path.exists("THE_QUEST/Base_datos/ranking.db"):
        createDB()
    if os.path.exists("THE_QUEST/Base_datos/ranking.db"):
        createTable()
        start=False
    
    