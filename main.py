## Descargo y procedo a revisar y calificar.


print("""
Acciones disponibles:
    - Registro (1)
    - Login (2)
""")

from medicos import acciones

ejecuta = acciones.Acciones()

accion = input("¿Qué quieres hacer?:")

if accion == str(1):
    ejecuta.registro()
elif accion == str(2):
    ejecuta.login()

print("\nFrancisco Manuel Federico \nDesarrollo para Dispositivos Inteligentes")
print("9° A" + "\n11 de Junio de 2022\n")
