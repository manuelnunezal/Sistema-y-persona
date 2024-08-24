class Paciente:
    def __init__(self):
        self.__nombre = ""
        self.__cedula = 0
        self.__genero = ""
        self.__servicio = "" 
    
    def verNombre(self):
        return self.__nombre
    def verServicio(self):
        return self.__servicio
    def verCedula(self):
        return self.__cedula
    def verGenero(self):
        return self.__genero
    
    def asignarNombre(self,n):
        self.__nombre = n 
    def asignarServicio(self,s):
        self.__servicio = s 
    def asignarCedula(self,c):
        self.__cedula = c
    def asignarGenero(self,g):
        self.__genero = g
    def __str__(self):
        return f"""
Nombre: {self.__nombre}
Cédula: {self.__cedula}
Género: {self.__genero}
Servicio: {self.__servicio}
"""
class Sistema:
    def __init__(self):
        self.__lista_pacientes = []
    def verificarPaciente(self,c):
        encontrado = False
        for p in self.__lista_pacientes:
            if c == p.verCedula():
                encontrado = True
                break
        return encontrado
    
    def ingresarPaciente(self,pac):
        if self.verificarPaciente(pac.verCedula()):
            return False # SI NO LO VERIFICA RETORNA FALSE
        self.__lista_pacientes.append(pac)
        return True  
    
    def verDatosPaciente(self,c):
        if self.verificarPaciente(c) == False:
            return None
        for p in self.__lista_pacientes:
            if c == p.verCedula():
                return p
            
    def verNumeroPacientes(self):
        return f"Hay {len(self.__lista_pacientes)} paciente(s) en el sistema" 
    
def main():
    sis = Sistema()
    
    while True:
        opcion = int(input("""
1. Ingresar paciente.
2. Ver Paciente.
3. Ver numero pacientes.
4. salir."""))
        
        if opcion == 1:
            print("Se solicitaran los datos...")
            
            nombre = input("Ingrese el nombre: ")
            while True:
                try:
                    cedula = int(input("Ingrese la cedula: "))
                    break
                except:
                    print("Ingrese solo valores númericos.")
            genero = input("Ingrese el genero: ")
            servicio = input("Ingrese el servicio: ")
            
            pac = Paciente()
            pac.asignarNombre(nombre)
            pac.asignarCedula(cedula)
            pac.asignarGenero(genero)
            pac.asignarServicio(servicio)
            
            resultado = sis.ingresarPaciente(pac)
            
            if resultado == False:
                print("Ya existe un paciente con esa cedula")
            else:
                print("Paciente ingresado")
        
        elif opcion == 2:
            
            while True:
                try:
                    c = int(input("Ingrese la cedula a buscar: "))
                    break
                except:
                    print("Ingrese valores númericos.")
            
            dp = sis.verDatosPaciente(c)
            
            
            print(dp)
            
            
            
        elif opcion == 3:
            np = sis.verNumeroPacientes()
            print(np)
            
        elif opcion != 4:
            continue
        
        else:
            break
        

main()
