"""

*** DO NOT MODIFY CODE HERE ***

"""

from typing import Dict, NoReturn

from contact_databases.contact_database import ContactDatabase, UnexistentContact
from model.contact import Contact

class ContactRamDatabase(ContactDatabase):
    """
    Contact ram database implementation
    """
    actual_id: int
    contact: Dict[int, Contact]

    def __init__(self):
        self.actual_id = 0
        self.contacts = {}

    def get_contacts(self) -> Dict[int, Contact]:
        """
        Gets all contacts from the database

        :return: a list of contacts
        """
        return self.contacts.copy()

    def add_contact(self, contact: Contact) -> int:
        """
        Adds a new contact to the database

        :param contact: the contact to add
        :return: a contact id to use for reference the object
        """
        self.contacts[self.actual_id] = contact
        self.actual_id += 1
        return self.actual_id - 1

    def delete_contact(self, contact_id: int) -> NoReturn:
        """
        Deletes a contact from the database

        :raise UnexistentContact: if the contact id does not exist

        :param contact_id: the id of the contact to delete
        """
        if contact_id not in self.contacts:
            raise UnexistentContact
        del self.contacts[contact_id]

    def replace_contact(self, contact_id: int,
                        contact: Contact) -> NoReturn:
        """
        Replaces a contact from the database

        :raise UnexistentContact: if the contact id does not exist

        :param contact_id: the id of the contact to delete
        :param contact: the contact for replacing
        """
        if contact_id not in self.contacts:
            raise UnexistentContact
        self.contacts[contact_id] = contact

    def get_contact(self, contact_id: int) -> Contact:
        """
        Gets a contact from the database

        :raise UnexistentContact: if the contact id does not exist

        :param contact_id: the id of the contact to delete
        """
        if contact_id not in self.contacts:
            raise UnexistentContact
        return self.contacts[contact_id]
