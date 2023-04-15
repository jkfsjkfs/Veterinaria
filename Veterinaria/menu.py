from mascotas import Perro, Gato, Pez, Ave
from personas import Cliente, Veterinario, Administrador, Vendedor
from venta import Venta

from orden import Orden
from historia import HistoriaClinica
from veterinaria import Veterinaria
from enumerados import Especie 
from datetime import datetime




veterinaria = Veterinaria()


def InicioSesion(_veterinaria, _lista):
    _veterinaria.usuario = None
    if not _lista:
        print("No hay usuarios registrados")
    else:
        user = int(input("Ingrese la Identificación del usuario: "))
        for usu in _lista:
            if usu.n_cedula == user:
                password = input("Ingrese password: ") 
                if password == usu.s_password:
                    _veterinaria.usuario = usu.s_nombre
                else:
                    print("Passord Incorrecto")
            else:
                print("Usuario NO registrado")
                    
    return (_veterinaria.usuario != None)
            
def CerrarSesion(_veterinaria):
    print("cerrando sesión...")
    _veterinaria.usuario = None
    MenuPpal(_veterinaria)        

    

def agregar_admin(_veterinaria):
    try:
        cedula = int(input("Ingrese la Identificación del Administrador: "))
        
        for vet in _veterinaria.veterinarios:
            if vet.n_cedula == cedula:
                raise Exception("Ya existe un Administrador con la misma Identificación.")

        nombre = input("Ingrese el nombre del Administrador: ")
        edad = int(input("Ingrese edad del Administrador (en años): "))

        password = input("Asigne un password: ") 

        nuevo = Administrador(cedula, nombre, edad, password)
        _veterinaria.administradores.append(nuevo)
        print("*********************Administrador agregado correctamente.*********************")

    except ValueError:
        print("********Error: El valor debe ser un número entero.")
    except Exception as e:
        print("********Error al agregar el Administrador: ", e)


def agregar_vendedor(_veterinaria):
    try:
        cedula = int(input("Ingrese la Identificación del vendedor: "))
        
        for vet in _veterinaria.veterinarios:
            if vet.n_cedula == cedula:
                raise Exception("Ya existe un vendedor con la misma Identificación.")

        nombre = input("Ingrese el nombre del vendedor: ")
        edad = int(input("Ingrese edad del vendedor (en años): "))

        password = input("Asigne un password: ") 

        nuevo = Vendedor(cedula, nombre, edad, password)
        _veterinaria.vendedores.append(nuevo)
        print("*********************vendedor agregado correctamente.*********************")

    except ValueError:
        print("********Error: El valor debe ser un número entero.")
    except Exception as e:
        print("********Error al agregar el vendedor: ", e)


def agregar_veterinario(_veterinaria):
    try:
        cedula = int(input("Ingrese la Identificación del veterinario: "))
        
        for vet in _veterinaria.veterinarios:
            if vet.n_cedula == cedula:
                raise Exception("Ya existe un veterinario con la misma Identificación.")

        nombre = input("Ingrese el nombre del veterinario: ")
        edad = int(input("Ingrese edad del veterinario (en años): "))

        usuario = input("Asigne un usuario: ") 
        password = input("Asigne un password: ") 

        nuevo_veterinario = Veterinario(cedula, nombre, edad, usuario, password)
        _veterinaria.veterinarios.append(nuevo_veterinario)
        print("*********************Veterinario agregado correctamente.*********************")

    except ValueError:
        print("********Error: El valor debe ser un número entero.")
    except Exception as e:
        print("********Error al agregar el veterinario: ", e)
    

