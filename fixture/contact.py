from model.contact import Contact

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
        self.contact_cache = None


    def delete(self):
        wd = self.app.wd
        #select first contact
        wd.find_element_by_name("selected[]").click()
        #submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        #confirm deletion
        wd.switch_to_alert().accept()
        self.contact_cache = None


    def modify(self, new_contact_data):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_name("selected[]").click()
        #modify contact fields
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
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
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.contact_cache =[]
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                id = element.find_element_by_name("selected[]").get_attribute("value")
                lastname = cells[1].text
                firstname = cells[2].text
                self.contact_cache.append(Contact(firstname = firstname, lastname = lastname, id = id))
        return list(self.contact_cache)