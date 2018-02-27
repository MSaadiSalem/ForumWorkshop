#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import models

member1 = models.Member("Ahmed", 25)
member2 = models.Member("Ali", 35)

post1 = models.Post("Title 01", "Body contents", member1.name)
post2 = models.Post("Title 02", "Body contents", member2.name)
post3 = models.Post("Title 03", "Body contents", member1.name)
