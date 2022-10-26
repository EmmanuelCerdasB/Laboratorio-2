import traceback
########Paga por hora

def Paga_por_Horas(horas_trabajadas, costo_x_hora):
    
    paga = horas_trabajadas * costo_x_hora
    
    print("\n\r| Horas trabajadas: ",horas_trabajadas, "\n\r| Costo por hora: ",costo_x_hora, "\n\r| Paga total: ",paga)
    
    
    
########Bienvenida
def bienvenida(nombre):

    print("\n\rBienvenido a la UIA  " + nombre.lower() +"\n\rBienvenido a la UIA " + nombre.upper())
    
    

########Elevar numero entero
def numero_elevar(numero_entero):
    
    try:
 
        if(numero_entero>=1 and numero_entero<=10):
                print(pow(numero_entero,2)) 
                
        elif(numero_entero>=11 and numero_entero<=20):
                print(pow(numero_entero,4))

        elif(numero_entero>=21 and numero_entero<=30):
                print(pow(numero_entero,6))

        elif(numero_entero>=31 and numero_entero<=40):
                print(pow(numero_entero,8))
        
        elif(numero_entero>=41 and numero_entero<=50):
                print(pow(numero_entero,8))

        else:
                print(0)
                
           
            
    except BaseException:
        print(traceback.format_exc())
        
        

######## Numero primo
def numero_primo(numero):
       
    x = 1
    c = 0
      
    while x <= numero:
        if numero % x == 0:
            c=c+1
        x=x+1
    if c==2:
        print("\n\rEl numero ", numero," es primo")
    else:
        print("\n\rEl numero ", numero," no es primo")



########Contador A
def contador_A(txt):
    
    conteo = txt.count('a')
    print("\n\rLa cantidad de veces que aparece la letra A es: ", conteo)
