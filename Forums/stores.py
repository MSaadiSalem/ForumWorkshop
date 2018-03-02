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
        member.member_id = MemberStore.last_id
        MemberStore.last_id += 1

    def entity_exists(self, member):
        exist = True
        if self.get_by_id(member.member_id) == None:
            exist = False
        return exist

    def get_by_id(self, id):
        obj = None
        for member in MemberStore.members:
            if member.member_id == id:
                obj = member
        return obj

    def delete(self, id):
        exist = self.get_by_id(id)
        if exist is not None:
            MemberStore.members.remove(exist)


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

    def get_by_id(self, id):
        obj = None
        for post in PostStore.posts:
            if post.post_id == id:
                obj = post
        return obj

    def delete(self, id):
        exist = self.get_by_id(id)
        if exist is not None:
            PostStore.posts.remove(exist)
