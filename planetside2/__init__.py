import requests
from flask import Flask, make_response

app = Flask(__name__)


@app.route('/character/<character_id>')
def get_character(character_id):
    fields = ["name.first", "creation_date", "battle_rank", "certs.earned_points"]
    resp = requests.get('http://census.daybreakgames.com/get/ps2:v2/character/?character_id={}&c:show={}'.format(
        character_id, ','.join(fields)))

    return make_response('\n'.join(["Name : {}, Rank : {}".format(
        character['name']['first'], character['battle_rank']['value']
    ) for character in resp.json()['character_list']]))

if __name__ == '__main__':
    app.run(debug=True)
