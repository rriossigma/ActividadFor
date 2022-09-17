from multiprocessing.sharedctypes import Value
from typing import ValuesView


diccionario = {"Miguel"    :18,
"Edwin"        :23,
"Erick"        :28,
"Pedro"        :16,
"Pau"        :25,
"Liliana"    :20,
"Marco"        :25,
"Claudia"    :21,
"Roland"    :25,
"Gerardo"    :9 ,
"Jonathan"    :15,
"Paco"        :13,
"Yolanda"    :4 ,
"Julio"        :28,
"Victor"    :3 ,
"Gustavo"    :8 ,
"Paulina"    :25
}


for k, v in diccionario.items():
    print(k, v)

max_val=max(diccionario.values())
min_val=min(diccionario.values())

print("El mayor numero es: ", max_val)
print("El menor numero es: ",  min_val)
    