from flask import Flask, jsonify, request

app = Flask(__name__)

# Define a list of items
items = ['item1', 'item2', 'item3']


# Define endpoint to retrieve all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)


# Define endpoint to add a new item
@app.route('/items', methods=['POST'])
def add_item():
    new_item = request.json['item']
    items.append(new_item)
    return jsonify(items)


# Define endpoint to update an existing item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    updated_item = request.json['item']
    items[item_id] = updated_item
    return jsonify(items)


# Define endpoint to delete an existing item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    items.pop(item_id)
    return jsonify(items)


if __name__ == '__main__':
    app.run(debug=True)
