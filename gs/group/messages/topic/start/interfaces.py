# -*- coding: utf-8 -*-
##############################################################################
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
##############################################################################
from __future__ import unicode_literals
from zope.schema import TextLine
from gs.group.messages.topic.base.interfaces import IGSPostMessage


class IStartTopic(IGSPostMessage):
    topic = TextLine(title='Topic',
                        description='The title of the topic. This appears '
                          'as the subject of the email messages that are '
                          'sent out.',
                        required=True)
