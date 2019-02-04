from flask import flask,jsonify

app = Flask(__name__)


stores = [
    {
        'name': 'My Store',
        'items': [
            {
            'name':'My Item'
            'price': 15.05
            }
        ]
    }
]


#POST
@app.route('/store', mothods=['POST'])
def create_store():
    pass

#GET
@app.route('/store/<string:name>')
def get_store(name):
    pass

#GET
@app.route('/store')
def get_stores():
    return jsonify({'stores':stores})


#POST
@app.route('/store/<string:name>/item', method=['POST'])
def create_item_in_store(name):
    pass


@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    pass
