import traceback
from Funciones import Paga_por_Horas, bienvenida, numero_elevar, numero_primo, contador_A




def menu():
    opcion = 0
    
    while opcion != 6:
        opcion = int(input("""
                    Menu principal
       1- Paga por Horas                      | 
       2- Ingrese su nombre                   | 
       3- Digite un numero entero del 1 al 50 | 
       4- Numero primo o no?                  | 
       5- Conteo de A en un texto             | 
       6- Salir                               |
       
       """))

        if (opcion == 1):
                
            horas_trabajadas = int(input("digite las horas trabajadas: "))
            costo_x_hora = int(input("digite el costo por hora: "))
            Paga_por_Horas(horas_trabajadas, costo_x_hora)
            
        if (opcion == 2):
            
            nombre = str(input("Digite su nombre: "))
            bienvenida(nombre)
                
        if (opcion == 3):
                
            numero_entero = int(input("digite un numero entero entre 1 a 50: "))
            numero_elevar(numero_entero)
                
        if (opcion == 4):

            numero = int(input("digite un numero para verificar si es primo: "))
            numero_primo(numero)
                
        if (opcion == 5):
                
            txt = str(input("Digite el texto que desea contar sus A: "))
            contador_A(txt)
                
        if (opcion == 6):
            print("Programa finalizado, gracias")
            
            

menu()