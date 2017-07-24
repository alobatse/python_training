# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.contact import Contact

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname = "Andrey", middlename = "Iv", lastname = "Lobanov",\
                                                    nickname = "law",\
                                                    title = "Lawer",\
                                                    company = "Lobanov&brothers",\
                                                    address = "Nalichnaya, 10",\
                                                    home = "1111111",\
                                                    mobile = "2222222",\
                                                    work = "3333333",\
                                                    fax = "4444444",\
                                                    email = "law@mail.ru",\
                                                    homepage = "lob.law.ru",\
                                                    day1 = 1,\
                                                    month1 = 4,\
                                                    byear = "1970",\
                                                    day2 = 17,\
                                                    month2 = 12,\
                                                    ayear = "2015",\
                                                    notes = "Important client",\
                                                    address2 = "Gaza, 20-55"))
    app.session.logout()