def agregar_cliente(_veterinaria):
    try:
        cedula_cliente = int(input("Ingrese Identificación del cliente: "))

        for cliente in _veterinaria.clientes:
            if cliente.n_cedula == cedula_cliente:
                raise Exception("Ya existe un cliente con la misma Identificación.")

        nombre = input("Ingrese el nombre del cliente: ")
        edad = int(input("Ingrese edad del cliente (en años): "))
        
        cliente = Cliente(cedula_cliente, nombre, edad)
        _veterinaria.clientes.append(cliente)
        print("*********************Cliente agregado correctamente.*********************")

    except ValueError:
        print("********Error: El valor deb ser un número entero.")
    except Exception as e:
        print("********Error al agregar el veterinario: ", e)

def agregar_mascota(_veterinaria):
    try:

        cedula_cliente = int(input("Identificación del cliente dueño de la mascota: "))
        
        sw = False
        for cliente in _veterinaria.clientes:
            if cliente.n_cedula == cedula_cliente:
                sw = True
        
        if sw == False:
            raise Exception("El cliente no existe en la BD de la veterinaria.")

        tipo = input("Tipo de mascota (perro, gato, pez o ave): ")

        #nombre = input("Nombre de la mascota: ")
        #edad = int(input("Edad de la mascota: "))
        #peso = float(input("Peso de la mascota (kg): "))
        #caracteristicas = input("Caracteristicas de la mascota (color, tamaño): ")
        #raza = input("Raza del {}: ".format(tipo))
        

        nId = _veterinaria.generaId("mascotas");
        
        if tipo == "perro":
            nueva_mascota = Perro(nId, \
                                  input("Nombre del {}: ".format(tipo)), \
                                  cedula_cliente, \
                                  int(input("Edad del {}: ".format(tipo))), \
                                  input("Raza del {}: ".format(tipo)), \
                                  input("Caracteristicas(color, tamaño): ".format(tipo)),  \
                                  float(input("Peso del {} (kg): ".format(tipo))))
        elif tipo == "gato":
            nueva_mascota = Gato(nId, \
                                 input("Nombre del {}: ".format(tipo)), \
                                 cedula_cliente, \
                                 int(input("Edad del {}: ".format(tipo))), \
                                 input("Raza del {}: ".format(tipo)), \
                                 input("Caracteristicas(color, tamaño): ".format(tipo)),  \
                                 float(input("Peso del {} (kg): ".format(tipo))))
        elif tipo == "pez":
            nueva_mascota = Pez(nId, \
                                input("Nombre del {}: ".format(tipo)), \
                                cedula_cliente, \
                                int(input("Edad del {}: ".format(tipo))), \
                                input("Raza del {}: ".format(tipo)), \
                                input("Caracteristicas(color, tamaño): ".format(tipo)),  \
                                float(input("Peso del {} (kg): ".format(tipo))))
        elif tipo == "ave":
            nueva_mascota = Ave(nId, \
                                input("Nombre del {}: ".format(tipo)), \
                                cedula_cliente, \
                                int(input("Edad del {}: ".format(tipo))), \
                                input("Raza del {}: ".format(tipo)), \
                                input("Caracteristicas(color, tamaño): ".format(tipo)),  \
                                float(input("Peso del {} (kg): ".format(tipo))))
        else:
            raise ValueError("Tipo de mascota inválido.")


        _veterinaria.mascotas.append(nueva_mascota)
        print("*********************La mascota se agregó correctamente.*********************")
    except ValueError as ve:
        print("*********Error:", ve)
    except Exception as e:
        print("*********Ocurrió un error:", e)


