######################
## Variables necesarias para las funciones establecidas:

######################################################################
import random
pc = 0 #Contador partidas ganadas por la PC
pl = 0 #Contador partidas ganadas por el Jugador
em = 0 #Contador para empates
totalPartidas=0 #Contador para la cantidad de partidas
#Contadores de cuantas veces el jugador Y COM a usado un arma
player_piedra = 0 
player_spock = 0
player_papel = 0
player_lagarto = 0
player_tijeras = 0
com_piedra = 0
com_spock = 0
com_papel = 0
com_lagarto = 0
com_tijeras = 0
##############################
listapl=[] #Lista usada para llevar registro sobre las armas del jugador
listacom=[] #Lista usada para llevar registro sobre las armas de la computadora
contador=0 # Lleva registro sobre el numero de partidas que se van jugando para realizar intervenciones espeficas
anteriorpl=int # Utilizado en los niveles 3 y 4 registra el arma anterior del jugador
anteriorcom=int # Utilizado en el nivel 4 registra el arma anterior de la com
difference=int  # Modulo utilizado para verificar un ganador

#######################################

### Funciones auxiliares ###
#Convertir el numero a un nombre usando if / elif /

# Entradas: numero *+* entero entre 0 y 5 para seleccionar arma
# Salidas: string correspondiente segun el numero seleccionado
#Restricciones: La entrada esta establecida en un rango de 0 a 5 dado el numero de armas disponibles


def numero_a_arma(numero):  
    
    if numero==0:return "piedra"  
    elif numero==1:return "spock"  
    elif numero==2:return "papel"  
    elif numero==3:return "lagarto"  
    elif numero==4:return "tijeras"  
    else:  
        print('Error! El número no está en el rango correcto.')  
      
    
# Convertir el nombre a un numero usando if / elif /

#Entradas : String a evuluar segun haya sido seleccionado previamente
#Salidas : numero asignado segun el arma elegida para la comparacion de un ganador
#Restricciones : Arma esta dado bajo un rango de 5 nombres
def arma_a_numero(arma):  
    
    if arma=="piedra":return 0  
    elif arma=="spock":return 1  
    elif arma=="papel":return 2  
    elif arma=="lagarto":return 3  
    elif arma=="tijeras":return 4  
    else:  
        print('Error! El nombre no es valido')  

#######################################










####### Funcion Jugar:
# JUGAR NIVEL 1
# Funcion encargada de llamar a nivel #1
# Entradas : nivel segun usuario haya eligido
# Salidas : 
def jugar(nivel):
    global player_piedra
    global player_spock
    global player_papel
    global player_lagarto
    global player_tijeras
    

        
    menu = {}
    menu['1']="piedra" 
    menu['2']="spock"
    menu['3']="papel"
    menu['4']="lagarto"
    menu['5']="tijeras"
    menu['6']="salir"
    while True:
      global ans
      options=menu.keys()
      
      for entry in sorted(options): 
        print (entry, menu[entry])

      selection=input("Selecciona alguno "+ans+":") 

      if selection =='1':


        player_piedra=player_piedra+1
        rpsls ("piedra")
      elif selection == '2':
     
        player_spock += 1
        rpsls ("spock")
      elif selection == '3':
    
        player_papel += 1
        rpsls ("papel") 
      elif selection == '4':
      
        player_lagarto += 1
        rpsls ("lagarto")
      elif selection == '5':
 
        player_tijeras += 1
        rpsls ("tijeras")
      elif selection == '6':
          
        global totalPartidas
        global pc
        global pl
        global em
        global com_piedra
        global com_spock
        global com_papel
        global com_lagarto
        global com_tijeras
        global totalPartidas
        totalPartidas=pc+pl+em
        if totalPartidas==0:
            piedracom=0
            spockcom=0
            papelcom=0
            lagartocom=0
            tijerascom=0
            piedrapl=0
            spockpl=0
            papelpl=0
            lagartopl=0
            tijeraspl=0
        else:
            
            ####### Variables Para el porcentaje de la PC
            totalcom=com_piedra+com_spock+com_papel+com_lagarto+com_tijeras #Representa el divisor para el porcentataje de la COM
            piedracom=com_piedra/totalcom*100 # Porcentaje calculado para piedra
            spockcom=com_spock/totalcom*100 #Porcentaje callculado para spock
            papelcom=com_papel/totalcom*100 #Porcentaje calculado para papel
            lagartocom=com_lagarto/totalcom*100 # Porcentae calculado para lagarto
            tijerascom=com_tijeras/totalcom*100 # Porcentaje calculado para tijeras
            
            ###### Variables Para el porcentaje de Jugador
            totalpl=player_piedra+player_spock+player_papel+player_lagarto+player_tijeras #Representa el divisor para el porcentataje de Jugador
            piedrapl=player_piedra/totalpl*100 # Porcentaje calculado para piedra
            spockpl=player_spock/totalpl*100 #Porcentaje callculado para spock
            papelpl=player_papel/totalpl*100 #Porcentaje calculado para papel
            lagartopl=player_lagarto/totalpl*100 # Porcentae calculado para lagarto
            tijeraspl=player_tijeras/totalpl*100  # Porcentaje calculado para tijera
        print("==========================================================")

        print('MARCADOR FINALL!!:'+ans+ ': '+str(pl)+' COM : '+str(pc)+'\n'+'Total de rondas fueron: '+str(totalPartidas)+'\nGanadas por COM: '+ str(pc) + '\n' +'Veces Empate'+': '+ str(em)+ '\n' +'Ganadas por '+ans+' : '+ str(pl))

        if pc>pl:
            print('EL GANADOR ES COM SUERTE PARA LA PROXIMA '+ans)
        elif pc==pl:
            print('VAYA HA HABIDO UN EMPATE!!')
        else:
            print('FELICIDADES '+ans+ ' ERES EL REY EN PIEDRA,PAPEL,TIJERA,LAGARTO,SPOCK')
            
        print()
        print("***********************************************************")
        print("-----------------Registro De Armas-------------------------")
        print()
        print('Veces usadas por ',ans,':')
        print()
        print('Piedra:',player_piedra,' %:'+str(piedrapl))
        print('Spock:', player_spock, '%: '+str(spockpl))
        print('Papel:', player_papel,'%: '+str(papelpl))
        print('Lagarto:',player_lagarto,'%: '+str(lagartopl))
        print('Tijeras:',player_tijeras,'%: '+str(tijeraspl))
        print()
        print('*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*')

        print('Veces usadas por Com:')
        print('Piedra:',com_piedra,' %:'+str(piedracom))
        print('Spock:',com_spock, '%: '+str(spockcom))
        print('Papel:',com_papel,'%: '+str(papelcom))
        print('Lagarto:',com_lagarto,'%: '+str(lagartocom))
        print('Tijeras:',com_tijeras,'%: '+str(tijerascom))

        print('================================\n')
        ans1 = input('Deseas jugar de nuevo'+'\n Jugar ( J ) \n Salir  ( ALGUNA TECLA )\n')
        if ans1=='J':
            pc = 0 
            pl = 0
            em = 0
            totalPartidas=0 
            #Contadores de cuantas veces el jugador Y COM a usado un arma
            player_piedra = 0 
            player_spock = 0
            player_papel = 0
            player_lagarto = 0
            player_tijeras = 0
            com_piedra = 0
            com_spock = 0
            com_papel = 0
            com_lagarto = 0
            com_tijeras = 0
            ##############################
            listapl=[]
            listacom=[]
            contador=0
            anteriorpl=int
            anteriorcom=int
            difference=int
            
            main()
        else:
            sys.exit()
      else: 
        print ("No elegiste bien!")

