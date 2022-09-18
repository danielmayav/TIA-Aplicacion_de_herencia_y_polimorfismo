import csv

class Persona:
    all = []
    def __init__(self, nombre, apellido, id, estd_civil):
        self.nombre = nombre
        self.apellido = apellido
        self.id = id
        self.estd_civil = estd_civil
        
        Persona.all.append(self)
    
    
    
    @classmethod
    def instatiate_from_csv(cls):
        with open('bd.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Persona(
                nombre = item.get('nombre'),
                apellido = item.get('apellido'),
                id = item.get('id'),
                estd_civil= item.get('estd_civil')
            )
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.nombre}', '{self.apellido}', '{self.id}', '{self.estd_civil}')"
    

class Estudiante(Persona):
   
    def __init__(self, nombre, apellido, id, estd_civil, curso):
        super().__init__(
            nombre, apellido, id, estd_civil
        )
        
        self.curso = curso

class Empleado(Persona):
   
    def __init__(self, nombre, apellido, id, estd_civil, ano_inco):
        super().__init__(
            nombre, apellido, id, estd_civil
        )
        
        self.ano_inco = ano_inco
        
class Emp_administrativo(Empleado):
    def __init__(self, nombre, apellido, id, estd_civil, ano_inco, dependencia):
        super().__init__(
            nombre, apellido, id, estd_civil, ano_inco
            )
        self.dependencia = dependencia
        
class Emp_profe(Empleado):
    def __init__(self, nombre, apellido, id, estd_civil, ano_inco, facultad):
        super().__init__(
            nombre, apellido, id, estd_civil, ano_inco
            )
        self.facultad = facultad

class Emp_servi(Empleado):
    def __init__(self, nombre, apellido, id, estd_civil, ano_inco, labor):
        super().__init__(
            nombre, apellido, id, estd_civil, ano_inco
            )
        self.labor = labor

      