cantidad=0
total=0

print("Hola, bienvenido a Sushiu")

while True:
    op=int(input("""
        1.- Pikachu Roll $4500
        2.- Otaku Roll $5000
        3.- Pulpo Venenoso Roll $5200
        4.- Anguila Eléctrica Roll $4800
                """))
    match op:
        case 1:
            cantidad+=1
            total=total+4500
        case 2:
            cantidad+=1
            total=total+5000
        case 3:
            cantidad+=1
            total=total+5200
        case 4:
            cantidad+=1
            total=total+4800
        case _:
            print("Elige una de las opciones")
            break







# if codigoDesc=="agUantelaU":
#     print("Aplica descuento")
#     desc=total*0.1
#     total=total-desc



    
# CODIGO POR CHATGPT

# def mostrar_menu():
#     print("\nMenú de Rolls:")
#     print("1. Pikachu Roll - $4500")
#     print("2. Otaku Roll - $5000")
#     print("3. Pulpo Venenoso Roll - $5200")
#     print("4. Anguila Eléctrica Roll - $4800")
#     print("5. Finalizar pedido")

# def solicitar_codigo_descuento():
#     while True:
#         codigo = input("¿Tiene un código de descuento? (si/no): ").lower()
#         if codigo == "si":
#             while True:
#                 ingreso = input("Ingrese el código de descuento o 'X' para volver al menú: ")
#                 if ingreso == "soyotaku":
#                     return 0.1  # 10% de descuento
#                 elif ingreso.upper() == "X":
#                     return 0.0
#                 else:
#                     print("Código no válido.")
#         elif codigo == "no":
#             return 0.0
#         else:
#             print("Respuesta no válida, escriba 'si' o 'no'.")

# def mostrar_detalle(pedido, precios, descuento):
#     print("\n******************************")
#     total_productos = sum(pedido.values())
#     print(f"TOTAL PRODUCTOS: {total_productos}")
#     print("******************************")
#     for roll in pedido:
#         print(f"{roll} : {pedido[roll]}")
#     subtotal = sum(pedido[roll] * precios[roll] for roll in pedido)
#     descuento_valor = subtotal * descuento
#     total = subtotal - descuento_valor
#     print("******************************")
#     print(f"Subtotal por pagar: ${subtotal}")
#     print(f"Descuento por código: ${int(descuento_valor)}")
#     print(f"TOTAL: ${int(total)}")
#     print("******************************")

# def main():
#     precios = {
#         "Pikachu Roll": 4500,
#         "Otaku Roll": 5000,
#         "Pulpo Venenoso Roll": 5200,
#         "Anguila Eléctrica Roll": 4800
#     }

#     while True:
#         pedido = {roll: 0 for roll in precios}
#         while True:
#             mostrar_menu()
#             opcion = input("Seleccione una opción (1-5): ")
#             if opcion == "1":
#                 pedido["Pikachu Roll"] += 1
#             elif opcion == "2":
#                 pedido["Otaku Roll"] += 1
#             elif opcion == "3":
#                 pedido["Pulpo Venenoso Roll"] += 1
#             elif opcion == "4":
#                 pedido["Anguila Eléctrica Roll"] += 1
#             elif opcion == "5":
#                 break
#             else:
#                 print("Opción no válida.")

#         descuento = solicitar_codigo_descuento()
#         mostrar_detalle(pedido, precios, descuento)

#         otra = input("¿Desea realizar otro pedido? (si/no): ").lower()
#         if otra != "si":
#             print("Gracias por usar nuestro sistema de pedidos.")
#             break

# if __name__ == "__main__":
#     main()
