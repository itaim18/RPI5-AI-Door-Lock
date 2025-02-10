from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample in-memory database (replace with real DB if needed)
data = []

# Create - Add a new item
@app.route('/items', methods=['POST'])
def create_item():
    new_item = request.get_json()  # Get the data sent in the request body
    data.append(new_item)  # Add item to "database"
    return jsonify(new_item), 201  # Return the item with a 201 status

# Read - Get all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(data), 200  # Return all items in the database

# Read - Get a specific item by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    if item_id < len(data):
        return jsonify(data[item_id]), 200  # Return item by ID
    return jsonify({'error': 'Item not found'}), 404  # Error if item doesn't exist

# Update - Update an existing item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    if item_id < len(data):
        updated_item = request.get_json()  # Get updated data
        data[item_id] = updated_item  # Update the item in the "database"
        return jsonify(updated_item), 200  # Return updated item
    return jsonify({'error': 'Item not found'}), 404

# Delete - Delete an item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    if item_id < len(data):
        deleted_item = data.pop(item_id)  # Remove item from "database"
        return jsonify(deleted_item), 200  # Return deleted item
    return jsonify({'error': 'Item not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
