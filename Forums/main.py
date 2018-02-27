#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import models

member1 = models.Member("Member 01", 25)
member2 = models.Member("Member 02", 35)

post1 = models.Post("Title 01", "Body contents", member1.member_id)
post2 = models.Post("Title 02", "Body contents", member2.member_id)
post3 = models.Post("Title 03", "Body contents", member1.member_id)
