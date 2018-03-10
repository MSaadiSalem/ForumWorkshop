#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools


class MemberStore(object):
    """Manipulate the principle operation on members.

    Attributes:
        members (list): Store members objects.
        last_id (int): A counter that holds last added member object id.
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

    def get_members_with_posts(self, posts):
        """Assign each member to his/her posts

        Args:
            posts (Post): An instance of post class.

        Returns:
            all_members (list): An updated members list associated their posts objects.
        """

        all_members = self.get_all()
        for member, post in itertools.product(all_members, posts):
            if post.member_id == member.id:
                member.posts.append(post)
        return all_members

    def get_top(self):
        """A list top members wrote posts

        Returns:
            all_members (list): Descending sorted ordered list contains top members.
        """

        all_members = self.get_all()
        all_members = list(all_members)
        all_members.sort(key=lambda member: len(member.posts), reverse=True)
        return all_members[:2]

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
        posts (list): Store posts objects.
        last_id (int): A counter that holds last added post object id.
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
