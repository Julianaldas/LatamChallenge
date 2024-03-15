# Importamos los tipos de datos List y Tuple de la biblioteca typing para las anotaciones de tipo.
# También importamos la clase datetime de la biblioteca datetime para trabajar con fechas y horas.
# Luego importamos el módulo json para trabajar con datos JSON y defaultdict de la biblioteca collections para crear diccionarios con valores predeterminados.
from typing import List, Tuple
from datetime import datetime
import json
from collections import defaultdict

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:

    # Primero se guardan los datos de fecha y username en una lista de lista, para luego poder contarlos acordemente.
    with open(file_path, 'r') as f:
        data = [[json.loads(line)['date'].split('T')[0], json.loads(line)['user']['username']]  for line in f.readlines()]
    
    # Se utiliza la clase Counter() junto con list comprehension para obtener las 10 fechas mas comunes de todos los tweets.
    most_common_dates = Counter([d[0] for d in data]).most_common(10)

    # Se de manera similar, se obtiene el usuario que mas tweetió para cada una de las fechas mas comunes.
    most_common_users = [Counter([d[1] for d in data if d[0] == date[0]]).most_common(1)[0][0] for date in most_common_dates]

    # Se utiliza zip para agrupar las dos listas obtenidas anteriormente, recordando pasar la fecha a formato datetime.date().
    return list(zip([datetime.strptime(date[0], "%Y-%m-%d").date() for date in most_common_dates], most_common_users))
    from q1_time import q1_time

initial_time = time()
result = q1_time(file_path=file_path)
print(f"Tiempo de ejecución: {time() - initial_time} ")
print(result)