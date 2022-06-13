import medicos.medicos as modelo
import citas.acciones

class Acciones:
    def registro(self):
        print("Registrarte como Médico...\n")

        nombre = input("¿Cuál es tu nombre?: ")
        apellidos = input("¿Cuales son tus apellido?: ")
        num_consul = input("¿Número de Consultorio?: ")
        email = input("Introduce tu email: ")
        user = input("Introduce tu Login de Usuario: ")
        password = input("Introduce tu contraseña: ")

        medico = modelo.Medicos(nombre,apellidos,num_consul,email,user,password)
        registro = medico.registrar()

        if registro[0] >= 1:
            print(f"\nPerfecto {registro[1].Nombre} te has registrado con el email {registro[1].Email} y tu Usuario es: {registro[1].User}")
        else:
            print("\nNo te has registrado correctamente!!!")

    def login(self):
        print("\nIndentificate en el sistema...")

        try:
            user = input("Introduce tu usuario: ")
            password = input("Introduce tu contraseña: ")

            medico = modelo.Medicos('','','','',user,password)
            login = medico.identificar()

            if user == login[5]:
                print(f"\nBienvenido {login[1]}, te has registrado en el sistema el {login[7]}")

                self.proximasAcciones(login)

        except Exception as e:
            print("\nLogin Incorrecto!!! Intentalo más tarde")

    def proximasAcciones(self,medico):
        print("""
        Acciones disponibles:
            - Registrar Cita (1)
            - Modificar Cita (2)
            - Mostrar Cita (3)
            - Eliminar Cita (4)
            - Salir (5)
        """)

        accion = input("¿Qué quieres hacer?: ")

        ejecuta = citas.acciones.Acciones()

        if accion == str(1):
            ejecuta.rigistrar(medico)
            self.proximasAcciones(medico)
        
        elif accion == str(2):
            ejecuta.modifica(medico)
            self.proximasAcciones(medico)

        elif accion == str(3):
            ejecuta.mostrar(medico)
            self.proximasAcciones(medico)

        elif accion == str(4):
            ejecuta.borrar(medico)
            self.proximasAcciones(medico)
            
        elif accion == "salir":
            exit() 
