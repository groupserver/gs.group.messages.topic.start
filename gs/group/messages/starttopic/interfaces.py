# coding=utf-8
from zope.interface import Interface
from zope.schema import Bool, Bytes, Choice, Field, Int, Text, TextLine 
from Products.XWFMailingListManager.interfaces import IGSPostMessage

class IStartTopic(IGSPostMessage):
    topic = TextLine(title=u'Topic',
        description=u'The title of the topic. This appears as the '\
          u'subject of the email messages that are sent out.',
        required=True)