####### JUGAR NIVEL2:
def jugar2(nivel):
    global player_piedra
    global player_spock
    global player_papel
    global player_lagarto
    global player_tijeras
    

        
    menu = {}
    menu['1']="piedra" 
    menu['2']="spock"
    menu['3']="papel"
    menu['4']="lagarto"
    menu['5']="tijeras"
    menu['6']="salir"
    while True:
      global ans
      options=menu.keys()
      
      for entry in sorted(options): 
        print (entry, menu[entry])

      selection=input("Selecciona alguno "+ans+":") 

      if selection =='1':

      
        player_piedra=player_piedra+1
        Nivel2 ("piedra")
      elif selection == '2':
     
        player_spock += 1
        Nivel2 ("spock")
      elif selection == '3':
     
        player_papel += 1
        Nivel2 ("papel") 
      elif selection == '4':
       
        player_lagarto += 1
        Nivel2 ("lagarto")
      elif selection == '5':
    
        player_tijeras += 1
        Nivel2 ("tijeras")
      elif selection == '6':
          
        global totalPartidas
        global pc
        global pl
        global em
      
        global com_piedra
        global com_spock
        global com_papel
        global com_lagarto
        global com_tijeras
        global totalPartidas
        totalPartidas=pc+pl+em
        if totalPartidas==0:
            piedracom=0
            spockcom=0
            papelcom=0
            lagartocom=0
            tijerascom=0
            piedrapl=0
            spockpl=0
            papelpl=0
            lagartopl=0
            tijeraspl=0
        else:
            
            ####### Variables Para el porcentaje de la PC
            totalcom=com_piedra+com_spock+com_papel+com_lagarto+com_tijeras #Representa el divisor para el porcentataje de la COM
            piedracom=com_piedra/totalcom*100 # Porcentaje calculado para piedra
            spockcom=com_spock/totalcom*100 #Porcentaje callculado para spock
            papelcom=com_papel/totalcom*100 #Porcentaje calculado para papel
            lagartocom=com_lagarto/totalcom*100 # Porcentae calculado para lagarto
            tijerascom=com_tijeras/totalcom*100 # Porcentaje calculado para tijeras
            
            ###### Variables Para el porcentaje de Jugador
            totalpl=player_piedra+player_spock+player_papel+player_lagarto+player_tijeras #Representa el divisor para el porcentataje de Jugador
            piedrapl=player_piedra/totalpl*100 # Porcentaje calculado para piedra
            spockpl=player_spock/totalpl*100 #Porcentaje callculado para spock
            papelpl=player_papel/totalpl*100 #Porcentaje calculado para papel
            lagartopl=player_lagarto/totalpl*100 # Porcentae calculado para lagarto
            tijeraspl=player_tijeras/totalpl*100  # Porcentaje calculado para tijera
            print("==========================================================")

        print('MARCADOR FINALL!!:'+ans+ ': '+str(pl)+' COM : '+str(pc)+'\n'+'Total de rondas fueron: '+str(totalPartidas)+'\nGanadas por COM: '+ str(pc) + '\n' +'Veces Empate'+': '+ str(em)+ '\n' +'Ganadas por '+ans+' : '+ str(pl))

        if pc>pl:
            print('EL GANADOR ES COM SUERTE PARA LA PROXIMA '+ans)
        elif pc==pl:
            print('VAYA HA HABIDO UN EMPATE!!')
        else:
            print('FELICIDADES '+ans+' ERES EL REY EN PIEDRA,PAPEL,TIJERA,LAGARTO,SPOCK')
            
        print()
        print("***********************************************************")
        print("-----------------Registro De Armas-------------------------")
        print()
        print('Veces usadas por ',ans,':')
        print()
        print('Piedra:',player_piedra,' %:'+str(piedrapl))
        print('Spock:', player_spock, '%: '+str(spockpl))
        print('Papel:', player_papel,'%: '+str(papelpl))
        print('Lagarto:',player_lagarto,'%: '+str(lagartopl))
        print('Tijeras:',player_tijeras,'%: '+str(tijeraspl))
        print()
        print('*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*')

        print('Veces usadas por Com:')
        print('Piedra:',com_piedra,' %:'+str(piedracom))
        print('Spock:',com_spock, '%: '+str(spockcom))
        print('Papel:',com_papel,'%: '+str(papelcom))
        print('Lagarto:',com_lagarto,'%: '+str(lagartocom))
        print('Tijeras:',com_tijeras,'%: '+str(tijerascom))

        print('================================\n')
        ans1 = input('Deseas jugar de nuevo'+'\n Jugar ( J ) \n Salir  ( ALGUNA TECLA )\n')
        if ans1=='J':
            pc = 0 
            pl = 0
            em = 0
            totalPartidas=0 
            #Contadores de cuantas veces el jugador Y COM a usado un arma
            player_piedra = 0 
            player_spock = 0
            player_papel = 0
            player_lagarto = 0
            player_tijeras = 0
            com_piedra = 0
            com_spock = 0
            com_papel = 0
            com_lagarto = 0
            com_tijeras = 0
            ##############################
            listapl=[]
            listacom=[]
            contador=0
            anteriorpl=int
            anteriorcom=int
            difference=int
            main()
        else:
            sys.exit()
      else: 
        print ("No elegiste bien!")

