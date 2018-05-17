$('#likes').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/post/like/', {post_id: catid}, function(data){
               $('#like_count').html(data);
               // $('#likes').hide();
    });
});

$('#post_comment').click(function(){
    var post_pk;
    post_pk = $(this).attr("data-post-pk");
    comment_details = $("#CommentBox").val();
    $.get(`/post/comment/`, {post_pk: post_pk, comment_details: comment_details}, function(result){
               var list_ = $('#comment-list ul');
               alert(result);
               list_.prepend(result);
    });
});
