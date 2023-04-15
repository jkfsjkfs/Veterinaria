

class HistoriaClinica:
    def __init__(self):
        self.registros = {}

    def agregar_registro(self,  id_mascota, fecha, medico, motivo_consulta, sintomatologia, diagnostico, procedimiento, medicamento, dosis_medicamento, id_orden, historial_vacunacion, alergias, detalle_procedimiento):
        if id_mascota not in self.registros:
            self.registros[id_mascota] = {}

        registro = {
            "fecha": fecha,
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
            "detalle_procedimiento": detalle_procedimiento,
            "anulacion_orden": False
        }

        self.registros[id_mascota][fecha] = registro

    def anular_orden(self, id_mascota, fecha):
        if id_mascota in self.registros and fecha in self.registros[id_mascota]:
            self.registros[id_mascota][fecha]["anulacion_orden"] = True