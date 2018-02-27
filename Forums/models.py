# -*- coding: utf-8 -*-


class Member():
    """Member related information

    Attributes:
        member_id (int): A unique member id.
        posts (list): List of posts id created by the member.

    """

    def __init__(self, name, age):
        """Create a new member

        Args:
            name (str): Member name.
            age (int): Member age.
        """

        self.name = name
        self.age = age
        self.member_id = 0
        self.posts = []

    def __str__(self):
        return "Name: %s\nAge: %d\nMember ID: %s\nPosts:%s " % (self.name, self.age, self.member_id, len(self.posts))


class Post():
    """Post related information

    Attributes:
        post_id (int): A unique post id.
    """

    def __init__(self, title, body, member_id):
        """Create a new post

        Args:
            title (str): Post title.
            body (str): Post content.
            member_id (int): Member id who is the creator of the post.
        """

        self.title = title
        self.body = body
        self.member_id = member_id
        self.post_id = 0

    def __str__(self):
        return "Title: %s\nContent: %s\nMember ID: %d\nPost ID: %d" % (self.title, self.body, self.member_id, self.post_id)