##########################################
        # Jugar Nivel3:
def jugar3(nivel):
    global player_piedra
    global player_spock
    global player_papel
    global player_lagarto
    global player_tijeras
    

        
    menu = {}
    menu['1']="piedra" 
    menu['2']="spock"
    menu['3']="papel"
    menu['4']="lagarto"
    menu['5']="tijeras"
    menu['6']="salir"
    while True:
      global ans
      options=menu.keys()
      
      for entry in sorted(options): 
        print (entry, menu[entry])

      selection=input("Selecciona alguno "+ans+":") 

      if selection =='1':

  
        player_piedra=player_piedra+1
        Nivel3 ("piedra")
      elif selection == '2':
     
        player_spock += 1
        Nivel3 ("spock")
      elif selection == '3':
 
        player_papel += 1
        Nivel3 ("papel") 
      elif selection == '4':
   
        player_lagarto += 1
        Nivel3 ("lagarto")
      elif selection == '5':
      
        player_tijeras += 1
        Nivel3 ("tijeras")
      elif selection == '6':
          
        global totalPartidas
        global pc
        global pl
        global em
       
        global com_piedra
        global com_spock
        global com_papel
        global com_lagarto
        global com_tijeras
        global totalPartidas
        totalPartidas=pc+pl+em
        if totalPartidas==0:
            piedracom=0
            spockcom=0
            papelcom=0
            lagartocom=0
            tijerascom=0
            piedrapl=0
            spockpl=0
            papelpl=0
            lagartopl=0
            tijeraspl=0
        else:
            
            ####### Variables Para el porcentaje de la PC
            totalcom=com_piedra+com_spock+com_papel+com_lagarto+com_tijeras #Representa el divisor para el porcentataje de la COM
            piedracom=com_piedra/totalcom*100 # Porcentaje calculado para piedra
            spockcom=com_spock/totalcom*100 #Porcentaje callculado para spock
            papelcom=com_papel/totalcom*100 #Porcentaje calculado para papel
            lagartocom=com_lagarto/totalcom*100 # Porcentae calculado para lagarto
            tijerascom=com_tijeras/totalcom*100 # Porcentaje calculado para tijeras
            
            ###### Variables Para el porcentaje de Jugador
            totalpl=player_piedra+player_spock+player_papel+player_lagarto+player_tijeras #Representa el divisor para el porcentataje de Jugador
            piedrapl=player_piedra/totalpl*100 # Porcentaje calculado para piedra
            spockpl=player_spock/totalpl*100 #Porcentaje callculado para spock
            papelpl=player_papel/totalpl*100 #Porcentaje calculado para papel
            lagartopl=player_lagarto/totalpl*100 # Porcentae calculado para lagarto
            tijeraspl=player_tijeras/totalpl*100  # Porcentaje calculado para tijera
        print("==========================================================")

        print('MARCADOR FINALL!!:'+ans+ ': '+str(pl)+' COM : '+str(pc)+'\n'+'Total de rondas fueron: '+str(totalPartidas)+'\nGanadas por COM: '+ str(pc) + '\n' +'Veces Empate'+': '+ str(em)+ '\n' +'Ganadas por '+ans+' : '+ str(pl))

        if pc>pl:
            print('EL GANADOR ES COM SUERTE PARA LA PROXIMA '+ans)
        elif pc==pl:
            print('VAYA HA HABIDO UN EMPATE!!')
        else:
            print('FELICIDADES '+ans+' ERES EL REY EN PIEDRA,PAPEL,TIJERA,LAGARTO,SPOCK')
            
        print()
        print("***********************************************************")
        print("-----------------Registro De Armas-------------------------")
        print()
        print('Veces usadas por ',ans,':')
        print()
        print('Piedra:',player_piedra,' %:'+str(piedrapl))
        print('Spock:', player_spock, '%: '+str(spockpl))
        print('Papel:', player_papel,'%: '+str(papelpl))
        print('Lagarto:',player_lagarto,'%: '+str(lagartopl))
        print('Tijeras:',player_tijeras,'%: '+str(tijeraspl))
        print()
        print('*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*')

        print('Veces usadas por Com:')
        print('Piedra:',com_piedra,' %:'+str(piedracom))
        print('Spock:',com_spock, '%: '+str(spockcom))
        print('Papel:',com_papel,'%: '+str(papelcom))
        print('Lagarto:',com_lagarto,'%: '+str(lagartocom))
        print('Tijeras:',com_tijeras,'%: '+str(tijerascom))

        print('================================\n')
        ans1 = input('Deseas jugar de nuevo'+'\n Jugar ( J ) \n Salir  ( ALGUNA TECLA )\n')
        if ans1=='J':
            pc = 0 
            pl = 0
            em = 0
            totalPartidas=0 
            #Contadores de cuantas veces el jugador Y COM a usado un arma
            player_piedra = 0 
            player_spock = 0
            player_papel = 0
            player_lagarto = 0
            player_tijeras = 0
            com_piedra = 0
            com_spock = 0
            com_papel = 0
            com_lagarto = 0
            com_tijeras = 0
            ##############################
            listapl=[]
            listacom=[]
            contador=0
            anteriorpl=int
            anteriorcom=int
            difference=int
            
            main()
        else:
            sys.exit()
      else: 
        print ("No elegiste bien!")

