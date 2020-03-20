print("Hola paciente te vamos a tomar los datos personales para tu ingreso.")

edad = input("Digite su edad: ");
rango = 0
nombreRango = ""

try:
    edad = int(edad)
except:
    print("Parece que la edad digitada no tiene un valor valido")

nombre = input("Digite su nombre: ")

direccion = input("Digite su direccion: ")

telefono = input("Digite su telefono: ")

if edad < 18:
    nombreRango = "Menor de Edad"
    rango = 1
elif edad >= 18 and edad < 60:
    nombreRango = "Adulto"
    rango = 2
elif edad >= 60:
    nombreRango = "Miembro de la tercera edad"
    rango = 3

def alerta(ran):
    if ran == 1:
        print("Usted puede irse para su casa y estar bajo observacion, \nPor favor conserve la calma. \nSI PRESENTA COMPLICACIONES POR FAVOR VOLVER DE INMEDIATO")
    if ran == 2:
        print("Usted puede pasar a obserbacion por unas horas, \nSi no presenta sintomas puede regresar a su hojar.\nSI PRESENTA COMPLICACIONES POR FAVOR VOLVER DE INMEDIATO")
    if ran == 3:
        v = "ALERTA "
        print(v*5)
        print(v*5)      
        print("-"*20) 
        print("Usted sera transmitido a una de nuestras salas de urgencias. \nLos examenes se realizaran en unos momentos \n SU SALUD ES NUESTRA PRIORIDAD")
        print("-"*20) 
        print(v*5)
        print(v*5)

alerta(rango)
        



