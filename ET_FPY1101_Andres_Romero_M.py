# https://github.com/andRomerom/ExamenTransversal/upload
from random import randint
# trabajadores=["Juan Pérez","María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel,Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]   
trabajadores=["Juan Pérez", 'María García' , 'Carlos López','Ana Martínez','Pedro Rodríguez','Laura Hernández','Miguel,Sánchez','Isabel Gómez','Francisco Díaz','Elena Fernández']   
sueldos=[]
sueldoMayor=0 
sueldoMenor=500000 
ruta="D:/CSV/reporte.csv"     

def dibujaMenu():
    print("---------Menu--------")
    print("                     ")
    print("1. Asignar sueldos aleatorios ")
    print("2. Clasificar sueldos")
    print("3. Ver estadísticas")
    print("4. Reporte de sueldos         ")
    print("5. Salir del programa")
def asignaSuledo():    
    
    for i in trabajadores:
      
         nombre=(f"{i.ljust(20)} \n")
         sueldo = int((f"{str(randint(100,1000)).ljust(5)}"))
         sueldos.append({"nombre":nombre, "sueldo":sueldo})  
    print("sueldos asignados exitosamente")

def clasificaSueldos():
    for i in sueldos:
        print(i["sueldo"])
       
        if   int(sueldoMayor) < int(i["sueldo"]) :
        # i["sueldo"] :
             print(sueldoMayor)
                
    print("el sueldo mayor es",sueldoMayor) 
    # print("el sueldo menor es",sueldoMenor) 
        
def estadisticas():
     print("aca no hace nada, no insista")
    
def reporteSueldos():     
    with open("Andres_Romero",'w') as f:
        for i in sueldos: 
            # f.write(i["nombre"])  
            # f.write(str(i["sueldo"]))
            f.write(str(i)) 
            print(" \n")   
          
            # f.write(str(i))   
              

while True:
      dibujaMenu()
      opc=input("Ingrese Opcion --> " )   
      if  opc=="1":
            asignaSuledo()        
      elif  opc=="2":
            clasificaSueldos()
      elif  opc=="3":
            estadisticas()
      elif  opc=="4":
            print("Salir del menu")
            reporteSueldos()       
      elif  opc=="5":
            print("Andres Romero Madrid")
            print("14.379.698-1")
            break
            
        
      

        
