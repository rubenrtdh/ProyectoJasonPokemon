import json

# Cargar el archivo JSON con la información de los Pokémon
with open('pokemon_platino.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

def calcular_media_estadisticas(pokemon):
    total_stats = sum(pokemon['estadisticas_base'].values())
    return total_stats / len(pokemon['estadisticas_base'])

def listar_pokemon():
    print("Lista de Pokémon en Pokémon Platino:")
    for pokemon in data["pokemon_platino"]:
        print(f"Nombre: {pokemon['nombre']}")
        print(f"Tipo: {', '.join(pokemon['tipo'])}")
        print(f"Habilidades: {', '.join(pokemon['habilidades'])}")
        print()

def contar_pokemon_por_tipo():
    tipos = {}
    for pokemon in data["pokemon_platino"]:
        for tipo in pokemon['tipo']:
            tipos[tipo] = tipos.get(tipo, 0) + 1
    print("Cantidad de Pokémon por tipo:")
    for tipo, count in tipos.items():
        print(f"Tipo: {tipo}, Cantidad: {count}")

def buscar_pokemon_por_tipo(tipo_buscado):
    print(f"Lista de Pokémon de tipo '{tipo_buscado}' en Pokémon Platino:")
    for pokemon in data["pokemon_platino"]:
        if tipo_buscado in pokemon['tipo']:
            print(f"Nombre: {pokemon['nombre']}")
            print(f"Tipo: {', '.join(pokemon['tipo'])}")
            print(f"Habilidades: {', '.join(pokemon['habilidades'])}")
            print()

def buscar_pokemon_por_nombre(nombre):
    print(f"Información de Pokémon '{nombre}' en Pokémon Platino:")
    for pokemon in data["pokemon_platino"]:
        if pokemon['nombre'].lower() == nombre.lower():
            print(f"Tipo: {', '.join(pokemon['tipo'])}")
            print(f"Habilidades: {', '.join(pokemon['habilidades'])}")
            print(f"Estadísticas Base:")
            for stat, value in pokemon['estadisticas_base'].items():
                print(f" - {stat}: {value}")
            return
    print("El Pokémon no se encontró en la lista.")

def buscar_pokemon_por_estadisticas(rango_min, rango_max):
    print(f"Lista de Pokémon cuyas estadísticas están dentro del rango [{rango_min}, {rango_max}] en Pokémon Platino:")
    found_pokemon = False
    for pokemon in data["pokemon_platino"]:
        media_estadisticas = calcular_media_estadisticas(pokemon)
        if rango_min <= media_estadisticas <= rango_max:
            if not found_pokemon:
                print(f"Nombre\t\tTipo\t\t\tHabilidades\t\tEstadísticas Base")
                found_pokemon = True
            print(f"{pokemon['nombre']}\t\t{', '.join(pokemon['tipo'])}\t\t{', '.join(pokemon['habilidades'])}\t\t{', '.join([f'{s}: {v}' for s, v in pokemon['estadisticas_base'].items()])}")
    if not found_pokemon:
        print("No se encontraron Pokémon dentro del rango especificado.")

def main():
    print("Bienvenido al Pokedex de Pokémon Platino")
    print("1. Listar todos los Pokémon")
    print("2. Contar Pokémon por tipo")
    print("3. Buscar Pokémon por tipo")
    print("4. Buscar información detallada de un Pokémon por nombre")
    print("5. Buscar Pokémon por estadísticas")
    print("6. Salir")

    while True:
        opcion = input("Seleccione una opción (1-6): ")
        if opcion == '1':
            listar_pokemon()
        elif opcion == '2':
            contar_pokemon_por_tipo()
        elif opcion == '3':
            tipo_buscado = input("Introduce el tipo de Pokémon a buscar: ")
            buscar_pokemon_por_tipo(tipo_buscado)
        elif opcion == '4':
            nombre_buscado = input("Introduce el nombre del Pokémon a buscar: ")
            buscar_pokemon_por_nombre(nombre_buscado)
        elif opcion == '5':
            rango_min = float(input("Introduce el valor mínimo del rango de media de estadísticas: "))
            rango_max = float(input("Introduce el valor máximo del rango de media de estadísticas: "))
            buscar_pokemon_por_estadisticas(rango_min, rango_max)
        elif opcion == '6':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida (1-6).")

if __name__ == "__main__":
    main()
