from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample in-memory database
users = {
    1: {'name': 'Alice', 'reputation': 100, 'avatar_url': 'http://example.com/avatar1.png'},
    2: {'name': 'Bob', 'reputation': 200, 'avatar_url': 'http://example.com/avatar2.png'},
}

@app.route('/users/<int:id>', methods=['GET', 'PUT'])
def user_profile(id):
    if request.method == 'GET':
        user = users.get(id)
        if user:
            return jsonify(user), 200
        else:
            return jsonify({'error': 'User not found'}), 404
    elif request.method == 'PUT':
        data = request.json
        if id in users:
            users[id].update(data)
            return jsonify(users[id]), 200
        else:
            return jsonify({'error': 'User not found'}), 404

@app.route('/users/<int:id>/reputation', methods=['GET'])
def user_reputation(id):
    user = users.get(id)
    if user:
        return jsonify({'reputation': user['reputation']}), 200
    else:
        return jsonify({'error': 'User not found'}), 404

@app.route('/users/<int:id>/avatar', methods=['POST'])
def user_avatar(id):
    user = users.get(id)
    if user:
        avatar_url = request.json.get('avatar_url')
        user['avatar_url'] = avatar_url
        return jsonify({'avatar_url': user['avatar_url']}), 200
    else:
        return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)