def agregar_historia_clinica(_veterinaria):
    try:
        if len(_veterinaria.mascotas) == 0:
            raise Exception("No hay mascotas registradas")
        
        print("Seleccione la mascota a la que desea agregar la historia clínica:")
        for i, mascota in enumerate(_veterinaria.mascotas):
            print(f"{i + 1}. {mascota.s_nombre}")
        
        try:
            opcion = int(input("Opción: "))
        except ValueError:
            raise IndexError()
        
        mascota_seleccionada =_veterinaria.mascotas[opcion - 1]

        print(f"Ingresando historia clínica para {mascota_seleccionada.s_nombre}:")

        cedula_cliente = mascota_seleccionada.n_cedula_Cliente
        id_mascota = mascota_seleccionada.Id
        
        fecha  = None
        try:
            fecha = datetime.strptime(input("Ingrese la fecha de la consulta (AAAA-MM-DD): "), '%Y-%m-%d').date()
        except ValueError:
            raise ValueError("debe ingresar una fecha")
        
        
        cedula_veterinario = int(input("Ingrese la Identificación del Medico veterinario: "))
        medico = ""
        for vet in _veterinaria.veterinarios:
            if vet.n_cedula == cedula_veterinario:
                medico = vet.s_nombre

        if medico == "":
           raise Exception("el medico veterinario NO está registrado.")
        else:
            print(f" ==> {medico}.")


        motivo_consulta = input("Ingrese el motivo de la consulta: ")
        sintomatologia = input("Ingrese la sintomatología: ")
        diagnostico = input("Ingrese el diagnóstico: ")
        procedimiento = input("Ingrese el procedimiento realizado: ")
        medicamento = input("Ingrese el medicamento recetado: ")
        dosis_medicamento = input("Ingrese la dosis del medicamento recetado: ")
        
        historial_vacunacion = ""
        if mascota_seleccionada.especie == Especie.Perro or mascota_seleccionada.especie == Especie.Gato: 
            historial_vacunacion = input("Ingrese el historial de vacunación: ")
            
        alergias = input("Ingrese las alergias del paciente: ")
        detalle_procedimiento = input("Ingrese el detalle del procedimiento realizado: ")

        id_orden = 0
        agregar_ordenes = input("¿Desea agregar una orden? (S/x): ")
        if agregar_ordenes.upper() == "S":
            id_orden = _veterinaria.generaId("ordenes")
            orden = Orden(id_orden, id_mascota, cedula_cliente, cedula_veterinario, medicamento, dosis_medicamento, fecha)
            _veterinaria.ordenes.append(orden)
            print(f"*************Orden {id_orden} Agregada*************")
        else:
            print(f"*************NO se agregó orden a la historia")


        _veterinaria.historias_clinicas.agregar_historia_clinica(id_mascota, fecha, medico, motivo_consulta, sintomatologia, diagnostico, procedimiento, medicamento, dosis_medicamento, id_orden, historial_vacunacion, alergias, detalle_procedimiento)
        print("*********************Historia clínica agregada exitosamente!*********************")
        
    except ValueError as e:
        print("**********Error: {}".format(e))
    except IndexError:
        print("**********Error: Opción inválida")
    except Exception as e:
        print(str(e))


