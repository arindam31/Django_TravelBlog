$('#likes').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/post/like/', {post_id: catid}, function(data){
               $('#like_count').html(data);
               // $('#likes').hide();
    });
});


