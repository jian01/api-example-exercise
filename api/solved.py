from contact_databases.ram_database import ContactRamDatabase, UnexistentContact
from model.contact import Contact
from flask import Flask, render_template, url_for, request
import json


app = Flask(__name__)
contact_database = ContactRamDatabase()


@app.route('/contact_list', methods=['GET'])
def get_contact_list():
    """
    Gets the whole contact list

    Returns a json with the form of:
        {"contacts": [{"contact_id": 4, "name": "Juanito", "number": "4888-8888"}, ...]}
    """
    contact_list = []
    contacts = contact_database.get_contacts()
    for contact_id, contact in contacts.items():
        contact_list.append({"contact_id": contact_id,
                             "name": contact.name,
                             "number": contact.number})
    return json.dumps({'contacts': contact_list}), 200


@app.route('/contact/<contact_id>', methods=['GET'])
def get_contact(contact_id):
    """
    Gets the contact data for the contact id queried

    Returns a json with the form of:
        {"contact_id": 4, "name": "Juanito", "number": "4888-8888"}

    If the contact does not exists returns "Unexistent Contact" with code 404

    :param contact_id: the contact id
    """
    try:
        contact = contact_database.get_contact(int(contact_id))
    except UnexistentContact:
        return "Unexistent Contact", 404
    return json.dumps({"contact_id": contact_id,
                       "name": contact.name,
                       "number": contact.number}), 200


@app.route('/contact', methods=['POST'])
def add_contact():
    """
    Add the contact for the data sent
    Body in json with the form of:
        {"name": "Juanito", "number": "4888-8888"}

    Returns a json with the form of:
        {"contact_id": 4, "name": "Juanito", "number": "4888-8888"}
    """
    body = request.json
    contact = Contact(name=body['name'], number=body['number'])
    contact_id = contact_database.add_contact(contact)
    return json.dumps({"contact_id": contact_id,
                       "name": contact.name,
                       "number": contact.number}), 200


@app.route('/contact/<contact_id>', methods=['PUT'])
def modify_contact(contact_id):
    """
    Modifies the contact for the id sent
    Body in json with the form of:
        {"name": "Juanito", "number": "4888-8888"}

    Returns a json with the form of:
        {"contact_id": contact_id, "name": "Juanito", "number": "4888-8888"}

    If the contact does not exists returns "Unexistent Contact" with code 404

    :param contact_id: the contact id
    """
    body = request.json
    contact = Contact(name=body['name'], number=body['number'])
    try:
        contact_database.replace_contact(int(contact_id), contact)
    except UnexistentContact:
        return "Unexistent Contact", 404
    return json.dumps({"contact_id": contact_id,
                       "name": contact.name,
                       "number": contact.number}), 200


@app.route('/contact/<contact_id>', methods=['DELETE'])
def delete_contact(contact_id):
    """
    Deletes the contact for the id sent

    Returns an "OK" message with code 200.
    If the contact does not exists returns "Unexistent Contact" with code 404

    :param contact_id: the contact id
    """
    try:
        contact_database.delete_contact(int(contact_id))
    except UnexistentContact:
        return "Unexistent Contact", 404
    return "OK", 200


app.run(host='127.0.0.1', port=8080, debug=True)