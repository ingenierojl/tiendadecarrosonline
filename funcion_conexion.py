import mysql.connector


def conexion():
    connection = mysql.connector.connect(host='localhost',
                                             database='empresay',
                                             user='root',
                                             password='')
    print("funcion conexion")
    return connection
    