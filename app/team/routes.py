from flask import Blueprint, render_template, request, redirect, url_for
from app.models import CreateTeam
import requests

from app.team.forms import CreateTeamForm
from flask_login import current_user, login_required

team = Blueprint('team', __name__, template_folder='teamtemplates')

from app.models import db

@team.route('/team/create', methods=['GET', 'POST'])
@login_required
def createTeam():
    form = CreateTeamForm()
    poke1 = ''
    poke2 = ''
    poke3 = ''
    poke4 = ''
    poke5 = ''
    poke6 = ''

    post = CreateTeam(poke1, poke2, poke3, poke4, poke5, poke6, current_user.id)
    
    
    db.session.add(post)
    db.session.commit()
    form=form 
    return redirect(url_for('home'))


# @team.route('/myteam')
# def getmyteam():
#     posts = CreateTeam.query.

@team.route('/myteam/<int:id>')
def viewteam(id):
    post = CreateTeam.query.get(id)
    print(post)
    return render_template('myteam.html', post=post)
    
# pokemon = {}
    # if request.method == 'POST':

    #     poke_name = user_id.poke1.data
    #     print(poke_name)
    #     url = f'https://pokeapi.co/api/v2/pokemon/{poke_name.lower()}'
    #     response = requests.get(url)
    #     if response.ok:
    #         data = response.json()
    #         pokemon = {
    #             'name': data['name'],
    #             'hp': data['stats'][0]['base_stat'],
    #             'ability': data['abilities'][0]['ability']['name'],
    #             'attack': data['stats'][1]['base_stat'],
    #             'defense': data['stats'][2]['base_stat'],
    #             'img': data['sprites']['front_default']
    #         }
    #         print(pokemon)
    # return render_template('myteam.html', post=post, pokemon=pokemon)

# @team.route('/team/catch')
# def catchpoke(poke):
#     if poke1 != '':
#     elif poke2 != '':
#     elif poke3 != '':
#     elif poke4 != '':
#     elif poke5 != '':
#     elif poke6 != '':
#     else:
#         print('team is full')