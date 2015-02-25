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
from __future__ import absolute_import, unicode_literals
from zope.app.form import CustomWidgetFactory
from zope.app.form.browser import FileWidget
from zope.cachedescriptors.property import Lazy
from zope.component import getMultiAdapter, createObject
from zope.formlib import form
from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile
from gs.group.base.form import GroupForm
from gs.group.member.canpost.interfaces import IGSPostingUser
from gs.group.messages.add.base import add_a_post
from gs.group.messages.privacy import MessagesPrivacy
from gs.profile.email.base.emailuser import EmailUser
from .interfaces import IStartTopic
from . import GSMessageFactory as _


class MyFileWidget(FileWidget):
    def _toFieldValue(self, input):
        #--=mpj17=-- Lookie! A hack!
        return self.context.missing_value


class StartTopic(GroupForm):
    """View of a single GroupServer Topic"""
    label = _('start-topic-label', 'Start a new topic')
    pageTemplateFileName = 'browser/templates/start.pt'
    template = ZopeTwoPageTemplateFile(pageTemplateFileName)
    form_fields = form.Fields(IStartTopic, render_context=False)

    def __init__(self, context, request):
        super(StartTopic, self).__init__(context, request)
        self.__message = None
        cw = CustomWidgetFactory(MyFileWidget)
        self.form_fields['uploadedFile'].custom_widget = cw

    @Lazy
    def privacy(self):
        retval = MessagesPrivacy(self.context)
        return retval

    def setUpWidgets(self, ignore_request=True):
        self.adapters = {}
        if self.userInfo.anonymous:
            fromAddr = ''
        else:
            emailUser = EmailUser(self.context, self.userInfo)
            addrs = emailUser.get_delivery_addresses()
            if addrs:
                fromAddr = addrs[0]
            else:
                fromAddr = ''
        data = {
            'fromAddress': fromAddr,
            'message': '',
            'sticky': False,  # New topics cannot be sticky
        }
        self.widgets = form.setUpWidgets(
            self.form_fields, self.prefix, self.context,
            self.request, form=self, data=data,
            ignore_request=ignore_request)
        assert self.widgets

    @form.action(label=_('start-button', 'Start'), name="start",
                 failure='handle_action_failure')
    def handle_add(self, action, data):
        if self.__message != data['message']:
            # --=mpj17=-- Formlib sometimes submits twice submits twice
            self.__message = data['message']
            uploadedFiles = [self.request[k]
                             for k in self.request.form
                             if (('form.uploadedFile' in k) and
                                 self.request[k])]
            r = add_a_post(
                groupId=self.groupInfo.id,
                siteId=self.siteInfo.id,
                replyToId='',
                topic=data['topic'],
                message=data['message'],
                tags=[],
                email=data['fromAddress'],
                uploadedFiles=uploadedFiles,
                context=self.context,
                request=self.request)
            if r['error']:
                # TODO make a seperate validator for messages that the
                #   web and email subsystems can use to verifiy the
                #   messages before posting them.
                self.status = r['message']
            else:
                s = '<p><a href="{id}#{id}">{message}</a></p>'
                self.status = s.format(**r)
        assert self.status
        assert type(self.status) == unicode

    def handle_action_failure(self, action, data, errors):
        if len(errors) == 1:
            s = _('single-error', 'There is an error:')
        else:
            s = _('errors', 'There are errors:')
        self.status = '<p>{0}</p>'.format(s)

    @Lazy
    def userInfo(self):
        retval = createObject('groupserver.LoggedInUser', self.context)
        return retval

    @Lazy
    def userPostingInfo(self):
        g = self.groupInfo.groupObj
        assert g
        # --=mpj17=-- A Pixie Caramel to anyone who can tell me
        #    why the following line does not work in Zope 2.10.
        #   "Zope Five is screwed" is not sufficient.
        #self.userPostingInfo = IGSPostingUser((g, userInfo))
        retval = getMultiAdapter((g, self.userInfo), IGSPostingUser)
        assert retval
        return retval
