from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String)
    username = db.Column(db.String)
    created_at = db.Column(db.String)
    updated_at = db.Column(db.DateTime)

@app.route('/messages', methods=['GET'])
def get_messages():
    messages = Message.query.order_by(Message.created_at.asc()).all()
    return jsonify([message.serialize() for message in messages])

@app.route('/messages', methods=['POST'])
def create_message():
    body = request.form.get('body')
    username = request.form.get('username')
    message = Message(body=body, username=username)
    db.session.add(message)
    db.session.commit()
    return jsonify(message.serialize())

@app.route('/messages/<int:id>', methods=['PATCH'])
def update_message(id):
    message = Message.query.get(id)
    body = request.form.get('body')
    message.body = body
    db.session.commit()
    return jsonify(message.serialize())

@app.route('/messages/<int:id>', methods=['DELETE'])
def delete_message(id):
    message = Message.query.get(id)
    db.session.delete(message)
    db.session.commit()
    return jsonify({'message': 'Message deleted'})

if __name__ == '__main__':
    app.run()