def realizar_venta(_veterinaria):
    try:
        if len(_veterinaria.clientes) == 0:
            print("**********No hay clientes registrados.")
            return

        if len(_veterinaria.mascotas) == 0:
            print("**********No hay mascotas registradas.")
            return

        if len(_veterinaria.veterinarios) == 0:
            print("**********No hay veterinarios registrados.")
            return

        cedula_cliente = int(input("Ingrese la cédula del cliente: "))
        cliente = None
        for c in _veterinaria.clientes:
            if c.n_cedula == cedula_cliente :
                cliente = c
                break

        if cliente is None:
            print("**********No se encontró el cliente.")
            return


        mascotas_cliente = []
        mascota_seleccionada  = None
        for mascota in _veterinaria.mascotas:
            if mascota.n_cedula_Cliente == cedula_cliente:
                mascotas_cliente.append(mascota)

        if len(mascotas_cliente) == 0:
            print("Este cliente no tiene mascotas registradas.")
        else:
            print("Seleccione la mascota a la que desea agregar la historia clínica:")
            for i, mascota in enumerate(mascotas_cliente):
                print(f"{i + 1}. {mascota.s_nombre}")
        
            try:
                opcion = int(input("Opción: "))
            except ValueError:
                raise IndexError()
        
            mascota_seleccionada =_veterinaria.mascotas[opcion - 1]

        
        mascota_id = mascota_seleccionada .Id

        veterinario_id = int(input("Ingrese la identificación del veterinario: "))
        veterinario = None
        for v in _veterinaria.veterinarios:
            if v.n_cedula == veterinario_id:
                veterinario = v
                break
        if veterinario is None:
            print("**********No se encontró el veterinario con La identificación ingresado.")
            return

        fecha  = None
        try:
            fecha = datetime.strptime(input("Ingrese la fecha de la venta (AAAA-MM-DD): "), '%Y-%m-%d').date()
        except ValueError:
            raise ValueError("debe ingresar una fecha")
        
        id_orden = None

        agregar_ordenes = input("¿Desea agregar desde orden - SOLO MEDICAMENTOS - ? (S/x): ")
        if len(_veterinaria.ordenes) > 0 and agregar_ordenes.upper() == "S":
                print("Seleccione la orden:")

                ordenes_cliente = []
                for orden in _veterinaria.ordenes:
                    if orden.cedula_cliente == cedula_cliente:
                        ordenes_cliente.append(orden)

                for i, orden in enumerate(ordenes_cliente):
                    print(f"{i + 1}. NroOrden:{orden.id_orden} Fecha: {orden.fecha_generacion} Medicamento: {orden.nombre_medicamento} Dosis: {orden.dosis}")

                opcion_orden = int(input("Opción: "))
                orden_seleccionada = _veterinaria.ordenes[opcion_orden - 1]
                id_orden = orden_seleccionada.id_orden

                nombre_producto = orden_seleccionada.nombre_medicamento
                print(f"*************Orden {id_orden} Agregada*************")
        else:
            print(f"*************NO se agregó orden a la venta")
            nombre_producto = input("Ingrese el nombre del producto: ")

        valor = float(input("Ingrese el valor del producto: "))
        cantidad = int(input("Ingrese la cantidad del producto: "))


        venta = Venta(_veterinaria.generaId("ventas"), mascota_id, cedula_cliente, veterinario_id, id_orden, nombre_producto, valor, cantidad, fecha)
        _veterinaria.ventas.append(venta)
        print("**********************La venta ha sido registrada con éxito.**********************")
    except ValueError:
        print("**********Error: el valor ingresado es inválido.")
    except IndexError:
        print("**********Error: Opción inválida")


def listar_admin(_veterinaria):
    if not _veterinaria.administradores:
        print("No hay administradores registrados")
    else:
        print("Lista de administradores:")
        print("{:-^100}".format(""))
        print("{:<10} {:<20} {:<10}".format("Cédula", "Nombre", "Edad"))
        print("{:-^100}".format(""))
        for c in _veterinaria.administradores:
            print("{:<10} {:<40} {:<10}".format(c.n_cedula, c.s_nombre, c.n_edad))
        print("{:-^100}".format(""))

def listar_veterinarios(_veterinaria):
    if not _veterinaria.veterinarios:
        print("No hay administradores registrados")
    else:
        print("Lista de veterinarios:")
        print("{:-^100}".format(""))
        print("{:<10} {:<20} {:<10}".format("Cédula", "Nombre", "Edad"))
        print("{:-^100}".format(""))
        for c in _veterinaria.veterinarios:
            print("{:<10} {:<40} {:<10}".format(c.n_cedula, c.s_nombre, c.n_edad))
        print("{:-^100}".format(""))

def listar_vendedores(_veterinaria):
    if not _veterinaria.vendedores:
        print("No hay administradores registrados")
    else:
        print("Lista de vendedores:")
        print("{:-^100}".format(""))
        print("{:<10} {:<20} {:<10}".format("Cédula", "Nombre", "Edad"))
        print("{:-^100}".format(""))
        for c in _veterinaria.vendedores:
            print("{:<10} {:<40} {:<10}".format(c.n_cedula, c.s_nombre, c.n_edad))
        print("{:-^100}".format(""))


