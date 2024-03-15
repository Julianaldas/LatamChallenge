# Importamos los tipos de datos List y Tuple de la biblioteca typing para las anotaciones de tipo.
from typing import List, Tuple
import json
from emoji import emoji_list
from collections import Counter

# Definimos una función llamada q2_time que toma la ruta del archivo como entrada y devuelve una lista de tuplas que contienen emojis y su recuento.
def q2_time(file_path: str) -> List[Tuple[str, int]]:
    # Primero, se obtienen todos los objetos de tweets de una vez.
    with open(file_path, 'r') as f:
        tweets = f.readlines()

    # Luego se obtiene un gran string que contenga todos los contenidos de los tweets.
    all_content = ""
    for tweet in tweets:
        all_content += json.loads(tweet)['content']
    
    # Usando el método emoji_list, se analiza todo el string y se obtienen todos los emojis presentes.
    emojis = [emoji['emoji'] for emoji in emoji_list(all_content)]

    # Se cuentan los emojis y se devuelven los 10 más utilizados.
    top_emojis = Counter(emojis).most_common(10)
    return top_emojis

# El siguiente código llama a la función q2_time con un archivo especificado y muestra el resultado.
initial_time = time()
result = q2_time(file_path=file_path)
print(f"Tiempo de ejecución: {time() - initial_time} ")
print(result)