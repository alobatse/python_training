from model.contact import Contact
import re

class ContactHelper:
    def __init__(self, app):
        self.app  = app

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def create(self, contact):
        wd = self.app.wd
        self.open_add_contact_page()
        self.fill_contact_form(contact)
        self.return_to_contact_page()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        #if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[" + str(
        #                contact.day1 + 2) + "]").is_selected():
        #    wd.find_element_by_xpath(
        #        "//div[@id='content']/form/select[1]//option[" + str(contact.day1 + 2) + "]").click()
        #if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[" + str(
        #                contact.month1 + 1) + "]").is_selected():
        #    wd.find_element_by_xpath(
        #        "//div[@id='content']/form/select[2]//option[" + str(contact.month1 + 1) + "]").click()
        #    change_field_value("byear")
        #if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[" + str(
        #                contact.day2 + 2) + "]").is_selected():
        #    wd.find_element_by_xpath(
        #        "//div[@id='content']/form/select[3]//option[" + str(contact.day2 + 2) + "]").click()
        #if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[" + str(
        #                contact.month2 + 1) + "]").is_selected():
        #    wd.find_element_by_xpath(
        #        "//div[@id='content']/form/select[4]//option[" + str(contact.month2 + 1) + "]").click()
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("notes", contact.notes)
        self.change_field_value("address2", contact.address2)
        #self.contact_cache = None



    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        #select contact
        self.select_contact_by_index(index)
        #submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        #confirm deletion
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        #select contact
        self.select_contact_by_id(id)
        #submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        #confirm deletion
        wd.switch_to_alert().accept()
        self.contact_cache = None


    def modify_first_contact(self, new_contact_data):
        self.modify_contact_by_index( 0, new_contact_data)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        # select contact
        #self.select_contact_by_index(index)
        # modify contact fields
        #wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        #wd.find_elements_by_xpath("//img[@tittle='Edit']")[index].click()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()
        self.fill_contact_form(new_contact_data)
        # submit modified group
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def modify_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        # select contact
        #self.select_contact_by_index(index)
        # modify contact fields
        #wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        #wd.find_elements_by_xpath("//img[@tittle='Edit']")[index].click()
        #row = wd.find_elements_by_name("entry")[index]
        checkbox = self.select_contact_by_id(id)
        row = checkbox.find_element_by_xpath("./../..")
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()
        self.fill_contact_form(new_contact_data)
        # submit modified group
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def return_to_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook") and len(wd.find_elements_by_name("searchstring")) > 0):
            wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def open_add_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("firstname")) > 0):
            wd.find_element_by_link_text("add new").click()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))


    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()


    def select_first_contact(self):
        self.select_contact_by_index(0)

    def select_contact_by_id(self, id):
        wd = self.app.wd
        checkbox = wd.find_element_by_css_selector("input[value='%s']" % id)
        checkbox.click()
        return checkbox

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache =[]
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                id = element.find_element_by_name("selected[]").get_attribute("value")
                #id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(firstname = firstname, lastname = lastname, id = id,
                                                  address = address,
                                                  all_emails_from_home_page=all_emails, all_phones_from_home_page = all_phones))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        id = wd.find_element_by_name("id").get_attribute("value")
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        #fax = wd.find_element_by_name("fax").get_attribute("value")
        return Contact(id=id, firstname=firstname, lastname=lastname, address = address,
                       home=home, mobile=mobile, work=work,
                       email = email, email2 = email2, email3 = email3)


    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home = re.search("H: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        return Contact(home=home, mobile=mobile, work=work)

    def add_contact_to_group(self, contact, group):
        wd = self.app.wd
        self.select_contact_by_id(contact.id)
        wd.find_element_by_name("to_group").find_element_by_css_selector("option[value=\"%s\"]" % group.id).click()
        wd.find_element_by_name("add").click()
        wd.find_element_by_partial_link_text("group page").click()

    def delete_contact_from_group(self, contact):
        wd = self.app.wd
        self.select_contact_by_id(contact.id)
        wd.find_element_by_name("remove").click()
        wd.find_element_by_partial_link_text("group page").click()

    def select_group(self, group):
        wd = self.app.wd
        wd.find_element_by_name("group").find_element_by_css_selector("option[value=\"%s\"]" % group.id).click()