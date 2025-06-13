#crear programa de manejo de notas
import os
notas={1,2,3,4,5,6,7}
while True:
    op=int(input("""""""""
      1. Ingresar nota
      2. Borrar nota
      3. Mostrar nota
      4. Sacar promedio, nota mayor y nota menor
      5. Limpiar todas las notas
      6. Salir
      ......
                     """))
    match op:
        case 1:
            nom=input("Ingresa una nota")
            notas.append(nom)
            print(notas)
        case 2:
            for i in range(len(notas)):
                print(i+1, ".-", notas(i))
            rm=int(input("que notas deseas brrrar"))-1
            notas.pop("")

        case 3:
        
        case 4:

        case 5:

        case 6:
            print("Saliendo...")
            break
        case _:
            print("Opcion invalida")
        
