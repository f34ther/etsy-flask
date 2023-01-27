from flask import Blueprint, request, jsonify, render_template
from helpers import token_required
from models import db, User, Item, contact_schema, contacts_schema

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/items', methods=['POST'])
@token_required
def create_contact(current_user_token):
    title = request.json['title']
    description = request.json['description']
    price = request.json['price']
    shipping_id = request.json['shipping_id']
    user_token = current_user_token.token

    print(f'BIG TESTER: {current_user_token.token}')

    contact = Item(title, description, price,
                   shipping_id, user_token=user_token)

    db.session.add(contact)
    db.session.commit()

    response = contact_schema.dump(contact)
    return jsonify(response)


@api.route('/items', methods=['GET'])
@token_required
def get_contact(current_user_token):
    a_user = current_user_token.token
    items = Item.query.filter_by(user_token=a_user).all()
    response = contacts_schema.dump(items)
    return jsonify(response)


@api.route('/items/<id>', methods=['GET'])
@token_required
def get_single_contact(current_user_token, id):
    contact = Item.query.get(id)
    response = contact_schema.dump(contact)
    return jsonify(response)


@api.route('/items/<id>', methods=['POST', 'PUT'])
@token_required
def update_contact(current_user_token, id):
    item = Item.query.get(id)
    item.title = request.json['title']
    item.description = request.json['description']
    item.price = request.json['price']
    item.shipping_id = request.json['shipping_id']
    item.user_token = current_user_token.token

    db.session.commit()
    response = contact_schema.dump(item)
    return jsonify(response)


@api.route('/items/<id>', methods=['DELETE'])
@token_required
def delete_contact(current_user_token, id):
    item = Item.query.get(id)
    db.session.delete(item)
    db.session.commit()
    response = contact_schema.dump(item)
    return jsonify(response)
