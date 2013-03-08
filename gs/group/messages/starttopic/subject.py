# -*- coding: utf-8 -*-
from json import dumps
from zope.cachedescriptors.property import Lazy
from gs.group.base import GroupPage
from queries import TopicsQuery


class Subjects(GroupPage):

    def __init__(self, group, request):
        super(Subjects, self).__init__(group, request)
        response = request.response
        response.setHeader("Content-Type", 'application/json; charset=ascii')

    @Lazy
    def topicsQuery(self):
        retval = TopicsQuery()
        return retval

    def __call__(self):
        topics = self.topicsQuery.recent_topics(self.groupInfo.id,
                                                self.siteInfo.id)
        retval = dumps(topics, ensure_ascii=True)
        return retval