def listar_clientes(_veterinaria):
    if not _veterinaria.clientes:
        print("No hay clientes registrados")
    else:
        print("Lista de clientes:")
        print("{:-^100}".format(""))
        print("{:<10} {:<20} {:<10}".format("Cédula", "Nombre", "Edad"))
        print("{:-^100}".format(""))
        for cliente in _veterinaria.clientes:
            print("{:<10} {:<40} {:<10}".format(cliente.n_cedula, cliente.s_nombre, cliente.n_edad))
        print("{:-^100}".format(""))


def listar_mascotas(_veterinaria):
    if not _veterinaria.mascotas:
        print("No hay mascotas registradas")
    else:
        print("{:^100}".format("Listado de Mascotas"))
        print("{:-^100}".format(""))
        print("{:<20} {:<20} {:<20} {:<20}".format("Nombre", "Edad", "Especie", "Dueño"))
        print("{:-^100}".format(""))
        for mascota in _veterinaria.mascotas:
            print("{:<20} {:<20} {:<20} {:<20}".format(mascota.s_nombre, mascota.n_edad, mascota.especie, mascota.n_cedula_Cliente))
        print("{:-^100}".format(""))


def listar_ordenes(_veterinaria):
    if not _veterinaria.ordenes:
        print("No hay órdenes registradas")
    else:
        print("{:^100}".format("Listado de Órdenes"))
        print("{:-^100}".format(""))
        print("{:<20} {:<20} {:<20} {:<20} {:<20}".format("ID", "Fecha", "Cliente", "Veterinario", "Producto"))
        print("{:-^100}".format(""))
        for orden in _veterinaria.ordenes:
            print("{:<20} {:<20} {:<20} {:<20} {:<20}".format(orden.id_orden, orden.fecha_generacion, orden.cedula_cliente, orden.cedula_veterinario, orden.nombre_medicamento))
        print("{:-^100}".format(""))



def listar_ventas(_veterinaria):
    if not _veterinaria.ventas:
        print("No hay ventas registradas")
    else:
        print("{:^100}".format("Listado de Ventas"))
        print("{:-^100}".format(""))
        print("{:<20} {:<20} {:<20} {:<20} {:<20}".format("Fecha", "Cliente", "Pruducto", "Cantidad", "Valor", "Total"))
        print("{:-^100}".format(""))
        for venta in _veterinaria.ventas:
            print("{:<20} {:<20} {:<20} {:<20} {:<20}".format(venta.d_fecha, venta.n_cedula_Cliente, venta.s_nombre_producto, venta.n_cantidadntidad , venta.n_valor, venta.n_valor*venta.n_cantidadntidad ))
        print("{:-^100}".format(""))


        
def MenuPpal(veterinaria):
    while True:
        print("------------------------------------------")
        print(f"Bienvenido al sistema VETERINARIA")
        print("------------------------------------------")
        print("Seleccione una opción:")
        print("1.  Iniciar como administrador")
        print("2.  Iniciar como veterinario")
        print("3.  Iniciar como vendedor")
        print("100. Salir del sistema")
        print("..................")
        opcion = input("Opción: ")
        

        if opcion == "1":
            if not veterinaria.administradores or InicioSesion(veterinaria, veterinaria.administradores):
                MenuAdmin(veterinaria)
        elif opcion == "2":
            if InicioSesion(veterinaria, veterinaria.veterinarios):
                MenuVeterinario(veterinaria)
        elif opcion == "3":
            if InicioSesion(veterinaria,veterinaria.vendedores):
                MenuVendedor(veterinaria)
        elif opcion == "100":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida")


