"""
inicio = int(input("Inicio: "))
fin = int(input("Fin: "))
salto = int(input("Salto: "))
rango = range(inicio,fin,salto)
print(rango)
print(len(rango))
"""

lista = [1,2,3]
lista.append(4)
lista.extend([-1,-2,-3])
lista2 = [7,8,9]
lista.extend(lista2)
print(lista)