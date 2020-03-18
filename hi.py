dias_semana = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]

for d in dias_semana:
    print(d)


def month(self):
    
    if self == 1:
        return "Enero"
    if self == 2:
        return "Febrero"
    if self == 3:
        return "Marzo"
    if self == 4:
        return "Abril"
    if self == 5:
        return "Mayo"
    
    return str(self)

meses = range(1,13)

for m in meses:
    print(month(m))



