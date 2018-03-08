#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections


class MemberStore(object):
    """Manipulate the principle operation on members.

    Attributes:
        members (list) = Store members objects.
    """

    members = []
    last_id = 1

    @classmethod
    def get_all(cls):
        return (member for member in cls.members)

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
        return (member for member in all_members if member.name == name)

    def get_members_with_posts(self):
        """Assign each member to his posts

        Returns:
            member_posts (dict): Ordered dictionary contains members with their posts.
        """
        all_members = self.get_all()
        members_posts = collections.OrderedDict()
        for member in all_members:
            members_posts[member] = self.get_member_posts(member)
        return members_posts

    def get_member_posts(self, member):
        return [PostStore().get_by_id(post_id) for post_id in member.posts]

    def get_top(self, list_length):
        """A list top members wrote posts

        Args:
            list_length (int): The length of top list members

        Returns:
            top_list (dict): Descending sorted ordered dictionary contains top list members.
        """
        posts = [post.member_id for post in PostStore().get_all()]
        post_member_count = collections.Counter(posts)
        top_list_member_id = reversed(collections.OrderedDict(
            sorted(post_member_count.items(), key=lambda t: t[1])))
        top_list = collections.OrderedDict()
        count = 0
        for id in top_list_member_id:
            if count >= list_length:
                break
            member = self.get_by_id(id)
            top_list[member] = self.get_member_posts(member)
            count += 1
        return top_list

    def delete(self, id):
        obj = self.get_by_id(id)
        MemberStore.members.remove(obj)

    def entity_exists(self, member):
        exist = True
        if self.get_by_id(member.id) is None:
            exist = False
        return exist

    def update(self, member):
        obj = self.get_by_id(member.id)
        obj_index = self.members.index(obj)
        MemberStore.members[obj_index] = member


class PostStore(object):
    """Manipulate the principle operation on members.

    Attributes:
        posts (list) = Store posts objects.
    """

    posts = []
    last_id = 1

    @classmethod
    def get_all(cls):
        return (post for post in cls.posts)

    def add(self, post):
        PostStore.posts += [post]
        post.id = PostStore.last_id
        PostStore.last_id += 1
        post_member = MemberStore().get_by_id(post.member_id)
        post_member.posts += [post.id]

    def get_by_id(self, id):
        all_posts = self.get_all()
        obj = None
        for post in all_posts:
            if post.id == id:
                obj = post
                break
        return obj

    def get_by_title(self, title):
        all_posts = self.get_all()
        return(post.title for post in all_posts if title in post.title)

    def delete(self, id):
        obj = self.get_by_id(id)
        PostStore.posts.remove(obj)

    def update(self, post):
        obj = self.get_by_id(post.id)
        obj_index = self.posts.index(obj)
        PostStore.posts[obj_index] = post
