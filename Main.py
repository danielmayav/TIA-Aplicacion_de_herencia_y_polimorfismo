from clases import *

# SE INSTANCIA LA CLASE PERSONA DESDE UN ARCHIVO CSV
# Persona.instatiate_from_csv()   

administrativo1 = Emp_administrativo("Carlos", "Sanchez", "4335734", "soltero", 1998, "gerencia")
administrativo2 = Emp_administrativo("Pacho", "Carvajal", "9878342", "casado", 2005, "legal")
administrativo3 = Emp_administrativo("Luis", "Montoya", "5099934", "soltero", 1989, "comunicaciones")

estudiante1 = Estudiante("Pedro", "Londoño", "2342095", "casado", "Matematicas")
estudiante2 = Estudiante("Julia", "Sanchez", "7872342", "soltero", "Quimica")
estudiante3 = Estudiante("Ana", "Ruiz", "6666232", "soltero", "Artes")


print(Persona.all)