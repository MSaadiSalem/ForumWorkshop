#/usr/bin/env python
# -*- coding: utf-8 -*-


class MemberStore(object):
    """Manipulate the principle operation on members.

    Atteributes:
        members (list) = Store members objects.
    """

    members = []
    last_id = 1

    @classmethod
    def get_all(cls):
        return cls.members

    def add(self, member):
        MemberStore.members += [member]
        member.id = MemberStore.last_id
        MemberStore.last_id += 1

    def get_by_id(self, id):
        all_members = self.get_all()
        obj = None
        for member in all_members:
            if member.id == id:
                obj = member
                break
        return obj

    def get_by_name(self, name):
        all_members = self.get_all()
        obj = []
        for member in all_members:
            if member.name == name:
                obj += [member]
        return obj

    def delete(self, id):
        obj = self.get_by_id(id)
        MemberStore.members.remove(obj)

    def entity_exists(self, member):
        exist = True
        if self.get_by_id(member.id) == None:
            exist = False
        return exist

    def update(self, member):
        obj = self.get_by_id(member.id)
        obj_index = self.members.index(obj)
        MemberStore.members[obj_index] = member


class PostStore(object):
    """Manipulate the principle operation on members.

    Atteributes:
        posts (list) = Store posts objects.
    """

    posts = []
    last_id = 1

    @classmethod
    def get_all(cls):
        return cls.posts

    def add(self, post):
        PostStore.posts += [post]
        post.id = PostStore.last_id
        PostStore.last_id += 1

    def get_by_id(self, id):
        obj = None
        for post in PostStore.posts:
            if post.id == id:
                obj = post
                break
        return obj

    def delete(self, id):
        obj = self.get_by_id(id)
        PostStore.posts.remove(obj)

    def update(self, post):
        obj = self.get_by_id(post.id)
        obj_index = self.posts.index(obj)
        PostStore.posts[obj_index] = post
