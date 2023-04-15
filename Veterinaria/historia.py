class HistoriaClinica:
    def __init__(self):
        self.historias_clinicas = {}

    def agregar_historia_clinica(self, id_mascota, fecha, medico, motivo_consulta, sintomatologia, diagnostico,
                                 procedimiento, medicamento, dosis_medicamento, id_orden, historial_vacunacion, alergias,
                                 detalle_procedimiento):
        try:
            historia = {
                fecha: {
                    "medico": medico,
                    "motivo_consulta": motivo_consulta,
                    "sintomatologia": sintomatologia,
                    "diagnostico": diagnostico,
                    "procedimiento": procedimiento,
                    "medicamento": medicamento,
                    "dosis_medicamento": dosis_medicamento,
                    "id_orden": id_orden,
                    "historial_vacunacion": historial_vacunacion,
                    "alergias": alergias,
                    "detalle_procedimiento": detalle_procedimiento
                }
            }


            if id_mascota in self.historias_clinicas:
                self.historias_clinicas[id_mascota].update(historia)
            else:
                self.historias_clinicas[id_mascota] = historia
            print("Historia clínica agregada correctamente")

        except:
            print("Error al agregar la historia clínica")


    def consultar_historia_clinica(self, id_mascota):
        try:
            if id_mascota in self.historias_clinicas:
                print("Historia clínica de la mascota con id", id_mascota)
                for fecha, registro in self.historias_clinicas[id_mascota].items():
                    print(fecha, registro)
            else:
                print("No se encontró la historia clínica de la mascota con id", id_mascota)
        except:
            print("Error al consultar la historia clínica")


    def crear_orden(id_orden):
        fecha = input("Ingrese la fecha de la orden (dd/mm/aaaa): ")
        tipo_servicio = input("Ingrese el tipo de servicio: ")
        detalle = input("Ingrese el detalle del servicio: ")
        valor_total = float(input("Ingrese el valor total: "))
        return Orden(id_orden, fecha, tipo_servicio, detalle, valor_total)