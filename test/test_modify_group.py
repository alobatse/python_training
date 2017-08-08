# -*- coding: utf-8 -*-
from model.group import Group

def test_modify_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name = "test"))
    new_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="Edited name", header="Edited header", footer="Edited footer"))
    old_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name = "test"))
    new_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="New edited name"))
    old_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name = "test"))
    new_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(header="New edited header"))
    old_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

