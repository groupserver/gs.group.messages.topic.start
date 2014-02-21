# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright © 2013, 2014 OnlineGroups.net and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
from __future__ import absolute_import, unicode_literals
from json import dumps as to_json
from zope.cachedescriptors.property import Lazy
from gs.core import to_ascii
from gs.group.base import GroupPage
from .queries import TopicsQuery


class Subjects(GroupPage):

    def __init__(self, group, request):
        super(Subjects, self).__init__(group, request)
        request.response.setHeader(to_ascii("Content-Type"),
                                    to_ascii('application/json; charset=ascii'))

    @Lazy
    def topicsQuery(self):
        retval = TopicsQuery()
        return retval

    def __call__(self):
        topics = self.topicsQuery.recent_topics(self.groupInfo.id,
                                                self.siteInfo.id)
        retval = to_json(topics, ensure_ascii=True)
        return retval
