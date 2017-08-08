# -*- coding: utf-8 -*-
from model.contact import Contact


def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname = "User1"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete()
    app.open_home_page()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)