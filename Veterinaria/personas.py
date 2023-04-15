
from enumerados import Rol
from abc import ABC, abstractmethod


class Persona(ABC):
    def __init__(self, cedula, nombre, edad):
        self.n_cedula = cedula
        self.s_nombre = nombre
        self.n_edad = edad
        

class Usuario(Persona, ABC):
    def __init__(self, cedula, nombre, edad, usuario, password):
        super().__init__(cedula, nombre, edad)
        self.s_usuario = usuario
        self.s_password = password


class Administrador(Usuario):
    def __init__(self, cedula, nombre, edad, rol, usuario, password):
        super().__init__(cedula, nombre, edad, usuario, password)
        self.e_rol = Rol.Admin

class Veterinario(Usuario):
    def __init__(self, cedula, nombre, edad, usuario, password):
        super().__init__(cedula, nombre, edad, usuario, password)
        self.e_rol = Rol.Veterinario

class Cliente(Persona):
    def __init__(self, cedula, nombre, edad):
        super().__init__(cedula, nombre, edad)
        self.e_rol = Rol.Cliente


class Vendedor(Usuario):
    def __init__(self, cedula, nombre, edad, usuario, password):
        super().__init__(cedula, nombre, edad, usuario, password)
        self.e_rol = Rol.Vendedor