##########################################33
        # Jugar Nivel 4:
def jugar4(nivel):
    global player_piedra
    global player_spock
    global player_papel
    global player_lagarto
    global player_tijeras
    

        
    menu = {}
    menu['1']="piedra" 
    menu['2']="spock"
    menu['3']="papel"
    menu['4']="lagarto"
    menu['5']="tijeras"
    menu['6']="salir"
    while True:
      global ans
      options=menu.keys()
      
      for entry in sorted(options): 
        print (entry, menu[entry])

      selection=input("Selecciona alguno "+ans+":") 

      if selection =='1':

        
        player_piedra=player_piedra+1
        Nivel4 ("piedra")
      elif selection == '2':
        
        player_spock=player_spock+1
        Nivel4 ("spock")
      elif selection == '3':
       
        player_papel = player_papel+1
        Nivel4 ("papel") 
      elif selection == '4':
        
        player_lagarto =player_lagarto+1
        Nivel4 ("lagarto")
      elif selection == '5':
        
        player_tijeras =player_tijeras+1
        Nivel4 ("tijeras")
      elif selection == '6':
          
        global totalPartidas
        global pc
        global pl
        global em
       
        global com_piedra
        global com_spock
        global com_papel
        global com_lagarto
        global com_tijeras
        global totalPartidas
        totalPartidas=pc+pl+em
        if totalPartidas==0:
            piedracom=0
            spockcom=0
            papelcom=0
            lagartocom=0
            tijerascom=0
            piedrapl=0
            spockpl=0
            papelpl=0
            lagartopl=0
            tijeraspl=0
        else:
            
            ####### Variables Para el porcentaje de la PC
            totalcom=com_piedra+com_spock+com_papel+com_lagarto+com_tijeras #Representa el divisor para el porcentataje de la COM
            piedracom=com_piedra/totalcom*100 # Porcentaje calculado para piedra
            spockcom=com_spock/totalcom*100 #Porcentaje callculado para spock
            papelcom=com_papel/totalcom*100 #Porcentaje calculado para papel
            lagartocom=com_lagarto/totalcom*100 # Porcentae calculado para lagarto
            tijerascom=com_tijeras/totalcom*100 # Porcentaje calculado para tijeras
            
            ###### Variables Para el porcentaje de Jugador
            totalpl=player_piedra+player_spock+player_papel+player_lagarto+player_tijeras #Representa el divisor para el porcentataje de Jugador
            piedrapl=player_piedra/totalpl*100 # Porcentaje calculado para piedra
            spockpl=player_spock/totalpl*100 #Porcentaje callculado para spock
            papelpl=player_papel/totalpl*100 #Porcentaje calculado para papel
            lagartopl=player_lagarto/totalpl*100 # Porcentae calculado para lagarto
            tijeraspl=player_tijeras/totalpl*100  # Porcentaje calculado para tijera
        print("==========================================================")

        print('MARCADOR FINALL!!:'+ans+ ': '+str(pl)+' COM : '+str(pc)+'\n'+'Total de rondas fueron: '+str(totalPartidas)+'\nGanadas por COM: '+ str(pc) + '\n' +'Veces Empate'+': '+ str(em)+ '\n' +'Ganadas por '+ans+' : '+ str(pl))

        if pc>pl:
            print('EL GANADOR ES COM SUERTE PARA LA PROXIMA '+ans)
        elif pc==pl:
            print('VAYA HA HABIDO UN EMPATE!!')
        else:
            print('FELICIDADES '+ans+' ERES EL REY EN PIEDRA,PAPEL,TIJERA,LAGARTO,SPOCK')
            
        print()
        print("***********************************************************")
        print("-----------------Registro De Armas-------------------------")
        print()
        print('Veces usadas por ',ans,':')
        print()
        print('Piedra:',player_piedra,' %:'+str(piedrapl))
        print('Spock:', player_spock, '%: '+str(spockpl))
        print('Papel:', player_papel,'%: '+str(papelpl))
        print('Lagarto:',player_lagarto,'%: '+str(lagartopl))
        print('Tijeras:',player_tijeras,'%: '+str(tijeraspl))
        print()
        print('*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*')

        print('Veces usadas por Com:')
        print('Piedra:',com_piedra,' %:'+str(piedracom))
        print('Spock:',com_spock, '%: '+str(spockcom))
        print('Papel:',com_papel,'%: '+str(papelcom))
        print('Lagarto:',com_lagarto,'%: '+str(lagartocom))
        print('Tijeras:',com_tijeras,'%: '+str(tijerascom))

        print('================================\n')
        ans1 = input('Deseas jugar de nuevo'+'\n Jugar ( J ) \n Salir  ( ALGUNA TECLA )\n')
        if ans1=='J':
            pc = 0 
            pl = 0
            em = 0
            totalPartidas=0 
            #Contadores de cuantas veces el jugador Y COM a usado un arma
            player_piedra = 0 
            player_spock = 0
            player_papel = 0
            player_lagarto = 0
            player_tijeras = 0
            com_piedra = 0
            com_spock = 0
            com_papel = 0
            com_lagarto = 0
            com_tijeras = 0
            ##############################
            listapl=[]
            listacom=[]
            contador=0
            anteriorpl=int
            anteriorcom=int
            difference=int
        
            main()
        else:
            sys.exit()
      else: 
        print ("No elegiste bien!")



