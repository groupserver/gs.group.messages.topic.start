jQuery.noConflict();

function GSGroupMessagesStartTopic (topicInputId) {
    
    var topicInput = null, topics = null;

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
    var h = null, d = null;
    h = jQuery('#gs-group-messages-topic-add-privacy').html();
    d = {animation: true, html: true, placement: 'top', trigger: 'click', 
         content: h};
    jQuery('#gs-group-messages-topic-add-privacy-summary').popover(d);

    GSGroupMessagesStartTopic('#form\\.topic');
});