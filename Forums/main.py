#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import models
import stores

member1 = models.Member("Member 01", 25)
member2 = models.Member("Member 02", 35)

member_store = stores.MemberStore()

member_store.add(member1)
member_store.add(member2)
print(member_store.get_all())

post1 = models.Post("Title 01", "Body contents", member1.member_id)
post2 = models.Post("Title 02", "Body contents", member2.member_id)
post3 = models.Post("Title 03", "Body contents", member1.member_id)
