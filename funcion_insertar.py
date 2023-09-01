from funcion_conexion import *

def insertar_variables_registro(fn,ap,em,pas):
    print("ESTAMOS EN LA FUNCION INSERTAR RGISTRO USUARIOS")               
    try:
        connection=conexion()
        if (connection):
            print("conexion realizada")            
        cursor=connection.cursor()
        query="""INSERT INTO `usuarios` (`Nombre`, `Apellido`, `Email`, `Password`) 
                 VALUES (%s, %s, %s, %s)"""
        variables=(fn,ap,em,pas)
        cursor.execute(query,variables)
        connection.commit()
        print("re ha realiado la insercion")
        return("la insercion se ha realizado señor usuario")
    except mysql.connector.Error:

        print("ALGO HA FALLADO")
    