##################################################################
        #### Jugar Nivel 5:
def jugar5(nivel):
    global player_piedra
    global player_spock
    global player_papel
    global player_lagarto
    global player_tijeras
    

        
    menu = {}
    menu['1']="piedra" 
    menu['2']="spock"
    menu['3']="papel"
    menu['4']="lagarto"
    menu['5']="tijeras"
    menu['6']="salir"
    while True:
      global ans
      options=menu.keys()
      
      for entry in sorted(options): 
        print (entry, menu[entry])

      selection=input("Selecciona alguno "+ans+":") 

      if selection =='1':
          player_piedra=player_piedra+1
          Nivel5 ("piedra")
      elif selection == '2':
          player_spock=player_spock+1
          Nivel5 ("spock")
      elif selection == '3':
          player_papel = player_papel+1
          Nivel5 ("papel") 
      elif selection == '4':
          player_lagarto =player_lagarto+1
          Nivel5 ("lagarto")
      elif selection == '5':
          player_tijeras =player_tijeras+1
          Nivel5 ("tijeras")
      elif selection == '6':
          
        global totalPartidas
        global pc
        global pl
        global em
       
        global com_piedra
        global com_spock
        global com_papel
        global com_lagarto
        global com_tijeras
        global totalPartidas
        totalPartidas=pc+pl+em
        if totalPartidas==0:
            piedracom=0
            spockcom=0
            papelcom=0
            lagartocom=0
            tijerascom=0
            piedrapl=0
            spockpl=0
            papelpl=0
            lagartopl=0
            tijeraspl=0
        else:
            
            ####### Variables Para el porcentaje de la PC
            totalcom=com_piedra+com_spock+com_papel+com_lagarto+com_tijeras #Representa el divisor para el porcentataje de la COM
            piedracom=com_piedra/totalcom*100 # Porcentaje calculado para piedra
            spockcom=com_spock/totalcom*100 #Porcentaje callculado para spock
            papelcom=com_papel/totalcom*100 #Porcentaje calculado para papel
            lagartocom=com_lagarto/totalcom*100 # Porcentae calculado para lagarto
            tijerascom=com_tijeras/totalcom*100 # Porcentaje calculado para tijeras
            
            ###### Variables Para el porcentaje de Jugador
            totalpl=player_piedra+player_spock+player_papel+player_lagarto+player_tijeras #Representa el divisor para el porcentataje de Jugador
            piedrapl=player_piedra/totalpl*100 # Porcentaje calculado para piedra
            spockpl=player_spock/totalpl*100 #Porcentaje callculado para spock
            papelpl=player_papel/totalpl*100 #Porcentaje calculado para papel
            lagartopl=player_lagarto/totalpl*100 # Porcentae calculado para lagarto
            tijeraspl=player_tijeras/totalpl*100  # Porcentaje calculado para tijera
        print("==========================================================")

        print('MARCADOR FINALL!!:'+ans+ ': '+str(pl)+' COM : '+str(pc)+'\n'+'Total de rondas fueron: '+str(totalPartidas)+'\nGanadas por COM: '+ str(pc) + '\n' +'Veces Empate'+': '+ str(em)+ '\n' +'Ganadas por '+ans+' : '+ str(pl))

        if pc>pl:
            print('EL GANADOR ES COM SUERTE PARA LA PROXIMA '+ans)
        elif pc==pl:
            print('VAYA HA HABIDO UN EMPATE!!')
        else:
            print('FELICIDADES '+ans+' ERES EL REY EN PIEDRA,PAPEL,TIJERA,LAGARTO,SPOCK')
            
        print()
        print("***********************************************************")
        print("-----------------Registro De Armas-------------------------")
        print()
        print('Veces usadas por ',ans,':')
        print()
        print('Piedra:',player_piedra,' %:'+str(piedrapl))
        print('Spock:', player_spock, '%: '+str(spockpl))
        print('Papel:', player_papel,'%: '+str(papelpl))
        print('Lagarto:',player_lagarto,'%: '+str(lagartopl))
        print('Tijeras:',player_tijeras,'%: '+str(tijeraspl))
        print()
        print('*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*')

        print('Veces usadas por Com:')
        print('Piedra:',com_piedra,' %:'+str(piedracom))
        print('Spock:',com_spock, '%: '+str(spockcom))
        print('Papel:',com_papel,'%: '+str(papelcom))
        print('Lagarto:',com_lagarto,'%: '+str(lagartocom))
        print('Tijeras:',com_tijeras,'%: '+str(tijerascom))

        print('================================\n')
        ans1 = input('Deseas jugar de nuevo'+'\n Jugar ( J ) \n Salir  ( ALGUNA TECLA )\n')
        if ans1=='J':
            pc = 0 
            pl = 0
            em = 0
            totalPartidas=0 
            #Contadores de cuantas veces el jugador Y COM a usado un arma
            player_piedra = 0 
            player_spock = 0
            player_papel = 0
            player_lagarto = 0
            player_tijeras = 0
            com_piedra = 0
            com_spock = 0
            com_papel = 0
            com_lagarto = 0
            com_tijeras = 0
            ##############################
            listapl=[]
            listacom=[]
            contador=0
            anteriorpl=int
            anteriorcom=int
            difference=int
        
            main()
        else:
            sys.exit()
      else: 
        print ("No elegiste bien!")




