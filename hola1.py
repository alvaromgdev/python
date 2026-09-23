"""
diccionario = {
    "nombre" : "Pepe",
    "apellido" : "López",
    "edad" : 18
}

diccionario["edad"] = 20
diccionario["direccion"] = "Calle 1"
del diccionario["edad"]
print(diccionario["direccion"])
print(diccionario)

lista = [1,2,3]
estudiante = {
    "nombre" : "Joselín",
    "apellido" : "Flores",
    "modulos" : ["Acceso a datos", "Python", "Proyecto"]
}
print(estudiante["modulos"][0])
"""
"""
estudiantes = [
    {
        "nombre" : "Joselín",
        "apellido" : "Flores",
        "modulos" : ["Acceso a datos", "Python", "Proyecto"]
    },
        {
        "nombre" : "Camilo",
        "apellido" : "Sesto",
        "modulos" : ["Acceso a datos", "Desarrollo de interfaces"]
    }
]
print(estudiantes[0]["modulos"][0])
"""

conjunto = {1, 2, 3, 3, 4}
conjunto.add(7)
conjunto.remove(3)
print(conjunto)

def main():
    print("ESTE ES EL MAIN")

if __name__ == "__main__":
    main()