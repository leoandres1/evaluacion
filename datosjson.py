import json
from datetime import datetime

ruta_archivo = '/home/devasc/labs/devnet-src/parsing/myfile.json'


with open(ruta_archivo, 'r') as ourjson:

    json_file = json.load(ourjson)


print(json_file)

{
    "token": "mi_token",
    "caducidad": "2024-04-10T12:00:00Z"
}
