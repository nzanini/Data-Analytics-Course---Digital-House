from clases.jugador import Jugador
from clases.enemigo import Enemigo
import random

def main():
    nombre_jugador = input("Bienvenido. Ingresa tu nombre: ")
    jugador = Jugador(nombre_jugador)

    enemigos = [
        Enemigo("Alien", 50, 10), 
        Enemigo("Robot", 30, 5), 
        Enemigo("Monstruo", 70, 15)
    ]

    #enemigos_derrotados = []

    print("Comenzamos!")

    while enemigos: # asi se corta cuando ya no haya enemigos
        enemigo_actual = random.choice(enemigos)
        #if enemigo_actual in enemigos_derrotados:
         #   continue

        print(f"Te encontraste con un {enemigo_actual.nombre}!")

        while enemigo_actual.salud > 0: # mientras el enemigo actual tengo salud, entra  al while (hay pelea)
            accion = input("Que queres hacer? (atacar/huir): ").lower() # asi lo toma en miniscula

            if accion == "atacar":
                dano_jugador = jugador.atacar()
                print(f"Atacaste al {enemigo_actual.nombre} y le causaste {dano_jugador} de dano")
                enemigo_actual.recibir_dano(dano_jugador)

                if enemigo_actual.salud > 0:
                    dano_enemigo = enemigo_actual.atacar()
                    print(f"El {enemigo_actual.nombre} te ataco y te causo {dano_enemigo} de dano")
                    jugador.recibir_dano(dano_enemigo)

            elif accion == "huir":
                print("Has decidido huir del combate")
                break # asi sale de la estructura actual, el segundo while

        if jugador.salud <= 0:
            print("Has perdido")
            break

        if enemigo_actual.salud <= 0:
            #enemigos_derrotados.append(enemigo_actual)
            enemigos.remove(enemigo_actual)

        jugador.ganar_experiencia(20)

        continuar = input("Queres seguir jugando? (s/n): ").lower()

        if continuar != "s":
            print("Gracias por jugar!")
            break

    if not enemigos:
        print("derrotaste a todos los enemigos!")

if __name__ == "__main__": # nos asegura que solo podremos ejecutar este script desde el programa princiapl
    main()

