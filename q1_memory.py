# Importamos los tipos de datos List y Tuple de la biblioteca typing para las anotaciones de tipo.
# También importamos la clase datetime de la biblioteca datetime para trabajar con fechas y horas.
# Luego importamos el módulo json para trabajar con datos JSON y defaultdict de la biblioteca collections para crear diccionarios con valores predeterminados.
from typing import List, Tuple
from datetime import datetime
import json
from collections import defaultdict

# Definimos una función llamada q1_memory que toma la ruta del archivo como entrada y devuelve una lista de tuplas que contienen fechas y usuarios.
def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    # Creamos un defaultdict anidado para almacenar el recuento de tweets por usuario y fecha.
    dates_counter = defaultdict(lambda: defaultdict(int))
    # Abrimos el archivo JSON en modo de lectura.
    with open(file_path, 'r') as file:
        # Iteramos línea por línea en el archivo.
        for line in file:
            # Cargamos cada línea como un objeto JSON.
            tweet = json.loads(line)
            # Extraemos la fecha del tweet y la convertimos al formato deseado.
            tweet_date = tweet['date'].split('T')[0]
            # Extraemos el nombre de usuario del tweet.
            username = tweet['user']['username']
            # Actualizamos el contador de tweets para este usuario en esta fecha.
            dates_counter[tweet_date][username] += 1
    
    # Ordenamos las fechas según el número total de tweets (usuarios únicos) publicados ese día.
    top_dates = sorted(dates_counter.keys(), key=lambda x: sum(dates_counter[x].values()), reverse=True)[:10]
    
    # Obtenemos el usuario con más tweets para cada una de las fechas principales.
    top_users = [max(dates_counter[date], key=dates_counter[date].get) for date in top_dates]

    # Convertimos las fechas de cadena a objetos datetime.date().
    top_dates = [datetime.strptime(date_str, "%Y-%m-%d").date() for date_str in top_dates]
    
    # Combinamos las fechas y los usuarios en una lista de tuplas y la devolvemos.
    return list(zip(top_dates, top_users))

# El siguiente código llama a la función q1_memory con un archivo especificado y muestra el resultado.
initial_time = time()
result = q1_memory(file_path=file_path)
print(f"Tiempo de ejecución: {time() - initial_time} ")
print(result)