import sys
import getopt
import scaffolder
import mysql.connector
from mysql.connector import Error

version = "0.9.0a"
hostName = ""
databaseName = ""
userName = ""
password = ""
destDirectory = ""
tableName = ""
tableList = []


# Funzione per la connessione al DB
def Mysql_Connect(hn, un, pw, dn): 
    connection = None
    try:
        connection = mysql.connector.connect(
            host=hn, 
            user=un, 
            password=pw,
            database=dn 
        )
        if connection.is_connected():
            db_info = connection.get_server_info()
            print("Connected to MySQL Server version: ", db_info)
    except Error as e:
        print("Unable to connect to the DB: ", e)

    return connection

# Funzione per la disconnessione dal DB
def Mysql_Disconnect(connection):
    connection.close()
    print("The MySQL Connection has been closed");
    connection = None
    return connection

# Funzione per ottenere la lista delle tabelle
def List_Tables(connection, destDirectory, tableName):
    global tableList
    cursor = connection.cursor()
    cursor.execute("SHOW TABLES;")
    tl = cursor.fetchall()
    cursor.close()
    if tableName=="":
        for (e,) in tl:
            tableList.append(scaffolder.Scaffolder(connection, e, destDirectory))
    else:
        tableList.append(scaffolder.Scaffolder(connection, tableName, destDirectory))

# Funzione dedicata alla spiegazione della linea di comando
def Show_Info():
    print("Slim Generator: Scaffolding software for Slim Framework projects and MySQL database, version: ", version)
    print("Command format:");
    print("python slimgenerator.py -h hostname -d databasename -u username -p password -o destination_path [-t tablename]")

# Funzione per l'input dei dati
def Input_args():
    global hostName
    global databaseName
    global userName
    global password
    global destDirectory
    global tableName

    if len(sys.argv) == 1:
        Show_Info()
        return 0
    else:
        #Elabora la linea di comando
        opts,args = getopt.getopt(sys.argv[1:],"h:d:u:p:o:t:")
        for opt,arg in opts:
            if opt=='-h':
                hostName = arg
            elif opt=="-d":
                databaseName = arg
            elif opt=="-u":
                userName = arg
            elif opt=="-p":
                password = arg
            elif opt=="-o":
                destDirectory = arg
            elif opt=="-t":
                tableName = arg
        return 1


# Corpo principale del programma
if Input_args()==1:
    connection = Mysql_Connect(hostName,userName,password,databaseName)
    List_Tables(connection, destDirectory, tableName)
    for e in tableList:
        e.generate()
    Mysql_Disconnect(connection)




