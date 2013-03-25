================================
``gs.group.messages.starttopic``
================================
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The Start a Topic page for GroupServer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Author: `Michael JasonSmith`_
:Contact: Michael JasonSmith <mpj17@onlinegroups.net>
:Date: 2013-03-25
:Organization: `GroupServer.org`_
:Copyright: This document is licensed under a
  `Creative Commons Attribution-Share Alike 3.0 New Zealand License`_
  by `OnlineGroups.Net`_.

Introduction
============

This product supplies the *New Topic* page_ for `GroupServer`_, as well as
the JSON_ list of topics that is used to provide the autocomplete
JavaScript for the page.

Page
====

The *New Topic* page is closely modelled on the *Add a reply* form on the
Topic page [#topic]_. Its primary difference is the ``Topic`` field, which
allows the participant to set the subject line. To encourage participants
to *add* to topics, rather than start new ones, the Typeahead_ plugin to
suggest existing topic-titles, rather than new ones. The autocomplete code
is supplied with data by the JSON_ page, also provided by this product.

JSON
====

The page ``topics.json`` supplies the list of 255 most recent topics
ordered by the date of the most recent post, in JSON format. This is used
to provide the data for the Typeahead JavaScript_.

JavaScript
----------

The resource ``/++resource++gs-group-messages-startopic-20130308.js``
provides the JavaScript for the page. It creates a Bootstrap Typeahead_
widget after the page loads. It then request ``topics.json`` using AJAX
once the user starts typing in the ``Topic`` field.

Resources
=========

- Code repository: https://source.iopen.net/groupserver/gs.group.messages.starttopic
- Questions and comments to http://groupserver.org/groups/development
- Report bugs at https://redmine.iopen.net/projects/groupserver

.. _GroupServer: http://groupserver.org/
.. _GroupServer.org: http://groupserver.org/
.. _OnlineGroups.Net: https://onlinegroups.net
.. _Michael JasonSmith: http://groupserver.org/p/mpj17
.. _Creative Commons Attribution-Share Alike 3.0 New Zealand License:
   http://creativecommons.org/licenses/by-sa/3.0/nz/
..  _Typeahead: http://twitter.github.com/bootstrap/javascript.html#typeahead
..  [#topic] See ``gs.group.messages.topic``.

..  LocalWords:  Typeahead json
