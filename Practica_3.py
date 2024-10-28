# -*- coding: utf-8 -*-
"""

@author: jared
"""
import random

# Lista de personajes históricos con sus atributos
personajes = [
    {"nombre": "Albert Einstein", "género": "masculino", "profesión": "científico", "continente": "Europa"},
    {"nombre": "Cleopatra", "género": "femenino", "profesión": "líder", "continente": "África"},
    {"nombre": "Genghis Khan", "género": "masculino", "profesión": "líder", "continente": "Asia"},
    {"nombre": "Marie Curie", "género": "femenino", "profesión": "científico", "continente": "Europa"},
    {"nombre": "Simón Bolívar", "género": "masculino", "profesión": "líder", "continente": "América"},
    {"nombre": "Joan of Arc", "género": "femenino", "profesión": "líder", "continente": "Europa"},
    {"nombre": "Frida Kahlo", "género": "femenino", "profesión": "artista", "continente": "América"},
    {"nombre": "Leonardo da Vinci", "género": "masculino", "profesión": "artista", "continente": "Europa"},
    {"nombre": "Mozart", "género": "masculino", "profesión": "músico", "continente": "Europa"},
    {"nombre": "Nelson Mandela", "género": "masculino", "profesión": "líder", "continente": "África"},
    {"nombre": "Socrates", "género": "masculino", "profesión": "filósofo", "continente": "Europa"},
    {"nombre": "Diego Rivera", "género": "masculino", "profesión": "artista", "continente": "América"},
    {"nombre": "Fela Kuti", "género": "masculino", "profesión": "músico", "continente": "África"},
    {"nombre": "Avicena (Ibn Sina)", "género": "masculino", "profesión": "filósofo", "continente": "Asia"},

]

# Selecciona aleatoriamente el personaje secreto
personaje_secreto = random.choice(personajes)

# Posibles preguntas y cómo filtran la lista
preguntas = {
    1: {"pregunta": "¿Es masculino?", "atributo": "género", "valor": "masculino"},
    2: {"pregunta": "¿Es femenino?", "atributo": "género", "valor": "femenino"},
    3: {"pregunta": "¿Es científico?", "atributo": "profesión", "valor": "científico"},
    4: {"pregunta": "¿Es líder?", "atributo": "profesión", "valor": "líder"},
    5: {"pregunta": "¿Es artista?", "atributo": "profesión", "valor": "artista"},
    6: {"pregunta": "¿Es músico?", "atributo": "profesión", "valor": "músico"},
    7: {"pregunta": "¿Es filósofo?", "atributo": "profesión", "valor": "filósofo"},
    8: {"pregunta": "¿Es de Asia?", "atributo": "continente", "valor": "Asia"},
    9: {"pregunta": "¿Es de América?", "atributo": "continente", "valor": "América"},
    10: {"pregunta": "¿Es de África?", "atributo": "continente", "valor": "África"},
    11: {"pregunta": "¿Es de Europa?", "atributo": "continente", "valor": "Europa"}
}

# Filtrar personajes con base en una pregunta
def filtrar_personajes(lista, atributo, valor):
    return [p for p in lista if p[atributo] == valor]

# Función principal del juego
def jugar_adivina_quien():
    personajes_restantes = personajes.copy()
    intentos = 5  # Número de preguntas disponibles para el jugador

    print("Bienvenido al juego de 'Adivina Quién - Personajes Históricos'")
    print("Trata de adivinar el personaje secreto haciendo preguntas.\n")

    while intentos > 0 and len(personajes_restantes) > 1:
        print(f"\nPersonajes restantes: {len(personajes_restantes)}")
        print("Preguntas disponibles:")
        for num, datos in preguntas.items():
            print(f"{num}. {datos['pregunta']}")

        # Obtener la pregunta del usuario
        try:
            eleccion = int(input(f"\nEscoge una pregunta (1-{len(preguntas)}): "))
            if eleccion not in preguntas:
                raise ValueError("Selección inválida. Intenta de nuevo.")
        except ValueError:
            print("Entrada no válida. Escoge un número de la lista.")
            continue

        # Filtrar la lista según la pregunta seleccionada
        pregunta_seleccionada = preguntas[eleccion]
        personajes_restantes = filtrar_personajes(
            personajes_restantes, 
            pregunta_seleccionada["atributo"], 
            pregunta_seleccionada["valor"]
        )
        
        # Retroalimentación para el usuario
        print(f"\nRespuesta a '{pregunta_seleccionada['pregunta']}': Sí")
        intentos -= 1

        # Verificar si se ha reducido a un solo personaje
        if len(personajes_restantes) == 1:
            print(f"\n¡Adivinaste! El personaje secreto es {personajes_restantes[0]['nombre']}.")
            return
        elif len(personajes_restantes) == 0:
            print("\nNo quedan personajes que coincidan con tus preguntas. Has perdido.")
            return

    # Resultado si no adivina en los intentos permitidos
    if len(personajes_restantes) > 1:
        print(f"\nNo lograste adivinar en los intentos permitidos. El personaje era: {personaje_secreto['nombre']}")

# Ejecutar el juego
if __name__ == "__main__":
    jugar_adivina_quien()