def MenuAdmin(veterinaria):
    while True:
        print("------------------------------------------")
        print(f"Bienvenido al sistema VETERINARIA - {veterinaria.usuario}")
        print("------------------------------------------")
        print("Seleccione una opción:")
        print("1.  Agregar administrador")
        print("2.  Agregar veterinario")
        print("3.  Agregar vendedor")
        print("4.  Agregar cliente")
        print("5.  Agregar mascota")
        print("6.  Agregar historia clínica")
        print("7.  Realizar venta")
        print("..................")
        print("8.  Lista de Administradores")
        print("9.  Lista de Veterinarios")
        print("10. Lista de Vendedores")
        print("11. Lista de Clientes")
        print("12. Lista de Mascotas")
        #print("13. Lista de Historias clínicas")
        print("14. Lista de Ordenes")
        print("15. Lista de Ventas")
        print("..................")
        print("99. Cerrar sesión")
        print("..................")
        opcion = input("Opción: ")
        
        if opcion == "1":
            agregar_admin(veterinaria)
        elif opcion == "2":
            agregar_veterinario(veterinaria)
        elif opcion == "3":
            agregar_vendedor(veterinaria)
        elif opcion == "4":
            agregar_cliente(veterinaria)
        elif opcion == "5":
            agregar_mascota(veterinaria)
        elif opcion == "6":
            agregar_historia_clinica(veterinaria)
        elif opcion == "7":
            realizar_venta(veterinaria)

        elif opcion == "8":
            listar_admin(veterinaria)
        elif opcion == "9":
            listar_veterinarios(veterinaria)
        elif opcion == "10":
            listar_vendedores(veterinaria)
        elif opcion == "11":
            listar_clientes(veterinaria)
        elif opcion == "12":
            listar_mascotas(veterinaria)

        elif opcion == "12":
            listar_mascotas(veterinaria)
        elif opcion == "14":
            listar_ordenes(veterinaria)

        elif opcion == "15":
            listar_ventas(veterinaria)


        elif opcion == "99":
            CerrarSesion(veterinaria)
        else:
            print("Opción no válida")

def MenuVeterinario(veterinaria):
    while True:
        print("------------------------------------------")
        print(f"Bienvenido al sistema VETERINARIA - {veterinaria.usuario}")
        print("------------------------------------------")
        print("Seleccione una opción:")
        print("4.  Agregar cliente")
        print("5.  Agregar mascota")
        print("6.  Agregar historia clínica")
        print("..................")
        print("11. Lista de Clientes")
        print("12. Lista de Mascotas")
        print("14. Lista de Ordenes")
        print("..................")
        print("99. Cerrar sesión")
        print("..................")
        opcion = input("Opción: ")
        
        if opcion == "4":
            agregar_cliente(veterinaria)
        elif opcion == "5":
            agregar_mascota(veterinaria)
        elif opcion == "6":
            agregar_historia_clinica(veterinaria)
        elif opcion == "11":
            listar_clientes(veterinaria)
        elif opcion == "12":
            listar_mascotas(veterinaria)

        elif opcion == "12":
            listar_mascotas(veterinaria)
        elif opcion == "14":
            listar_ordenes(veterinaria)

        elif opcion == "99":
            CerrarSesion(veterinaria)
        else:
            print("Opción no válida")

def MenuVendedor(veterinaria):
    while True:
        print("------------------------------------------")
        print(f"Bienvenido al sistema VETERINARIA - {veterinaria.usuario}")
        print("------------------------------------------")
        print("Seleccione una opción:")
        print("4.  Agregar cliente")
        print("7.  Realizar venta")
        print("..................")
        print("11. Lista de Clientes")
        print("14. Lista de Ordenes")
        print("15. Lista de Ventas")
        print("..................")
        print("99. Cerrar sesión")
        print("..................")
        opcion = input("Opción: ")
        
        if opcion == "4":
            agregar_cliente(veterinaria)
            agregar_historia_clinica(veterinaria)
        elif opcion == "7":
            realizar_venta(veterinaria)

        elif opcion == "11":
            listar_clientes(veterinaria)
        elif opcion == "14":
            listar_ordenes(veterinaria)

        elif opcion == "15":
            listar_ventas(veterinaria)
        elif opcion == "99":
            print("cerrando sesión...")
        else:
            print("Opción no válida")




MenuPpal(veterinaria)