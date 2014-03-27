"use strict";
// Copyright © 2013, 2014 OnlineGroups.net and Contributors.
// All Rights Reserved.
//
// This software is subject to the provisions of the Zope Public License,
// Version 2.1 (ZPL). http://groupserver.org/downloads/license/
//
// THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
// WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
// WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND
// FITNESS FOR A PARTICULAR PURPOSE.
jQuery.noConflict();

function GSGroupMessagesStartTopic (topicInputId) {
    
    var topicInput=null, topics=null;

    function topic_source(query, process) {
        function load(data) {
            topics = data;
            process(topics);
        }
        if (topics == null) {
            jQuery.post('topics.json', load);
        } else {
            process(topics);
        }
    }

    function init() {
        topicInput = jQuery(topicInputId);
        topicInput.typeahead({source: topic_source});
    }
    init(); // Run the init automatically
}


jQuery(window).load( function () {
    GSGroupMessagesStartTopic('#form\\.topic');
});
