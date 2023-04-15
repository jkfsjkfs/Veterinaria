
from enumerados import Rol, Especie
from abc import ABC

class Mascota(ABC):
    def __init__(self, Id, nombre, cedula_cliente, edad, raza, caracteristicas, peso):
        self.s_nombre = nombre
        self.n_cedula_Cliente = cedula_cliente
        self.n_edad = edad
        self.s_raza = raza
        self.s_caracteristicas = caracteristicas
        self.n_peso = peso
        self.Id = Id


class Perro(Mascota):
    def __init__(self, Id, nombre, cedula_cliente, edad, raza, caracteristicas, peso):
        especie = Especie.Perro
        super().__init__(Id, nombre, cedula_cliente, edad, raza, caracteristicas, peso)

class Gato(Mascota):
    def __init__(self, Id, nombre, cedula_cliente, edad, raza, caracteristicas, peso):
        especie = Especie.Gato
        super().__init__(Id, nombre, cedula_cliente, edad, raza, caracteristicas, peso)

class Pez(Mascota):
    def __init__(self, Id, nombre, cedula_cliente, edad, raza, caracteristicas, peso):
        especie = Especie.Pez
        super().__init__(Id, nombre, cedula_cliente, edad, raza, caracteristicas, peso)

class Ave(Mascota):
    def __init__(self, Id,  nombre, cedula_cliente, edad, raza, caracteristicas, peso):
        especie = Especie.Ave
        super().__init__(Id, nombre, cedula_cliente, edad, raza, caracteristicas, peso)
