# Importamos los tipos de datos List y Tuple de la biblioteca typing para las anotaciones de tipo, y Counter de la biblioteca collections para contar elementos.
from typing import List, Tuple
import json
from collections import Counter

# Definimos una función llamada q3_memory que toma la ruta del archivo como entrada y devuelve una lista de tuplas que contienen usernames y su recuento.
def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    # Creamos un diccionario para almacenar los usuarios mencionados y su recuento.
    usuarios_recuento = {}

    # Abrimos el archivo en modo de lectura.
    with open(file_path, 'r') as archivo:
        # Iteramos sobre cada línea del archivo.
        for linea in archivo:
            # Cargamos la línea como un objeto JSON.
            datos = json.loads(linea)
            # Obtenemos la lista de usuarios mencionados.
            usuarios_mencionados = datos.get('mentionedUsers')
            # Si hay usuarios mencionados, los procesamos.
            if usuarios_mencionados:
                # Iteramos sobre cada usuario mencionado.
                for usuario in usuarios_mencionados:
                    # Obtenemos el nombre de usuario.
                    nombre_usuario = usuario.get('username')
                    # Actualizamos el contador para este usuario.
                    usuarios_recuento[nombre_usuario] = usuarios_recuento.get(nombre_usuario, 0) + 1

    # Ordenamos el diccionario por el recuento de usuarios mencionados en orden descendente.
    usuarios_ordenados = sorted(usuarios_recuento.items(), key=lambda x: x[1], reverse=True)
    
    # Devolvemos los 10 usuarios más mencionados como una lista de tuplas.
    return usuarios_ordenados[:10]

# Llamamos a la función q3_memory con el archivo especificado y mostramos el resultado.
tiempo_inicial = time()
resultado = q3_memory(file_path=file_path)
print(f"Tiempo de ejecución: {time() - tiempo_inicial} ")
print(resultado)