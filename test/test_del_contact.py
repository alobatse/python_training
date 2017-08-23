# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_delete_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname = "User1"))
    old_contacts = db.get_contact_list()
    for contact in old_contacts:
        print (contact)
    #index = random.randrange(len(old_contacts))
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    app.open_home_page()
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = db.get_contact_list()
    #old_contacts[index:index+1] = []
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key = Contact.id_or_max) == sorted(app.contact.get_contact_list(), key = Contact.id_or_max)