# coding=utf-8
from zope.interface import Interface
from zope.schema import TextLine 
from gs.group.messages.topic.interfaces import IGSPostMessage

class IStartTopic(IGSPostMessage):
    topic = TextLine(title=u'Topic',
        description=u'The title of the topic. This appears as the '\
          u'subject of the email messages that are sent out.',
        required=True)
