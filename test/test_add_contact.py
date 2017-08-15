# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
              #+ string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_str_digit(prefix, maxlen):
    symbols = string.digits + '+' + '-' + '(' + ')'
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname = "", middlename = "", lastname = "",
                                                    address = "",
                                                    home = "",
                                                    mobile = "",
                                                    work = "",
                                                    fax = "",
                                                    email = "")] + [Contact(firstname = random_string("f.n. ", 10),
                                                    lastname = random_string("l.n. ", 10),
                                                    address = random_string("addr. ", 10),
                                                    home = random_str_digit("+", 10),
                                                    mobile = random_str_digit("+", 10),
                                                    work = random_str_digit("", 10),
                                                    email = random_string("", 6) + '@' + random_string("", 6),
                                                    email2 = random_string("", 6) + '@' + random_string("", 6),
                                                    email3 = random_string("", 6) + '@' + random_string("", 6))
                                                    for i in range(5)
                                                    ]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])


def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    app.open_home_page()
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)