##################################################

##### Funcion Nivel:
        #NIVEL 1
def rpsls(arma):   
    global pc
    global pl
    global em
    global player_piedra
    global player_spock
    global player_papel
    global player_lagarto
    global player_tijeras
    global com_piedra
    global com_spock
    global com_papel
    global com_lagarto
    global com_tijeras
    global lista
    global mayores
    global contador
    global ans
    
    # Convertir arma a numero  usando arma_a_numero
    arma_jugador= arma_a_numero(arma)
    
    # calcularal azar para comp_number usando random.randrange ()
    comp_number=random.randrange(0,5)
    
    if comp_number==0:
        com_piedra=com_piedra+1
    elif comp_number==1:
        com_spock=com_spock+1
    elif comp_number==2:
        com_papel=com_papel+1
    elif comp_number==3:
        com_lagarto=com_lagarto+1
    elif comp_number==4:
        com_tijeras=com_tijeras+1
        
    # calcular la diferencia de player_number y comp_number modulo cinco 
    difference=(arma_jugador-comp_number)%5  
  
    # use if/elif/else para determinar el ganador 
    if difference==0:
        em = em + 1
        results='Empate!! Marcador:\n' +'Ganadas por COM: '+ str(pc) + '\n' +'Veces Empate'+ ': '+str(em)+ '\n' +'Ganadas por '+ans+' : '+ str(pl)
        
        
    elif difference>=3:
        pc = pc + 1

        results='Gana la PC! Marcador:\n' +'Ganadas por COM: '+ str(pc) + '\n' +'Veces Empate'+': '+ str(em)+ '\n' +'Ganadas por '+ans+' : '+ str(pl)
        
    elif difference<=2:
        pl = pl + 1 
        results='Gana Jugador! Marcador:\n'  +'Ganadas por COM: '+ str(pc) + '\n' +'Veces Empate'+': '+ str(em)+ '\n' +'Ganadas por '+ans+' : '+ str(pl)
        
        
    # comp_number convertir a nombre usando numero_a_arma
    comp_name=numero_a_arma(comp_number)  
      
    # Imprimir resultados
    print('================================\n')  
    print(ans,"escoje "+arma)
    print("PC escoje "+comp_name)  
    print(results)
    totalPartidas = pc + pl + em
    print('================================\n')

    #########################################################################


    
#NIVEL 2:
def Nivel2(arma):
    global pc
    global pl
    global em
    global player_piedra
    global player_spock
    global player_papel
    global player_lagarto
    global player_tijeras
    global com_piedra
    global com_spock
    global com_papel
    global com_lagarto
    global com_tijeras
    global mayores
    global contador
    global ans
    # Convertir arma a numero  usando arma_a_numero
    arma_jugador= arma_a_numero(arma)
    
    # calcularal azar para comp_number usando random.randrange ()
    lista=[player_piedra,player_spock,player_papel,player_lagarto,player_tijeras]
    mayores=sorted(lista)
    mayores=mayores[4:2:-1]
    
    if player_piedra==mayores[0] or player_piedra==mayores[1]:
        contra=[1,2]
    else:
        ()
            
    if player_spock==mayores[0] or player_spock==mayores[1]:
        contra=contra+[2,3]
    else:
        ()
            
    if player_papel==mayores[0] or player_papel==mayores[1]:
        contra=contra+[3,4]
    else:
        ()
         
    if player_lagarto==mayores[0] or player_lagarto==mayores[1]:
        contra=contra+[0,4]
    else:
        ()
            
    if player_tijeras==mayores[0] or player_tijeras==mayores[1]:
        contra=contra+[0,1]
    else:
        ()
    contra=random.choice(contra)
    contra=int(contra)

    if contador<9:
        
        comp_number=random.randrange(0,5)
        contador=contador+1
    else:
        comp_number=contra
        
    
    if comp_number==0:
        com_piedra=com_piedra+1
    elif comp_number==1:
        com_spock=com_spock+1
    elif comp_number==2:
        com_papel=com_papel+1
    elif comp_number==3:
        com_lagarto=+1
    elif comp_number==4:
        com_tijeras=+1
                
    # calcular la diferencia de player_number y comp_number modulo cinco 
    difference=(arma_jugador-comp_number)%5  
  
    # use if/elif/else para determinar el ganador 
    if difference==0:
        em = em + 1
        results='Empate!! Marcador:\n' +'Ganadas por COM: '+ str(pc) + '\n' +'Veces Empate'+ ': '+str(em)+ '\n' +'Ganadas por '+ans+' : '+ str(pl)
        
        
    elif difference>=3:
        pc = pc + 1

        results='Gana la PC! Marcador:\n' +'Ganadas por COM: '+ str(pc) + '\n' +'Veces Empate'+': '+ str(em)+ '\n' +'Ganadas por '+ans+' : '+ str(pl)
        
    elif difference<=2:
        pl = pl + 1 
        results='Gana Jugador! Marcador:\n'  +'Ganadas por COM: '+ str(pc) + '\n' +'Veces Empate'+': '+ str(em)+ '\n' +'Ganadas por '+ans+' : '+ str(pl)
        
        
    # comp_number convertir a nombre usando numero_a_arma
    comp_name=numero_a_arma(comp_number)  
      
    # Imprimir resultados
    print('================================\n')  
    print(ans,"escoje "+arma)
    print("PC escoje "+comp_name)  
    print(results)
    totalPartidas = pc + pl + em
    print('================================\n')

