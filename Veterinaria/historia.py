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

    