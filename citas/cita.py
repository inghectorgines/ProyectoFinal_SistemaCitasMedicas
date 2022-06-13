import sqlite3
from unittest import result
import medicos.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Cita:
    def __init__(self, medico_id,paciente="",diagnostico="",descripcion="",prox_cita=""):
        self.Medico_id = medico_id
        self.Paciente = paciente
        self.Diagnostico = diagnostico
        self.Descripcion = descripcion
        self.ProxCita = prox_cita

    def guardar(self):
        sql = "INSERT INTO citas VALUES(null,%s,%s,%s,%s,%s,NOW())"
        cita = (self.Medico_id,self.Paciente,self.Diagnostico,self.Descripcion,self.ProxCita)

        try:
            cursor.execute(sql,cita)
            database.commit()

            result = [cursor.rowcount, self]
        except:
            result = [0, self]

        return result

    def listar(self):
        sql = f"SELECT * FROM citas WHERE medico_id  = {self.Medico_id}"

        cursor.execute(sql)
        result = cursor.fetchall()

        return result

    def eliminar(self,id):
        sql = f"DELETE FROM citas WHERE id = {id}"

        try:
            cursor.execute(sql)
            database.commit()

            result = [cursor.rowcount, self]
        except:
            result = [0, self]

        return result

    def listarModificar(self, id):
        sql = f"SELECT * FROM citas WHERE id  = {id}"

        cursor.execute(sql)
        result = cursor.fetchall()

        return result

    def modificar(self,Paciente,Diagnostico,Descripcion,ProxCita,id):
        sql = f"UPDATE citas SET paciente = '{Paciente}', diagnostico = '{Diagnostico}', descripcion = '{Descripcion}', proxima_cita = '{ProxCita}' WHERE id = {id}"

        try:
            cursor.execute(sql)
            database.commit()

            result = [cursor.rowcount, self]
        except:
            result = [0, self]

        return result
