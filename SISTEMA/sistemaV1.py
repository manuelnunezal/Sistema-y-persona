class Paciente:
    def __init__(self):
        self.__nombre = ""
        self.__cedula = 0
        self.__genero = ""
        self.__servicio = ""
    def verNombre(self):
        return self.__nombre
    def verCedula(self):
        return self.__cedula
    def verGenero(self):
        return self.__genero
    def verServicio(self):
        return self.__servicio
    
    def asignarNombre(self,n):
        self.__nombre = n
    def asignarCedula(self,c):
        self.__cedula = c
    def asignarGenero(self,g):
        self.__genero = g
    def asignarServicio(self,s):
        self.__servicio = s

class Sistema:
    def __init__(self):
        self.__lista_pacientes = [ ]
        self.__numero_pacientes = len(self.__lista_pacientes)
    
    def ingresarPaciente(self):
        p = Paciente()
        nombre = input("Ingrese el nombre: ")
        p.asignarNombre(nombre)

        while True:
            try:
                cedula = int(input("Ingrese la cédula: "))
                break
            except:
                print("Ingrese valores numericos")

        for patient in self.__lista_pacientes: # Se verifica si ya se encuentra registrado un paciente con la misma cedula.
            if cedula == patient.verCedula():
                print("Ya se encuentra un paciente registrado con esta cedula")
                break
            else:
                p.asignarCedula(cedula)
                

        genero = input("Ingrese el género: ")
        servicio = input("Ingrese el servicio: ")

        p = Paciente()
        p.asignarNombre(nombre)
        p.asignarCedula(cedula)
        p.asignarGenero(genero)
        p.asignarServicio(servicio)

        self.__lista_pacientes.append(p) #agrego los pacientes.
        self.__numero_pacientes = len(self.__lista_pacientes) #actualizar numero de pacientes.
    
    def verDatosPacientes(self):
        while True:
            try:
                cedula = int(input("Ingrese la cédula a buscar: "))
                break
            except:
                print("Ingrese valores numericos")
                
        for paciente in self.__lista_pacientes:
            if cedula == paciente.verCedula():
                print(f"""
    Nombre: {paciente.verNombre()}
    Cedula: {str(paciente.verCedula())}
    Genero: {paciente.verGenero()}
    Servicio: {paciente.verServicio()}
    """)
            else:
                print(f"No se ha encontrado el paciente con cedula: {cedula}")
                      
    def verNumeroPacientes(self):
        return self.__numero_pacientes
    
sistema_ = Sistema()

while True:
    opcion = int(input("""
1. Agregar paciente
2. Ver datos paciente
3. Ver numero de pacientes
4. Salir
"""))
    
    if opcion == 1:
        sistema_.ingresarPaciente()
    elif opcion == 2:
        sistema_.verDatosPacientes()
    elif opcion == 3:
        sistema_.verNumeroPacientes()
    elif opcion == 4:
        print("Fin del programa.")
        break
    else:
        print("Ingrese una opción valida.")

    




    