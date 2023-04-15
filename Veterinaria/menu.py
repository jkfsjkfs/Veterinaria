
from mascotas import Perro, Gato, Pez, Ave
from personas import Cliente, Veterinario
from venta import Venta
from historia import HistoriaClinica

from veterinaria import Veterinaria

veterinaria = Veterinaria()


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


        _veterinaria.mascotas[nueva_mascota.Id] = nueva_mascota
        print("La mascota se agregó correctamente.")
    except ValueError as ve:
        print("Error:", ve)
    except Exception as e:
        print("Ocurrió un error:", e)

    
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


def agregar_veterinario(_veterinaria):
    try:
        cedula = int(input("Ingrese la Identificación del veterinario: "))
        
        for vet in _veterinaria.veterinarios:
            if vet.n_cedula == cedula:
                raise Exception("Ya existe un veterinario con la misma Identificación.")

        nombre = input("Ingrese el nombre del veterinario: ")
        edad = int(input("Ingrese edad del cliente (en años): "))

        usuario = input("Asigne un usuario: ") 
        password = input("Asigne un password: ") 

        nuevo_veterinario = Veterinario(cedula, nombre, edad, usuario, password)
        _veterinaria.veterinarios.append(nuevo_veterinario)
        print("*********************Veterinario agregado correctamente.*********************")

    except ValueError:
        print("********Error: El valor debe ser un número entero.")
    except Exception as e:
        print("********Error al agregar el veterinario: ", e)



def agregar_historia_clinica(_veterinaria):
    try:
        if not mascotas:
            raise Exception("No hay mascotas registradas")
        
        print("Seleccione la mascota a la que desea agregar la historia clínica:")
        for i, mascota in enumerate(mascotas):
            print(f"{i + 1}. {mascota.nombre}")
        
        opcion = int(input("Opción: "))
        mascota_seleccionada = mascotas[opcion - 1]
        
        print(f"Ingresando historia clínica para {mascota_seleccionada.nombre}:")
        fecha = input("Fecha de ingreso (YYYY-MM-DD): ")
        sintomas = input("Síntomas: ")
        diagnostico = input("Diagnóstico: ")
        medicamentos = input("Medicamentos recetados: ")
        
        historia_clinica = HistoriaClinica(fecha, sintomas, diagnostico, medicamentos)
        mascota_seleccionada.agregar_historia_clinica(historia_clinica)
        print("Historia clínica agregada exitosamente!")
        
    except ValueError:
        print("Error: La opción ingresada debe ser un número entero")
    except IndexError:
        print("Error: Opción inválida")
    except Exception as e:
        print(str(e))



def realizar_venta(_veterinaria):
    try:
        if len(_veterinaria.clientes) == 0:
            print("No hay clientes registrados.")
            return

        if len(_veterinaria.mascotas) == 0:
            print("No hay mascotas registradas.")
            return

        if len(_veterinaria.veterinarios) == 0:
            print("No hay veterinarios registrados.")
            return

        cliente_id = int(input("Ingrese el ID del cliente: "))
        cliente = None
        for c in _veterinaria.clientes:
            if c.id == cliente_id:
                cliente = c
                break
        if cliente is None:
            print("No se encontró el cliente con el ID ingresado.")
            return

        mascota_id = int(input("Ingrese el ID de la mascota: "))
        mascota = None
        for m in _veterinaria.mascotas:
            if m.id == mascota_id:
                mascota = m
                break
        if mascota is None:
            print("No se encontró la mascota con el ID ingresado.")
            return

        veterinario_id = int(input("Ingrese la identificación del veterinario: "))
        veterinario = None
        for v in _veterinaria.veterinarios:
            if v.id == veterinario_id:
                veterinario = v
                break
        if veterinario is None:
            print("No se encontró el veterinario con La identificación ingresado.")
            return

        fecha_venta = input("Ingrese la fecha de la venta (en formato dd/mm/yyyy): ")
        monto = float(input("Ingrese el monto de la venta: "))
        venta = Venta(cliente, mascota, veterinario, fecha_venta, monto)
        self.ventas.append(venta)
        print("La venta ha sido registrada con éxito.")
    except ValueError:
        print("Error: el valor ingresado es inválido.")


def menu(veterinaria):
    while True:
        print("------------------------------------------")
        print("Bienvenido al sistema VETERINARIA")
        print("------------------------------------------")
        print("Seleccione una opción:")
        print("1. Agregar cliente")
        print("2. Agregar mascota")
        print("3. Agregar veterinario")
        print("4. Agregar historia clínica")
        print("5. Realizar venta")
        print("6. Salir")
        opcion = input("Opción: ")
        
        if opcion == "1":
            agregar_cliente(veterinaria)
        elif opcion == "2":
            agregar_mascota(veterinaria)
        elif opcion == "3":
            agregar_veterinario(veterinaria)
        elif opcion == "4":
            agregar_historia_clinica(veterinaria)
        elif opcion == "5":
            realizar_venta(veterinaria)
        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida")

        
    




menu(veterinaria)