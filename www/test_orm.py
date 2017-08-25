#!/usr/bin/env python
# -*- coding:utf-8 -*-

import asyncio
import orm
from models import User


async def test(loop):
    await orm.create_pool(loop, user='root', password='220930', db='awssome')

    u = User(name='Test', email='test_2@example.com', password='1234567890', image='about:blank')

    await u.save()


loop = asyncio.get_event_loop()

loop.run_until_complete(test(loop))


loop.close()