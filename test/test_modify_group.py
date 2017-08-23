# -*- coding: utf-8 -*-
from model.group import Group
import random

def test_modify_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name = "test"))
    #old_groups = app.group.get_group_list()
    old_groups = db.get_group_list()
    group = Group(name="Edited name", header="Edited header", footer="Edited footer")
    index = random.randrange(len(old_groups))
    random_group = old_groups[index]
    print ("len(old_groups) = " + str(len(old_groups)))
    group.id = random_group.id
    #group.id = old_groups[index].id
    app.group.modify_group_by_id(random_group.id, group)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key = Group.id_or_max) == sorted(app.group.get_group_list(), key = Group.id_or_max)

#def test_modify_group_name(app, db):
#    if app.group.count() == 0:
#        app.group.create(Group(name = "test"))
#    old_groups = app.group.get_group_list()
#    group = Group(name="New edited name")
#    index = randrange(len(old_groups))
#    group.id = old_groups[index].id
#    app.group.modify_group_by_index(index, group)
#    assert len(old_groups) == app.group.count()
#    new_groups = app.group.get_group_list()
#    old_groups[index] = group
#    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_modify_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name = "test"))
#    old_groups = app.group.get_group_list()
#    group = Group(header="New edited header")
#    group.id = old_groups[0].id
#    app.group.modify_first_group(group)
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
#    old_groups[0] = group
#    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

