from app import app
from flask import render_template, request
from .forms import PokeFinderForm
import requests 

@app.route('/', methods=['GET', 'POST'])
def home():
    form = PokeFinderForm()
    pokemon = {}
    if request.method == 'POST':
        if form.validate():
            poke_name = form.name.data
            print(poke_name)
            url = f'https://pokeapi.co/api/v2/pokemon/{poke_name.lower()}'
            response = requests.get(url)
            if response.ok:
                data = response.json()
                pokemon = {
                    'name': data['name'],
                    'hp': data['stats'][0]['base_stat'],
                    'ability': data['abilities'][0]['ability']['name'],
                    'attack': data['stats'][1]['base_stat'],
                    'defense': data['stats'][2]['base_stat'],
                    'img': data['sprites']['front_default']
                }
                print(pokemon)
            else:
                print('That pokemon is invalid')
    return render_template('home.html', form=form, pokemon=pokemon)