################################################################################
# Nivel3:

def Nivel3(arma):   
    global pc
    global pl
    global em
    global player_piedra
    global player_spock
    global player_papel
    global player_lagarto
    global player_tijeras
    global com_piedra
    global com_spock
    global com_papel
    global com_lagarto
    global com_tijeras
    global lista
    global mayores
    global contador
    global ans
    global anteriorpl
    
    # Convertir arma a numero  usando arma_a_numero
    arma_jugador= arma_a_numero(arma)
    
    # calcularal azar para comp_number usando random.randrange ()
    if contador==0:
        comp_number=random.randrange(0,5)
        anteriorpl=arma_jugador
        contra=comp_number
    else :
        arma_jugador=anteriorpl
        if arma_jugador==0:
            contra=[2,3,4]
        elif arma_jugador==1:
            contra=[3,4,0]
        elif arma_jugador==2:
            contra=[4,0,1]
        elif arma_jugador==3:
             contra=[0,1,2]
        elif arma_jugador==4:
            contra=[1,2,3]
        contra=random.choice(contra)
        contra=int(contra)
        comp_number=contra
        arma_jugador= arma_a_numero(arma)
        anteriorpl=arma_jugador
    if comp_number==0:
        com_piedra=com_piedra+1
    elif comp_number==1:
        com_spock=com_spock+1
    elif comp_number==2:
        com_papel=com_papel+1
    elif comp_number==3:
        com_lagarto=com_lagarto+1
    elif comp_number==4:
        com_tijeras=com_tijeras+1
        
    # calcular la diferencia de player_number y comp_number modulo cinco 
    difference=(arma_jugador-comp_number)%5  
    contador=contador+1
    # use if/elif/else para determinar el ganador 
    if difference==0:
        em = em + 1
        results='Empate!! Marcador:\n' +'Ganadas por COM: '+ str(pc) + '\n' +'Veces Empate'+ ': '+str(em)+ '\n' +'Ganadas por '+ans+' : '+ str(pl)
        
        
    elif difference>=3:
        pc = pc + 1

        results='Gana la PC! Marcador:\n' +'Ganadas por COM: '+ str(pc) + '\n' +'Veces Empate'+': '+ str(em)+ '\n' +'Ganadas por '+ans+' : '+ str(pl)
        
    elif difference<=2:
        pl = pl + 1 
        results='Gana Jugador! Marcador:\n'  +'Ganadas por COM: '+ str(pc) + '\n' +'Veces Empate'+': '+ str(em)+ '\n' +'Ganadas por '+ans+' : '+ str(pl)
        
        
    # comp_number convertir a nombre usando numero_a_arma
    comp_name=numero_a_arma(comp_number)  
      
    # Imprimir resultados
    print('================================\n')  
    print(ans,"escoje "+arma)
    print("PC escoje "+comp_name)  
    print(results)
    totalPartidas = pc + pl + em
    print('================================\n')



###############################################
    #  Nivel 4:
def Nivel4(arma):   
    global pc
    global pl
    global em
    global player_piedra
    global player_spock
    global player_papel
    global player_lagarto
    global player_tijeras
    global com_piedra
    global com_spock
    global com_papel
    global com_lagarto
    global com_tijeras
    global lista
    global mayores
    global contador
    global ans
    global anteriorpl
    global anteriorcom
    global difference
    
    # Convertir arma a numero  usando arma_a_numero
    arma_jugador= arma_a_numero(arma)
    
    # calcularal azar para comp_number usando random.randrange ()
    if contador==0:
        comp_number=random.randrange(0,5)
        difference=(arma_jugador-comp_number)%5
        anteriorpl=arma_jugador
        anteriorcom=comp_number
    if contador>0:
        if difference==0 or difference<=2:
            arma_jugador=anteriorpl
            if arma_jugador==0:
               contra=[1,2]
            elif arma_jugador==1:
                contra=[2,3]
            elif arma_jugador==2:
                contra=[3,4]
            elif arma_jugador==3:
                contra=[0,4]
            elif arma_jugador==4:
                 contra=[1,0]
        
            
            
        elif difference>=3:
            if anteriorcom==1:
                contra=[4]
            elif anteriorcom==2:
                contra=[0]
            elif anteriorcom==3:
                contra=[1]
            elif anteriorcom==4:
                contra=[]
            elif anteriorcom==0:
                contra=[3]
                
        contra=random.choice(contra)
        contra=int(contra)
        comp_number=contra
        arma_jugador= arma_a_numero(arma)
        difference=(arma_jugador-comp_number)%5
        anteriorpl=arma_jugador
        anteriorcom=comp_number

    if comp_number==0:
        com_piedra=com_piedra+1
    elif comp_number==1:
        com_spock=com_spock+1
    elif comp_number==2:
        com_papel=com_papel+1
    elif comp_number==3:
        com_lagarto=com_lagarto+1
    elif comp_number==4:
        com_tijeras=com_tijeras+1
        
    # calcular la diferencia de player_number y comp_number modulo cinco 
    difference=(arma_jugador-comp_number)%5  
    contador=contador+1
    # use if/elif/else para determinar el ganador 
    if difference==0:
        em = em + 1
        results='Empate!! Marcador:\n' +'Ganadas por COM: '+ str(pc) + '\n' +'Veces Empate'+ ': '+str(em)+ '\n' +'Ganadas por '+ans+' : '+ str(pl)
        
        
    elif difference>=3:
        pc = pc + 1

        results='Gana la PC! Marcador:\n' +'Ganadas por COM: '+ str(pc) + '\n' +'Veces Empate'+': '+ str(em)+ '\n' +'Ganadas por '+ans+' : '+ str(pl)
        
    elif difference<=2:
        pl = pl + 1 
        results='Gana Jugador! Marcador:\n'  +'Ganadas por COM: '+ str(pc) + '\n' +'Veces Empate'+': '+ str(em)+ '\n' +'Ganadas por '+ans+' : '+ str(pl)
        
        
    # comp_number convertir a nombre usando numero_a_arma
    comp_name=numero_a_arma(comp_number)  
      
    # Imprimir resultados
    print('================================\n')  
    print(ans,"escoje "+arma)
    print("PC escoje "+comp_name)  
    print(results)
    totalPartidas = pc + pl + em
    print('================================\n')

