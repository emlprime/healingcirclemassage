$(function(){
    // fix for target="_blank"
    $("a[@rel~='external']").click(function(){
	window.open($(this).attr("href"));
	return false;
    });
});

$(document).ready(function() {
        $('#email_form').on('mouseenter', function(event) {
                form_unlocked = true;
	    });
        $('#email_form').on('mouseover', function(event) {
                form_unlocked = true;
	    });
        $('#email_form').on('tap', function(event) {
                form_unlocked = true;
	    });
        $('#email_form').click(function(event) {
                form_unlocked = true;
	    });

    $('#submit_email').click(function(event) {
	if (!form_unlocked) {
     	    event.preventDefault();
       	}
        if($('.honey').val()) {
     	    event.preventDefault();
	}
    });
});