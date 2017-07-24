# -*- coding: utf-8 -*-
import pytest
from Application import application
from model.contact import Contact

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    self.create_contact(wd, Contact( firstname = "Andrey", middlename = "Iv", lastname = "Lobanov",\
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
    self.return_to_contact_page(wd)
    self.session,logout(wd)


def create_contact(self, wd, contact):
    self.open_add_contact_page(wd)
    wd.find_element_by_name("firstname").click()
    wd.find_element_by_name("firstname").clear()
    wd.find_element_by_name("firstname").send_keys(contact.firstname)
    wd.find_element_by_name("middlename").click()
    wd.find_element_by_name("middlename").clear()
    wd.find_element_by_name("middlename").send_keys(contact.middlename)
    wd.find_element_by_name("lastname").click()
    wd.find_element_by_name("lastname").clear()
    wd.find_element_by_name("lastname").send_keys(contact.lastname)
    wd.find_element_by_name("nickname").click()
    wd.find_element_by_name("nickname").clear()
    wd.find_element_by_name("nickname").send_keys(contact.nickname)
    #wd.find_element_by_name("photo").click()
    wd.find_element_by_name("title").click()
    wd.find_element_by_name("title").clear()
    wd.find_element_by_name("title").send_keys(contact.title)
    wd.find_element_by_name("company").click()
    wd.find_element_by_name("company").clear()
    wd.find_element_by_name("company").send_keys(contact.company)
    wd.find_element_by_name("address").click()
    wd.find_element_by_name("address").clear()
    wd.find_element_by_name("address").send_keys(contact.address)
    wd.find_element_by_name("home").click()
    wd.find_element_by_name("home").clear()
    wd.find_element_by_name("home").send_keys(contact.home)
    wd.find_element_by_name("mobile").click()
    wd.find_element_by_name("mobile").clear()
    wd.find_element_by_name("mobile").send_keys(contact.mobile)
    wd.find_element_by_name("work").click()
    wd.find_element_by_name("work").clear()
    wd.find_element_by_name("work").send_keys(contact.work)
    wd.find_element_by_name("fax").click()
    wd.find_element_by_name("fax").clear()
    wd.find_element_by_name("fax").send_keys(contact.fax)
    wd.find_element_by_name("email").click()
    wd.find_element_by_name("email").clear()
    wd.find_element_by_name("email").send_keys(contact.email)
    wd.find_element_by_name("homepage").click()
    wd.find_element_by_name("homepage").clear()
    wd.find_element_by_name("homepage").send_keys(contact.homepage)
    if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[" + str(contact.day1 + 2) + "]").is_selected():
        wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[" + str(contact.day1 + 2) + "]").click()
    if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[" + str(contact.month1 + 1) + "]").is_selected():
        wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[" + str(contact.month1 + 1) + "]").click()
    wd.find_element_by_name("byear").click()
    wd.find_element_by_name("byear").clear()
    wd.find_element_by_name("byear").send_keys(contact.byear)
    if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[" + str(contact.day2 + 2) + "]").is_selected():
        wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[" + str(contact.day2 + 2) + "]").click()
    if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[" + str(contact.month2 + 1) + "]").is_selected():
        wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[" + str(contact.month2 + 1) + "]").click()
    wd.find_element_by_name("ayear").click()
    wd.find_element_by_name("ayear").clear()
    wd.find_element_by_name("ayear").send_keys(contact.ayear)
    wd.find_element_by_name("notes").click()
    wd.find_element_by_name("notes").clear()
    wd.find_element_by_name("notes").send_keys(contact.notes)
    wd.find_element_by_name("address2").click()
    wd.find_element_by_name("address2").clear()
    wd.find_element_by_name("address2").send_keys(contact.address2)

def return_to_contact_page(self,wd):
    wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

def open_add_contact_page(self, wd):
    wd.find_element_by_link_text("add new").click()






