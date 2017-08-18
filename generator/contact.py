from model.contact import Contact
import random
import string
import os.path
#import json
import getopt
import sys
import jsonpickle

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file="])
except getopt.GetoptError as err:
    print(err)
    getopt.usage()
    sys.exit(2)

n=3
f= "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

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
                                                    lastname = random_string("l.n. ", 15),
                                                    address = random_string("addr. ", 15),
                                                    home = random_str_digit("+", 15),
                                                    mobile = random_str_digit("+", 15),
                                                    work = random_str_digit("+", 15),
                                                    email = random_string("", 6) + '@' + random_string("", 10),
                                                    email2 = random_string("", 6) + '@' + random_string("", 10),
                                                    email3 = random_string("", 6) + '@' + random_string("", 10))
                                                    for i in range(4)
                                                    ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file,"w") as out:
    #out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))