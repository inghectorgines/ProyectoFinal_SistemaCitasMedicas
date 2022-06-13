import datetime
import hashlib
from sqlite3 import connect
import medicos.conexion as conexion
from unittest import result # Cifrar contraseña

# Llamar la clase Conectar
connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Medicos:
    def __init__(self, nombre, apellidos, num_consultorio, email, user, password):
        self.Nombre = nombre
        self.Apellidos = apellidos
        self.Num_Consultorio = num_consultorio
        self.Email = email
        self.User = user
        self.Password = password

    def registrar(self):
        fecha = datetime.datetime.now()

        # Cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.Password.encode('utf8'))

        sql = "INSERT INTO medicos VALUES (null, %s,%s,%s,%s,%s,%s,%s)"
        medico = (self.Nombre,self.Apellidos,self.Num_Consultorio,self.Email,self.User,cifrado.hexdigest(),fecha)

        try:
            cursor.execute(sql,medico)
            database.commit()

            result = [cursor.rowcount, self]
        except:
            result = [0, self]


        return result

    def identificar(self):
        # Login de medicos
        sql = "SELECT * FROM medicos WHERE user = %s AND pass = %s"

        # Cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.Password.encode('utf8'))

        # Datos para la consulta
        medico = (self.User, cifrado.hexdigest())

        cursor.execute(sql,medico)
        result = cursor.fetchone()

        return result
