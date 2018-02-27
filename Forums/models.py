# -*- coding: utf-8 -*-


class Member():

    def __init__(self, name, age):
        """Create a new member

        Args:
            name (str): Member name.
            age (int): Member age.
        """

        self.name = name
        self.age = age


class Post():

    def __init__(self, title, body, member):
        """Create a new post

        Args:
            title (str): Post title.
            body (str): Post content.
            member (str): the member who creates the post.
        """

        self.title = title
        self.body = body
        self.member = member
