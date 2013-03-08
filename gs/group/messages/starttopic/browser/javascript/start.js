jQuery.noConflict();

function GSGroupMessagesStartTopic (topicInputId) {
    
    var topicInput = null;
    var topics = null;

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