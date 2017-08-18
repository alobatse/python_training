from model.group import Group
#import random
#import string

testdata = [
       Group(name="dfg", header="dfgdfg", footer="dfgdfgdfg"),
       Group(name="dfg1", header="dfgdfg1", footer="dfgdfgdfg1")
       ]

#def random_string(prefix, maxlen):
#    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
#    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


#testdata = [Group(name="", header="", footer="")] + [
#       Group(name=random_string("gr", 10), header=random_string("hd", 20), footer=random_string("", 10))
#       for i in range(2)

       #for name in ["", random_string("gr", 10)]
       #for header in ["", random_string("hd", 20)]
       #for footer in ["", random_string("", 10)]
#]