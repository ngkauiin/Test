from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('Ping! Ping! Pong! Pong!')

VISITORS = [
    {
        'id': uuid.uuid4().hex,
        'ID': '0',
        'name': 'Baxter',
        'visitTime': '19/01/2020',
        'favDrink': 'Cap',
        'purpose': 'Nothing'
    },
    {
        'id': uuid.uuid4().hex,
        'ID': '1',
        'name': 'Baxter son',
        'visitTime': '19/01/2020',
        'favDrink': 'Coke',
        'purpose': 'His father'
    }
]

@app.route('/visitor_log', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        VISITORS.append({
            'ID': post_data.get('ID'),
            'name': post_data.get('name'),
            'visitTime': post_data.get('visitTime'),
            'favDrink': post_data.get('favDrink'),
            'purpose': post_data.get('purpose')
        })
        response_object['message'] = 'Visitor added!'
    else:
        response_object['visitors'] = VISITORS
    return jsonify(response_object)

if __name__ == '__main__':
    app.run()
