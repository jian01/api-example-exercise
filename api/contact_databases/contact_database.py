"""

*** DO NOT MODIFY CODE HERE ***

"""

from abc import abstractmethod
from typing import Dict, NoReturn

from model.contact import Contact


class UnexistentContact(ValueError):
    pass


class ContactDatabase:
    """
    Contact database interface
    """

    @abstractmethod
    def get_contacts(self) -> Dict[int, Contact]:
        """
        Gets all contacts from the database

        :return: a list of contacts
        """

    @abstractmethod
    def add_contact(self, contact: Contact) -> int:
        """
        Adds a new contact to the database

        :param contact: the contact to add
        :return: a contact id to use for reference the object
        """

    @abstractmethod
    def delete_contact(self, contact_id: int) -> NoReturn:
        """
        Deletes a contact from the database

        :raise UnexistentContact: if the contact id does not exist

        :param contact_id: the id of the contact to delete
        """

    @abstractmethod
    def replace_contact(self, contact_id: int,
                        contact: Contact) -> NoReturn:
        """
        Replaces a contact from the database

        :raise UnexistentContact: if the contact id does not exist

        :param contact_id: the id of the contact to delete
        :param contact: the contact for replacing
        """

    @abstractmethod
    def get_contact(self, contact_id: int) -> Contact:
        """
        Gets a contact from the database

        :raise UnexistentContact: if the contact id does not exist

        :param contact_id: the id of the contact to delete
        """
