from historia import HistoriaClinica
from orden import Orden

from mascotas import Perro, Gato, Pez, Ave
from personas import Cliente, Veterinario


class Veterinaria:
    mascotas = []
    clientes = []
    veterinarios = []
    administradores = []
    vendedores = []
    ventas = []
    historias_clinicas = HistoriaClinica()
    ordenes = []
    usuario = None
    
    def generaId(self, tabla):
        siguiente_id  = 1
        try:
            if tabla == "mascotas":
                siguiente_id = max([mascota.Id for mascota in self.mascotas]) + 1

            elif tabla == "ventas":
                siguiente_id = max([venta.Id for venta in self.ventas]) + 1
        
            elif tabla == "ordenes":
                siguiente_id = max([orden.Id for orden in self.ordenes]) + 1
        except:
            siguiente_id = 1

        return siguiente_id 

    def __init__(self):
        self.llenar_valores_por_defecto()


    def llenar_valores_por_defecto(self):
        # Llenar lista de clientes
        cliente1 = Cliente(1111111111, 'Juan Perez', 30)
        cliente2 = Cliente(2222222222, 'Maria Gomez', 45)
        cliente3 = Cliente(3333333333, 'Pedro Torres', 20)
        self.clientes = [cliente1, cliente2, cliente3]

        # Llenar lista de veterinarios
        veterinario1 = Veterinario(4444444444, 'Laura Hernandez', 28,  '123456')
        veterinario2 = Veterinario(5555555555, 'Carlos Rodriguez', 40, 'qwerty')
        self.veterinarios = [veterinario1, veterinario2]

        # Llenar lista de mascotas
        self.mascotas.append(Perro(self.generaId('mascotas'), 'Fido', 1111111111, 2, 'Labrador', 'Juega mucho', 10))
        self.mascotas.append(Perro(self.generaId('mascotas'), 'Rocky', 1111111111, 4, 'Bulldog', 'Muy fiel', 20))
        self.mascotas.append(Gato(self.generaId('mascotas'), 'Mishu', 2222222222, 5, 'Siames', 'Le gusta dormir', 3))
        self.mascotas.append(Gato(self.generaId('mascotas'), 'Pelusa', 3333333333, 1, 'Persa', 'Muy cariñoso', 2))
        self.mascotas.append(Ave(self.generaId('mascotas'), 'Loro', 2222222222, 3, 'Ara', 'Habla mucho', 0.5))
        self.mascotas.append(Pez(self.generaId('mascotas'), 'Nemo', 3333333333, 1, 'Payaso', 'Le gusta esconderse', 0.1))
        
          
        # Llenar lista de historias clínicas
        self.historias_clinicas.agregar_historia_clinica(self.generaId('historias'), 1, '2022-01-01', 'Dr. Juan Pérez', 'Dolor abdominal', 'Vómito, diarrea', 'Gastroenteritis', 'Suero, dieta blanda', 'Cada 12 horas', 1, 'Vacunación al día', '', '')
        self.historias_clinicas.agregar_historia_clinica(self.generaId('historias'), 2, '2022-02-15', 'Dra. Laura Hernández', 'Fiebre y tos', 'Secreción nasal, tos', 'Bronquitis', 'Antibiótico, jarabe', 'Cada 8 horas', 2, 'Faltan vacunas', 'Ninguna', '')
        self.historias_clinicas.agregar_historia_clinica(self.generaId('historias'), 3, '2022-03-20', 'Dr. Carlos Rodríguez', 'Dolor en las patas', 'Cojera, llanto', 'Fractura en la pata', 'Inmovilización, vendaje', 'Cada 24 horas', 3, 'Vacunación al día', '', 'Reposo absoluto')
        self.historias_clinicas.agregar_historia_clinica(self.generaId('historias'), 4, '2022-04-05', 'Dr. Juan Pérez', 'Herida en la pata', 'Sangrado, cojera', 'Herida infectada', 'Limpieza, sutura', 'Cada 12 horas', 4, 'Faltan vacunas', 'Ninguna', '')
        self.historias_clinicas.agregar_historia_clinica(self.generaId('historias'), 5, '2022-05-10', 'Dra. Laura Hernández', 'Problemas de piel', 'Picazón, enrojecimiento', 'Dermatitis', 'Baño con champú especial', 'Cada 24 horas', 5, 'Vacunación al día', 'Alergia a ciertos alimentos', '')


        self.ordenes.append(Orden(1, 1, 1111111111, 4444444444, "Ibuprofeno", "1 comprimido cada 12 horas", "2022-03-01"))
        self.ordenes.append(Orden(2, 2, 1111111111, 5555555555, "Paracetamol", "1 comprimido cada 8 horas", "2022-03-02"))
        self.ordenes.append(Orden(3, 3, 2222222222, 4444444444, "Amoxicilina", "1 comprimido cada 24 horas", "2022-03-03"))
        self.ordenes.append(Orden(4, 4, 3333333333, 5555555555, "Prednisona", "1 comprimido cada 12 horas", "2022-03-04"))
        self.ordenes.append(Orden(5, 5, 2222222222, 4444444444, "Metronidazol", "1 comprimido cada 24 horas", "2022-03-05"))


        