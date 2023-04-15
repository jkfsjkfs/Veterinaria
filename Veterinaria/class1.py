

class Historia:
    id_Mascota = 0
    d_fecha = {1/1/2000}
    n_cedula_Veterinario = 0
    s_motivo = ""
    s_sintomas = ""
    s_diagnostico = ""
    s_procedimiento = ""
    s_medicamento = ""
    n_dosis = 0.0
    id_Orden = 0
    s_vacunas = ""
    s_alergia_medicamento = ""
    s_detalle_procedimiento = "" 


class Orden:
    Id = 0
    id_Mascota = 0
    n_cedula_Cliente = 0
    n_cedula_Veterinario = 0
    d_fecha = {1/1/2000}
    s_nombre_medicamento = ""
    n_dosis = 0.0


    
class Venta:
    Id = 0
    id_Mascota = 0
    n_cedula_Cliente = 0
    n_cedula_Veterinario = 0
    id_Orden = 0
    d_fecha = {1/1/2000}
    s_nombre_producto = ""
    n_valor = 0.0
    n_cantidad = 0

