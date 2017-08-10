# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = (Contact(firstname = "Andrey", middlename = "Iv", lastname = "Lobanov",
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
    app.contact.create(contact)
    app.open_home_page()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)









