

class Veterinaria:
    mascotas = []
    clientes = []
    veterinarios = []
    ventas = []
    historias_clinicas = []
    ordenes = []

    
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

