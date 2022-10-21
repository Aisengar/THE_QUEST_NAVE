import sqlite3 as sql
import os #este modulo me permite usar el comando para verificar si un archovo existe

#crea elfichero de sqlite
def createDB():
    conn=sql.connect("THE_QUEST/Base_datos/ranking.db")
    conn.commit()
    conn.close()
#createDB()

#Define los valores dentro del sql
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
#createTable()

# inserta los valores dentro de la lista en sql
def insertRow(nombre,score):
    conn=sql.connect("THE_QUEST/Base_datos/ranking.db")
    cursor = conn.cursor()
    instruccion=f"INSERT INTO ranking VALUES (‘{nombre}‘,{score})"  #f"" es una instruccion para un formato string
    cursor.execute(instruccion)
    conn.comit()
    conn.close()

#lee todos los datos dentro de la lista de sql en orden desendente de mayor a menor
def readOrdered(field):
    conn=sql.connect("THE_QUEST/Base_datos/ranking.db")
    cursor = conn.cursor()
    instruccion=f"SELECT * FROM ranking ORDER BY {field} DESC)"  #f"" es una instruccion para un formato string
    cursor.execute(instruccion)
    datos=cursor.fetchall()#almasena todos los datos de forma automatica
    conn.comit()
    conn.close()


#estas dos instrucciones crearan el archivo de ranking.db
while not os.path.exists("THE_QUEST/Base_datos/ranking.db"):
    print("Empezo")
    if not os.path.exists("THE_QUEST/Base_datos/ranking.db"):
        createDB()
    if os.path.exists("THE_QUEST/Base_datos/ranking.db"):
        createTable()
        start=False
    
    