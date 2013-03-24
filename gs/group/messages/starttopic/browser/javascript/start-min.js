jQuery.noConflict();function GSGroupMessagesStartTopic(b){var c=null,e=null;function a(g,h){function f(i){e=i;
h(e)}if(e==null){jQuery.post("topics.json",f)}else{h(e)}}function d(){c=jQuery(b);
c.typeahead({source:a})}d()}jQuery(window).load(function(){var a=null,b=null;a=jQuery("#gs-group-messages-topic-add-privacy").html();
b={animation:true,html:true,placement:"top",trigger:"click",content:a};jQuery("#gs-group-messages-topic-add-privacy-summary").popover(b);
GSGroupMessagesStartTopic("#form\\.topic")});