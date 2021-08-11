#funciones cotidianas

def ver_tv():
    print('Nunca hay nada bueno en este cable\n')

def cocinar():
    print('Vamos a preparar algo rico\n')

def comer():
    print('Miummm, que rico\n')
    
def chatear():
    print('Me dejo en visto :V\n')

def Ir_al_bano(a):
        if(a == 1):
            print('Hacer Pi Pi\n')
        elif(a == 2):
            print('Hacer Po Po ...\n')
        else:
            print('a que venia?\n')

def oir_musica(cancion):
    print('siempre me ah encantado oir {}'.format(cancion))

def main():
    while True:
        #menu
        print('Que te gustaria hacer hoy?')
        print('1. Oir Musica')
        print('2. Ver Tv')
        print('3. ir al bano')
        print('4. cocinar')
        print('5. comer')
        print('6. chatear')
        print('7. Salir')
        opcion = int(input('R:'))
        
        if(opcion == 1):
            oir_musica()
        elif(opcion == 2):
            ver_tv()
        elif(opcion == 3):
            accion = int(input('1. Pipi\n2. Popo'))
            Ir_al_bano(accion)
        elif(opcion == 4):
            cocinar()
        elif(opcion == 5):
            comer()
        elif(opcion == 6):
            chatear()
        elif(opcion == 7):
            print('saliendo')
            break
        else:
            print('La opcion no es valida\n')
        

if __name__ == "__main__":
    main()