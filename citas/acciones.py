from statistics import mode
import citas.cita as modelo

class Acciones:
    def rigistrar(self, usuario):
        print(f"Doctor: {usuario[1]} !! Procedemos a registrar Cita...")

        paciente = input("Introduce nombre del paciente: ")
        diagnostico = input("Introdude el diagnostico: ")
        descripcion = input("Describa el diagnostico: ")
        prox = input("Proxima cita: ")

        cita = modelo.Cita(usuario[0],paciente,diagnostico,descripcion,prox)
        guardar = cita.guardar()

        if guardar[0] >= 1:
            print(f"\nCita registrada al paciente: {cita.Paciente}")
        else:
            print(f"\nError al registrar Cita!!! {usuario[1]}")

    def mostrar(self,usuario):
        cita = modelo.Cita(usuario[0])
        citas =  cita.listar()
        print(f"\nDr. {usuario[1]}!! Lista de sus Pacientes: \n")

        for cita in citas:
            print(f"Folio Cita: {cita[0]}")
            print(f"Paciente: {cita[2]}")
            print(f"Diagnostico: {cita[3]}")
            print(f"Descripción: {cita[4]}")
            print(f"Prox. Cita: {cita[5]}")
            print("***************************")

            
    def borrar(self, usuario):
        id = input("Introduce el folio a eliminar: ")
        print(f"\nDr. {usuario[1]}, Se procede a eliminar la Cita con Folio: {id}")

        cita = modelo.Cita(usuario[0])
        elimina = cita.eliminar(id)

        if elimina[0] >= 1:
            print(f"\nSe eliminio la cita correctamente!!!")
        else:
            print("No se borro la nota, prueba más tarde...")


    def mostrarCita(self,usuario,id):
        cita = modelo.Cita(usuario[0])
        citas =  cita.listarModificar(id)
        print("\nDatos anteriores: \n")

        for cita in citas:
            print(f"Folio Cita: {cita[0]}")
            print(f"Paciente: {cita[2]}")
            print(f"Diagnostico: {cita[3]}")
            print(f"Descripción: {cita[4]}")
            print(f"Prox. Cita: {cita[5]}")


    def modifica(self,usuario):
        id = input("\nIntroduce el folio de la cita a modificar: ")

        self.mostrarCita(usuario,id)

        print("\nDatos nuevos: \n")

        paciente = input("Introduce nombre del paciente: ")
        diagnostico = input("Introdude el diagnostico: ")
        descripcion = input("Describa el diagnostico: ")
        prox = input("Proxima cita: ")

        cita = modelo.Cita(usuario[0])
        modificar = cita.modificar(paciente,diagnostico,descripcion,prox,id)

        if modificar[0] >= 1:
            print(f"\nLa Cita se actualizo correctamente!!!")
        else:
            print("No se pudo actualizar, prueba más tarde...")



