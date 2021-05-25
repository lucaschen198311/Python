$(document).ready(function(){
    $("#email").keyup(function(){
        let data = $(".regist").serialize();
        $.ajax({
            url:"/email_check",
            method: "POST",
            data: data
        })
        .done(function(res){
            $(".emailMsg").html(res)
        })
    })
})

$(".search_bar").ready(function(){
    $(".name_search").keyup(function(){
        $.ajax({
            method: "GET",
            url:$(this).attr('action'),
            data:$(this).serialize()
        })
        .done(function(response){
            $(".name_result").html(response)
        })
    })
})