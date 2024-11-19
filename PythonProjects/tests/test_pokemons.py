import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '944890816359f3eae36547d12f152fa3'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '7844'




def test_status_code_trainers():
    responce = requests.get(url = f'{URL}/trainers')
    assert responce.status_code == 200

def test_part_of_responce():
    responce_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert responce_get.json()["data"][0]["trainer_name"] == 'MaryZhezhe'





    