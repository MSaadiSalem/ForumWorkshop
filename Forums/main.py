#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import models
import stores


def create_members():
    member1 = models.Member("Mohammed", 20)
    member2 = models.Member("Omar", 22)
    member3 = models.Member("Abdo", 25)
    print(member1)
    print(member2)
    print(member3)
    print("=" * 30)

    return member1, member2, member3


def store_should_add_models(instances, instance_store):

    for instance in instances:
        instance_store.add(instance)


def link_posts_to_members(posts):
    members = stores.MemberStore()

    for post in posts:
        post_member = members.get_by_id(post.member_id)
        post_member.posts += [post.id]


def stores_should_be_similar():

    member_store1 = stores.MemberStore()
    member_store2 = stores.MemberStore()
    if member_store1.get_all() is member_store2.get_all():
        print("Same stores elements !")


def print_all_instances(instance_store):
    print("-" * 30)

    for instance in instance_store.get_all():
        print(instance)

    print("-" * 30)


def get_by_id_should_retrieve_same_object(member_store, member2):
    member2_retrieved = member_store.get_by_id(member2.id)

    if member2 is member2_retrieved:
        print("member2 and member2_retrieved are matching !")


def update_should_modify_object(member_store, member3):
    member3_copy = models.Member(member3.name, member3.age)
    member3_copy.id = 3

    if member3_copy is not member3:
        print("member3 and member3_copy are not the same !")

    print(member3_copy)
    member3_copy.name = "john"
    member_store.update(member3_copy)
    print(member_store.get_by_id(member3.id))


def catch_exception_when_deleting():
    try:
        member_store.delete(5)
    except ValueError:
        print("It should be an existence entity before deleting !")


def create_post():
    post1 = models.Post("Title 01", "Content 01", member1.id)
    post2 = models.Post("Title 02", "Content 02", member2.id)
    post3 = models.Post("Title 03", "Content 03", member3.id)
    post4 = models.Post("Title 04", "Content 04", member1.id)
    post5 = models.Post("Title 05", "Content 05", member1.id)
    print(post1)
    print(post2)
    print(post3)
    print(post4)
    print(post5)
    print("=" * 30)

    return post1, post2, post3, post4, post5

# Members


members_instances = create_members()
member1, member2, member3 = members_instances

member_store = stores.MemberStore()

store_should_add_models(members_instances, member_store)

stores_should_be_similar()

print_all_instances(member_store)

get_by_id_should_retrieve_same_object(member_store, member2)

update_should_modify_object(member_store, member3)

catch_exception_when_deleting()

print_all_instances(member_store)

# Posts

post_instances = create_post()
post1, post2, post3, post4, post5 = post_instances

post_store = stores.PostStore()

store_should_add_models(post_instances, post_store)

print_all_instances(post_store)

# Link Posts to Members

link_posts_to_members(post_store.posts)


print_all_instances(member_store)
