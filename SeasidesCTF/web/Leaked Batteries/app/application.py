import os
import base64
import pickle

from flask import Flask, request, make_response, render_template
import pandas as pd

app = Flask(__name__)

FLAG = os.getenv('FLAG') or 'sea{delirious_deserialization}sides'

class PokeMash(object):
    """
        Handle pokemon name mashing
    """
    
    POKEMON_FILE_NAME = os.getenv('POKEMON_FILE_NAME') or 'poke_names.txt'
    POKEMON_NAME_LIST = [ name.rstrip() for name in open(POKEMON_FILE_NAME)]
    
    @property
    def names(self):
        return self.POKEMON_NAME_LIST

    def mash(self, name_list):
        validity_list = [name in self.names for name in name_list]
        if False in validity_list:
            return "INVALIDOMON!"

        return ''.join([ name[:len(name)//2] for name in name_list ])
    
    def export_mash(self, mashed_data):
        return base64.b64encode(pickle.dumps(mashed_data)).decode()

    def import_mash(self, exported_data):
        return pickle.loads(base64.b64decode(exported_data))
    
POKEMASHER = PokeMash()
    

@app.route('/', methods=['GET', 'POST'])
def index():
    data_dict = {
        'names': POKEMASHER.names
    }
    if request.method == 'GET':
        return render_template('index.html', data_dict=data_dict)
    if request.method == 'POST':
        name1 = request.form.get('name1')
        name2 = request.form.get('name2')

        name_list = [name1, name2]

        mashed_poke = POKEMASHER.mash(name_list)
        unique_string = POKEMASHER.export_mash(mashed_poke)

        data_dict.update({
            'mashed': mashed_poke,
            'unique_string': unique_string
        })

        return render_template('index.html', data_dict=data_dict)

@app.route('/import', methods=['POST'])
def import_mash_view():
    data_dict = {
        'names': POKEMASHER.names
    }
    if request.method == 'POST':
        try:
            unique_string = request.form.get('unique_string')
            mashed_poke = POKEMASHER.import_mash(unique_string)
        except:
            mashed_poke = 'INVALID INPUT'
            unique_string = ''
            
        data_dict.update({
            'mashed': mashed_poke,
            'unique_string': unique_string
        })

        return render_template('index.html', data_dict=data_dict)

if __name__ == '__main__':
    app.run(debug=True)