#/usr/bin/env python
# -*- coding: utf-8 -*-


class MemberStore(object):
    """Manipulate the principle operation on members.

    Atteributes:
        members (list) = Store members objects.
    """

    members = []
    last_id = 1

    def get_all(self):
        return MemberStore.members

    def add(self, member):
        MemberStore.members += [member]


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
