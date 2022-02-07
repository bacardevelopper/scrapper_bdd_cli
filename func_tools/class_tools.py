from tinydb import TinyDB, Query

import requests
import string
import random

# config
path = 'bdd/db.json'
db = TinyDB(path)
User = Query()
salage = 7


class Tools:
    def __init__(self) -> None:
        pass

    def ajouter(self, data):
        cle_random = ''.join(random.choices(
            string.ascii_uppercase + string.digits, k=salage))
        db.insert({'cle': cle_random,  'data': data})
        print('| bien inserer |')

    def voir_tout(self,data):
        db.search()