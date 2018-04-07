$(window).scroll(function() {
    if ($(this).scrollTop() > 200) { //use `this`, not `document`
        $('#featured').css({
            'display': 'none'
        });
    }
});