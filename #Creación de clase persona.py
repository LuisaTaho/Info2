#Creación de clase persona (Padre)
class Persona:
    #Creación de atributos de instancia
    def __init__(self,nombre,edad,género):
        self.nombre=nombre
        self.edad=edad
        self.género=género
    #Creación de métodos de instancia
    def informacionPersonal(self):
        return f"Nombre:{self.nombre}\nEdad:{self.edad}\nGénero:{self.género}"
#Creación de objeto
p1=Persona('Luisa',19,'femenino')
#Prueba de escritorio 
p1.informacionPersonal()
#Creación de clase Paciente (Hija)
class Paciente(Persona):
    #Creación de atributos de instancia
    def __init__(self,nombre,edad,género,historiaClinica):
        super().__init__(nombre, edad, género)
        self.historiaClinica = historiaClinica
        #Relación de dependencia con la clase hospital
        Hospital.agregarPaciente(self)

    def informacionPersonal(self):
         return f"Nombre:{self.nombre}\nEdad:{self.edad}\nGénero:{self.género}\n{self.historiaClinica}"
    


#Creación de clase Doctor
class Doctor(Persona):
    #Creación de atributos de instancia
    def __init__(self, nombre, edad, género,especialidad):
        super().__init__(nombre, edad, género)
        self.especialidad=especialidad
    def informacionPersonal(self):
        return f"Nombre:{self.nombre}\nEdad:{self.edad}\nGénero:{self.género}\n{self.especialidad}"



#Creación de clase consulta médica (hija)
class ConsultaMedica:
    #Creación de atributos de instancia
    def __init__(self,doctor,paciente,fecha):
        self.doctor=doctor
        self.paciente=paciente
        self.fecha=fecha
    #Creación de métodos de instancia
    def informacionConsulta(self):
        return f"Fecha:{self.fecha}\nDoctor:\n{self.doctor.informacionPersonal()}"


#Creación de clase hospital  
class Hospital:
    #Creación de atributo de clase
    totalPacientes=0
    pacientes=[]
    #Creación de atributos de instancia
    def __init__(self,nombreHospital,ubicacion):
        self.nombreHospital=nombreHospital
        self.ubicacion=ubicacion
    #Creación de métodos de clase
    @classmethod
    def agregarPaciente(cls,paciente):
        cls.pacientes.append(paciente)
        cls.totalPacientes +=1

    @classmethod
    def totalGeneral(cls):
        return cls.totalPacientes


#Prueba de escritorio Paciente
pc1=Paciente('Luisa',19,'femenino',2658)
pc1.informacionPersonal()
#print(pc1.informacionPersonal())

#Creación de objeto
d1=Doctor('Luisito', 100, 'masculino', 'cardiología')
#Prueba de escritorio Doctor
d1.informacionPersonal()
#print(d1.informacionPersonal())

#Creación de objeto
c1=ConsultaMedica(d1,p1,'19 de abril')
c1.informacionConsulta()
#print(c1.informacionConsulta())  

#Prueba de escritorio Hospital
hospital=Hospital('Uno','Aquí')
print(hospital.totalGeneral())

        