from sys import maxsize

class Contact:
    def __init__ (self, firstname = None, middlename = None, lastname = None, nickname = None, title = None,
                  company = None, address = None, home = None, mobile = None, work = None, fax = None,
                  all_phones_from_home_page = None,
                  email = None, email2 = None, email3 = None, all_emails_from_home_page = None,
                  homepage = None, day1 = None, month1 = None, byear = None, day2 = None,
                  month2 = None, ayear = None, notes = None, address2 = None, id = None ):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.day1 = day1
        self.month1 = month1
        self.byear = byear
        self.day2 = day2
        self.month2 = month2
        self.ayear = ayear
        self.notes = notes
        self.address2 = address2
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page
        self.id = id

    def __repr__ (self):
        return "%s:%s %s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id == None or other.id == None or  self.id == other.id) and self.firstname.rstrip() == other.firstname.rstrip() and self.lastname.rstrip() == other.lastname.rstrip()

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize