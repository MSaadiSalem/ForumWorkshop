#/usr/bin/env python
# -*- coding: utf-8 -*-


class MemberStore(object):
    """Manipulate the principle operation on members.

    Atteributes:
        members (list) = Store members objects.
    """

    members = []

    def get_all(self):
        return MemberStore.members

    def add(self, member):
        if self.entity_exists(member):
            MemberStore.members += [member]

    def entity_exists(self, member):
        exist = False
        if not member in MemberStore.members:
            exist = True
        return exist


class PostStore(object):
    """Manipulate the principle operation on members.

    Atteributes:
        posts (list) = Store posts objects.
    """

    posts = []

    def get_all(self):
        return PostStore.posts

    def add(self, post):
        PostStore.posts += [post]
