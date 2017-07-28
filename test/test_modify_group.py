# -*- coding: utf-8 -*-
from model.group import Group

def test_modify_group(app):
    app.group.modify_first_group(Group(name="Edited name", header="Edited header", footer="Edited footer"))


def test_modify_group_name(app):
    app.group.modify_first_group(Group(name="New edited name"))


def test_modify_group_header(app):
    app.group.modify_first_group(Group(header="New edited header"))

