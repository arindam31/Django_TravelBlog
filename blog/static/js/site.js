var previousScroll = 0;
headerOrgOffset = $('#header').height();

$('#header-wrap').height($('#header').height());

$(window).scroll(function() {
    var currentScroll = $(this).scrollTop();
    if(currentScroll > headerOrgOffset) {
        if (currentScroll > previousScroll) {
            $('#header').animate({
                 top: '-60px'      //Change to Height of header
            }, 250);               //Mess with animate time
        } else {
            $('#header').animate({
                 top: '0px'
            },250);
            $('#header').addClass('fixed');
        }
    } else {
         $('#header').removeClass('fixed');   
    }
    previousScroll = currentScroll;
});