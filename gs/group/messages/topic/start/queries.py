# -*- coding: utf-8 -*-
############################################################################
#
# Copyright © 2013, 2015 OnlineGroups.net and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
############################################################################
import sqlalchemy as sa
from gs.database import getSession, getTable


class TopicsQuery(object):
    def __init__(self):
        self.topicTable = getTable('topic')

    def recent_topics(self, groupId, siteId, limit=255):
        tt = self.topicTable
        cols = [tt.c.original_subject]
        s = sa.select(cols, order_by=sa.desc(tt.c.last_post_date))
        s.append_whereclause(tt.c.group_id == groupId)
        s.append_whereclause(tt.c.site_id == siteId)
        s.append_whereclause(tt.c.site_id == siteId)
        s.append_whereclause(tt.c.hidden == None)  # lint:ok

        session = getSession()
        r = session.execute(s)
        retval = [x['original_subject'].encode('ascii', 'ignore')
                  for x in r]
        return retval
