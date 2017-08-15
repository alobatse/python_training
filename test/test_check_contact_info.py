import re

def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_info_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phone_from_home_page == merge_phones_like_on_home_page(contact_info_from_edit_page)


def test_phones_on_home_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_info_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home == contact_info_from_edit_page.home
    assert contact_from_view_page.mobile == contact_info_from_edit_page.mobile
    assert contact_from_view_page.work == contact_info_from_edit_page.work


def test_check_contact_info(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_info_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.firstname == contact_info_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_info_from_edit_page.lastname
    assert merge_address(contact_from_home_page.address) == merge_address(contact_info_from_edit_page.address)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_info_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_info_from_edit_page)


def clear_phones(s):
    return re.sub("[() -]","", s)

def clear_emails(s):
    return re.sub("[() ]","", s)

def merge_address(s):
    return "".join(map(lambda x: x.rstrip().lstrip(),
                         filter(lambda x: x is not None,
                                s.split())))

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter( lambda x: x!="",
                             map(lambda x: clear_phones(x),
                                 filter(lambda x: x is not None,
                                        [contact.home, contact.mobile, contact.work]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter( lambda x: x!="",
                             map(lambda x:
                                 clear_emails(x),
                                 filter(lambda x: x is not None,
                                        [contact.email, contact.email2, contact.email3]))))