#################################################################################
    #### NIVEL 5:
def Nivel5(arma):   
    global pc
    global pl
    global em
    global player_piedra
    global player_spock
    global player_papel
    global player_lagarto
    global player_tijeras
    global com_piedra
    global com_spock
    global com_papel
    global com_lagarto
    global com_tijeras
    global mayores
    global contador
    global ans
    global anteriorpl
    global anteriorcom
    global difference
    
    # Convertir arma a numero  usando arma_a_numero
    arma_jugador= arma_a_numero(arma)
    lista=[player_piedra,player_spock,player_papel,player_lagarto,player_tijeras]
    mayores=sorted(lista)
    mayores=mayores[-1] #Guardo arma favorita 
    mayores=int(mayores)
    # calcularal azar para comp_number usando random.randrange ()

    if player_piedra==mayores:
        contra=[1,2]
    else:
        ()
            
    if player_spock==mayores:
        contra=[2,3]
    else:
        ()
            
    if player_papel==mayores:
        contra=[3,4]
    else:
        ()
         
    if player_lagarto==mayores:
        contra=[0,4]
    else:
        ()
            
    if player_tijeras==mayores:
        contra=[0,1]
    else:
        ()
    contra=random.choice(contra)
    contra=int(contra)
    
    if contador%10==0: # asignado cada 10 turnos
        comp_number=1
                    
    elif contador%5==0:
        comp_number=contra

    elif contador%5!=0:
        comp_number=random.randrange(0,5)
        # Sumatorias   
    if comp_number==0:
        com_piedra=com_piedra+1
    elif comp_number==1:
        com_spock=com_spock+1
    elif comp_number==2:
        com_papel=com_papel+1
    elif comp_number==3:
        com_lagarto=com_lagarto+1
    elif comp_number==4:
        com_tijeras=com_tijeras+1
    
    # calcular la diferencia de player_number y comp_number modulo cinco 
    difference=(arma_jugador-comp_number)%5  
    contador=contador+1
    # use if/elif/else para determinar el ganador 
    if difference==0:
        em = em + 1
        results='Empate!! Marcador:\n' +'Ganadas por COM: '+ str(pc) + '\n' +'Veces Empate'+ ': '+str(em)+ '\n' +'Ganadas por '+ans+' : '+ str(pl)
        
        
    elif difference>=3:
        pc = pc + 1

        results='Gana la PC! Marcador:\n' +'Ganadas por COM: '+ str(pc) + '\n' +'Veces Empate'+': '+ str(em)+ '\n' +'Ganadas por '+ans+' : '+ str(pl)
        
    elif difference<=2:
        pl = pl + 1 
        results='Gana Jugador! Marcador:\n'  +'Ganadas por COM: '+ str(pc) + '\n' +'Veces Empate'+': '+ str(em)+ '\n' +'Ganadas por '+ans+' : '+ str(pl)
        
        
    # comp_number convertir a nombre usando numero_a_arma
    comp_name=numero_a_arma(comp_number)  
      
    # Imprimir resultados
    print('================================\n')  
    print(ans,"escoje "+arma)
    print("PC escoje "+comp_name)  
    print(results)
    totalPartidas = pc + pl + em
    print('================================\n')


################################################################################
import sys

# funcion principal
def main():
    global ans
    ans = input("Bienvenido : Digite su nombre de usuario\n")

    print()
    #rpsls("piedra")
    ans1 = input('Bienvenido ' +ans+ '\n Jugar ( J ) \n Instrucciones ( I ) \n Salir  ( S )\n')

    if ans1=="J":

      nivel = {}
      nivel['1']="Para Nivel 1"
      nivel['2']="Para Nivel 2"
      nivel['3']="Para Nivel 3"
      nivel['4']="Para Nivel 4"
      nivel['5']="Para Nivel 5"

      
      while True:
          options=nivel.keys()
        
          for entry in sorted(options): 
            print (entry, nivel[entry])


          selection=input('Hola ' + ans + ' Seleccione alguno:') 
          if selection =='1':
              jugar(nivel)
          elif selection=='2':
              jugar2(nivel)
          elif selection=='3':
              jugar3(nivel)
          elif selection=='4':
              jugar4(nivel)
          elif selection=='5':
              jugar5 (nivel)
      
    elif ans1=="I":
      print("""Reglas del juego 
El objetivo de piedra-papel-tijeras-lagarto-Spock es derrotar al contrincante por medio de la selección de un arma que derrote al arma escogida por el oponente siguiendo las siguientes reglas:  
GANADOR ACCION PERDEDOR
Tijera decapita Lagarto
Tijera corta Papel
Papel tapa Piedra
Papel desautoriza Spock
Piedra lapida Lagarto
Piedra aplasta Tijera
Lagarto come Papel
Lagarto envenena Spock
Spock vaporiza Piedra
Spock rompe Tijera""")
      main()
    elif ans1=="S":
        print('Hasta Pronto')
        sys.exit("S")
    else:
       print("\n No valido")
       main()
        
main()
