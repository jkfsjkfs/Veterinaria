
class HistoriaClinica:
    def __init__(self, id_mascota, fecha, medico, motivo_consulta, sintomatologia, diagnostico, procedimiento, medicamento, dosis_medicamento, id_orden, historial_vacunacion, alergias, detalle_procedimiento):
        self.id_mascota = id_mascota
        self.fecha = fecha
        self.medico = medico
        self.motivo_consulta = motivo_consulta
        self.sintomatologia = sintomatologia
        self.diagnostico = diagnostico
        self.procedimiento = procedimiento
        self.medicamento = medicamento
        self.dosis_medicamento = dosis_medicamento
        self.id_orden = id_orden
        self.historial_vacunacion = historial_vacunacion
        self.alergias = alergias
        self.detalle_procedimiento = detalle_procedimiento


