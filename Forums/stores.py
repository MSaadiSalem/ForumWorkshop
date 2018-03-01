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
        for member in MemberStore.members:
            if member.member_id == id:
                return member
        print "Invalid Member ID."

    def delete(self, id):
        exist = self.get_by_id(id)
        if exist != None:
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
        for post in PostStore.posts:
            if post.post_id == id:
                return post
        print "Invalid Post ID."

    def delete(self, id):
        exist = self.get_by_id(id)
        if exist != None:
            PostStore.posts.remove(exist)
