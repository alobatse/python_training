# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname = "User1", middlename = "First", lastname = "Second"))
    old_contacts = app.contact.get_contact_list()
    contact = (Contact(firstname = "changed_Andrey", middlename = "changed_Iv", lastname = "changed_Lobanov",
                                                    nickname = "law",
                                                    title = "Lawer",
                                                    company = "Lobanov&brothers",
                                                    address = "Nalichnaya, 10",
                                                    home = "1111111",
                                                    mobile = "2222222",
                                                    work = "3333333",
                                                    fax = "4444444",
                                                    email = "law@mail.ru",
                                                    homepage = "lob.law.ru",
                                                    day1 = 1,
                                                    month1 = 4,
                                                    byear = "1970",
                                                    day2 = 17,
                                                    month2 = 12,
                                                    ayear = "2015",
                                                    notes = "Important client",
                                                    address2 = "Gaza, 20-55"))
    index = (0 if len(old_contacts)==0 else randrange(len(old_contacts)))
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    app.open_home_page()
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)