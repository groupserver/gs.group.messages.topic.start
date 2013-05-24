jQuery.noConflict();function GSGroupMessagesStartTopic(b){var c=null,e=null;function a(g,h){function f(i){e=i;
h(e)}if(e==null){jQuery.post("topics.json",f)}else{h(e)}}function d(){c=jQuery(b);
c.typeahead({source:a})}d()}jQuery(window).load(function(){GSGroupMessagesStartTopic("#form\\.topic")
});